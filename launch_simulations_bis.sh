#!/bin/bash

seed=$1
echo $seed
mkdir simulations_with_leadership_egalitarian/;
  for r in 3. 5. 7.; do
    for mu in 0.0  ; do
      for Beta_imit in 10.; do
        for Beta_follow in 0.1 1. ; do
          for fc in 0.1 0.3 0.5 0.7 0.9; do
            for M in 0 4 10; do
                python public_good_game_with_leadership_egalitarian.py simulations_with_leadership_egalitarian/ $r $mu $Beta_imit $Beta_follow $fc $M $seed
            done
          done
        done
      done
    done
  done