# Where FlyNet sits, and a one-line experiment to try

## 1. What FlyNet's rule is, in the field's words

FlyNet's fast-weight update is

```
F = (1 - erase) * F + ws * write * outer(x_new, x_old)
```

This is a known recipe with a name. Miconi's **differentiable plasticity** (2018) is exactly "effective weight = W + A * Hebb", with A trained by backprop [1]. **Backpropamine** (2019) adds a gate the network produces itself that says how much to write each step [2]. FlyNet is Backpropamine with a second self-produced gate, `erase`, that controls decay instead of a fixed decay constant. The write strength `ws` is what Miconi calls eta, the plasticity learning rate, made trainable.

So training FlyNet with backprop through the whole episode is standard differentiable plasticity. It is not MAML: there is no inner gradient step on a labelled set, the "inner loop" is the Hebbian rule itself.

## 2. Hebb is a gradient step, which points at the experiment

`outer(x_new, x_old)` is the gradient, with respect to F, of the score `x_new · (F x_old)`. So F is already doing gradient ascent on an inner objective, one step per tick. The objective is linear, has no best value, so F grows without limit. That is why FlyNet needs a clamp and why the erase gate has been the hard part in runs 4 through 8B.

The 2024 to 2025 sequence-model literature made this observation and changed the inner objective. Schlag, Irie and Schmidhuber showed that linear attention is the same Hebbian outer-product write [3]. **Test-Time Training** (Sun et al. 2024) makes the fast state a small model that takes a gradient step on a self-supervised prediction loss each step [4]. **Titans** (Behrouz et al. 2024) adds momentum on that gradient and a learned, data-dependent forget gate [5]. **Gated DeltaNet** (Yang et al. 2025) is the minimal version: the delta rule plus a gate [6]. Wang et al. 2025 show all of these are one family, "test-time regression", differing only in the inner loss and the inner optimizer [7].

The delta rule is the simplest member. It replaces "write the full pattern" with "write only the part F failed to predict":

```
pred  = F x_old
F = (1 - erase) * F + ws * write * outer(x_new - pred, x_old)
```

It self-limits: once F predicts x_new, it stops writing. So the erase gate's job changes from "stop F saturating" to "forget the last trip".

## 3. The experiment

One knob, one line, in `flynet.py`:

```python
# Hebb (current)
hebb = x.unsqueeze(2) * x_old.unsqueeze(1)

# delta rule (Gated DeltaNet)
pred = torch.bmm(self.F, x_old.unsqueeze(2)).squeeze(2)
hebb = (x - pred).unsqueeze(2) * x_old.unsqueeze(1)
```

Everything else stays: gates, ws, A, the two-trip episode, the F-held-at-zero test. A `--rule hebb|delta` flag makes it a campaign run.

Prediction to write down before running: delta should need no clamp, should keep a wider F-allowed versus F-zero gap on 20 and 30 s wanders, and the erase gate should become food-selective sooner, because it is no longer fighting saturation. If that is wrong, that is a result too.

Second rung, a few more lines, is the Titans update: keep a momentum state S the same shape as F, `S = eta * S - ws * write * grad`, `F = (1 - erase) * F + S`, with eta either fixed or a fourth output gate. Titans' theta, eta and alpha map onto write, eta and erase here.

## 4. Biological reading

Hebb is "fire together, wire together". Delta is "wire together only when the post-synaptic cell was surprised". Both are three-factor rules; in Hebb the third factor is the global write gate, in delta it is a local prediction error. They make different predictions about what happens at a synapse when the fly revisits a heading it has already walked. Which one the hΔ store synapses look like is an open question.

## References

1. Miconi, Stanley, Clune. *Differentiable plasticity: training plastic neural networks with backpropagation.* ICML 2018. https://arxiv.org/abs/1804.02464
2. Miconi, Rawal, Clune, Stanley. *Backpropamine: training self-modifying neural networks with differentiable neuromodulated plasticity.* ICLR 2019. https://arxiv.org/abs/2002.10585
3. Schlag, Irie, Schmidhuber. *Linear Transformers Are Secretly Fast Weight Programmers.* ICML 2021. https://arxiv.org/abs/2102.11174
4. Sun et al. *Learning to (Learn at Test Time): RNNs with Expressive Hidden States.* 2024. https://arxiv.org/abs/2407.04620
5. Behrouz, Zhong, Mirrokni. *Titans: Learning to Memorize at Test Time.* 2024. https://arxiv.org/abs/2501.00663
6. Yang, Kautz, Hatamizadeh. *Gated Delta Networks: Improving Mamba2 with Delta Rule.* ICLR 2025. https://arxiv.org/abs/2412.06464
7. Wang et al. *Test-time regression: a unifying framework for designing sequence models with associative memory.* 2025. https://arxiv.org/abs/2501.12352
8. Finn, Abbeel, Levine. *Model-Agnostic Meta-Learning for Fast Adaptation of Deep Networks.* ICML 2017. https://arxiv.org/abs/1703.03400 (for the contrast in section 1)
