# Homing — a fly's unfinished story

A local, silent, 20-second Three.js animation accompanying the repository's four circuit hypotheses. All fly geometry, flight trails, vectors, compass graphics, and neuron callouts are rendered in WebGL. There is no hero layout or separate brain panel. Minimal playback controls are HTML and disappear during playback.

## Run

Requires Node.js 20.19+ or 22.12+.

```sh
cd flight-scene
npm ci
npm run dev -- --port 5173
```

Open http://127.0.0.1:5173. No API keys, external models, or connectome download are required. Fonts and their OFL licenses are bundled locally.

- **Space**: play / pause
- **Left / right arrow**: step half a second
- **Timeline**: scrub precisely; pauses playback
- **Chapter buttons**: jump and play
- **Restart**: replay the film
- **Fullscreen**: expand the arena

Reduced-motion preferences start the scene paused. The animation stops at 20 seconds so the final question can be read.

## Timing

| Time | Scene |
| --- | --- |
| 0–5s | Deep XYZ flight, equal-time sampled gold dots, deceleration into freeze |
| 5–9s | A pulse reads the fixed dots; the running vector terminates at the fly; store callouts |
| 9–15s | hΔM callout, 180° vector reversal, resumed flight |
| 15–17.5s | FB3A / PS196_b, speed streaks and turning arc |
| 17.5–20s | EPG / PEN feedback, modeled compass lag during a turn |

The flying animal and XYZ integration are illustrations extending the motivating walking-navigation story. The pulse computes displacement from the actual 3D trajectory, but dots represent movement samples, not anatomical synapses. This is an authored hypothesis visualization, not a whole-brain simulation or a reproduced flight experiment. Flight behavior, synaptic storage, and signal identities are not claimed as validated by this animation.

## Build and check

```sh
npm run build
# With the dev server running, and Playwright Chromium installed:
npm test
npm run capture
```

If Chromium is absent, install it with `npx playwright install chromium`. The browser check covers playback, restart, chapter boundaries, scrubbing, mobile layout, and reduced motion. `capture` writes representative frames to `/tmp/homing-*.png`.

The scene is deterministic when seeking: `window.__flight.seek(seconds)` pauses at any frame. `window.__flight.play()` resumes. This is useful for screenshots and a later video export.

The procedural insect, annotations, and timeline live in `src.js`; the editorial layout is in `style.css`. The path and callouts are deliberately illustrative rather than anatomical neuron reconstructions.
