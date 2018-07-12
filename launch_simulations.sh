#!/bin/bash

seed=$1
echo $seed
mkdir simulations_with_leadership_exponential_roulette_wheel_death/;
  for r in 3. 5. 7.; do
        for Beta_follow in  1. ; do
          for fc in 0.1 0.3 0.5 0.7 0.9; do
            for M in 0 4 10; do
               python public_good_game_with_leadership_exponential_roulette_wheel_death.py simulations_with_leadership_exponential_roulette_wheel_death/ $r $Beta_follow $fc $M $seed
            done
          done
        done
  done
