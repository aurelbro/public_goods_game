#!/bin/bash

for r in 8 10 12 14; do
for mu in 0.0 0.01 0.02; do
python public_good_game_version_2_2.py $r $mu 10 0.5 0 &
done
done