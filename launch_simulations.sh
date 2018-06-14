#!/bin/bash

seed=$1
echo $seed
mkdir simulations_with_leadership_normal/;
  for r in 3. 5. 7.; do
    for mu in 0.0  ; do
      for Beta in 10; do
        for fc in 0.1 0.3 0.5 0.7 0.9; do
          for M in 0 4 10; do
              python public_good_game_with_leadership_normal.py simulations_with_leadership_normal/ $r $mu $Beta $fc $M $seed
            done
          done
        done
      done
    done

