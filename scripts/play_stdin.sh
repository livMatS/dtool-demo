#!/bin/bash
DELAY=200
ORIGINAL_KEYBOARD_LAYOUT=$(setxkbmap -print -verbose 10 | grep layout | awk '{print $2}')
setxkbmap -layout us
terminator &
sleep 1
while IFS= read -r line
do
  xdotool type --delay $DELAY "$line"
  sleep 0.2
  xdotool key Return
  sleep 1
done < stdin_file
setxkbmap -layout ${ORIGINAL_KEYBOARD_LAYOUT}
