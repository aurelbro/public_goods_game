#!/bin/bash
  for r in 8 12; do
    for mu in 0.0 0.01 ; do
      for Beta in 10; do
        for fc in 0.1 0.3 0.5 0.7 0.9; do
          for M in 0 4 10; do 
             python public_good_game_version_4.py simulations/ $r $mu $Beta $fc $M
            done
          done
        done
      done
    done
