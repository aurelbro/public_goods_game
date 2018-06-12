#!/bin/bash

#seed=$1

mkdir simulations_4;
  for r in 3. 5. 7.; do
    for mu in 0.0  ; do
      for Beta in 10; do
        for fc in 0.1 0.3 0.5 0.7 0.9; do
          for M in 0 4 10; do
            for seed in $1; do 
              python public_good_game_version_4.py simulations_4/ $r $mu $Beta $fc $M $seed
            done
          done
        done
      done
    done
  done
