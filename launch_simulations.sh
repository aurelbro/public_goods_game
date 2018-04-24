#!/bin/bash
for folder in /home/aurelien/istc/public_goods_game/experiments/; do
  for r in 8 10 12 14; do
    for mu in 0.0 0.01 0.02; do
      for Beta in 0.1 1 10; do
        for fc in 0 0.1 0.3 0.5 0.7 0.9 1; do
          for M in 0 2 4 6 8 10; do 
             python public_good_game_version_2_2.py $folder $r $mu $Beta $fc $M
            done
          done
        done
      done
    done
  done
done