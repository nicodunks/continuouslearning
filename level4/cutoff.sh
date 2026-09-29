#!/bin/bash
# stop all level 4 training at 11:50 (charter amendment 09:06)
until [ "$(date +%H%M)" -ge 1150 ]; do sleep 30; done
pkill -CONT -f train4.py; sleep 1; pkill -TERM -f train4.py
echo "$(date +%H:%M:%S) cutoff: all training stopped" >> narrative_sched.log
