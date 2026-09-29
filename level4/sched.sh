#!/bin/bash
# level 4 scheduler: resume paused runs as cores free up, so every run finishes its full budget.
cd "$(dirname "$0")"
done_count() { ls $1 2>/dev/null | wc -l; }
log() { echo "$(date +%H:%M:%S) $*" | tee -a narrative_sched.log; }
# 1. when the three-rate-3e-4 rival colds finish (6 runs), resume the 1e-3 rival colds
until [ $(done_count "runs/*_c?_lr3e-4/final.pt") -ge 6 ]; do sleep 20; done
for p in $(pgrep -f "run (twin_c|gru_c)[0-9]_lr1e-3"); do kill -CONT $p; done; log "resumed 1e-3 rival colds"
# 2. when the warm twins B finish, resume the original warm twins
until [ $(done_count "runs/twinB_w*/final.pt") -ge 4 ]; do sleep 20; done
for r in twin_w28 twin_w40 twin_w41 twin_w45; do kill -CONT $(pgrep -f "run $r ") ; done; log "resumed original warm twins"
