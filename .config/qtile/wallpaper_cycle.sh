#!/bin/bash
current_wall=$(grep "/home" ~/.fehbg | cut -d " " -f 4- | cut -d "'" -f 2)
wall_dir=~/Pictures/Wallpapers
total_walls=$(ls $wall_dir/* | wc -l)
wall_no=1

for wall in $wall_dir/*; do
    if [[ $wall == $current_wall ]]; then
        current_wall_found=true
        break
    fi
    wall_no=$((wall_no + 1))
done

if [[ $1 == "--next" ]]; then
    if [[ $current_wall_found == true ]] && [[ $wall_no != $total_walls ]]; then
        feh --bg-scale "$(ls -d $wall_dir/* | sed -n $((wall_no + 1))p)"
    else
        feh --bg-scale "$(ls -d $wall_dir/* | head -n 1)"
    fi
elif [[ $1 == "--prev" ]]; then
    if [[ $current_wall_found == true ]] && [[ $wall_no != 1 ]]; then
        feh --bg-scale "$(ls -d $wall_dir/* | sed -n $((wall_no - 1))p)"
    else
        feh --bg-scale "$(ls -d $wall_dir/* | tail -n 1)"
    fi
else
    echo -e "No option specified.\n"\
            "\t--next\tchange to next wallpaper\n"\
            "\t--prev\tchange to previous wallpaper"
fi

