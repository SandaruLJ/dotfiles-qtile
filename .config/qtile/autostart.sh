#!/bin/bash
feh --bg-scale --randomize ~/Pictures/Wallpapers/* &
picom --experimental-backend -b &
xset r rate 400 50 &
spice-vdagent &
