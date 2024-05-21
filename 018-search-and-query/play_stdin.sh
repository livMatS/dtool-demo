#!/bin/bash
DELAY=200
ORIGINAL_KEYBOARD_LAYOUT=$(setxkbmap -print -verbose 10 | grep layout | awk '{print $2}')
setxkbmap -layout us
terminator &
sleep 1
xdotool type --delay $DELAY "source ../venv/bin/activate"
sleep 0.2
xdotool key Return
sleep 3

xdotool type --delay $DELAY "asciinema rec --overwrite recording.cast"
sleep 0.2
xdotool key Return
sleep 3

xdotool type --delay $DELAY "cat dtool.json"
sleep 0.2
xdotool key Return
sleep 3

xdotool type --delay $DELAY "mkdir -p ~/.config/dtool"
sleep 0.2
xdotool key Return
sleep 3

xdotool type --delay $DELAY "cp dtool.json ~/.config/dtool/"
sleep 0.2
xdotool key Return
sleep 3

xdotool type --delay $DELAY "source ../005-setup/venv/bin/activate"
sleep 0.2
xdotool key Return
sleep 3

xdotool type --delay $DELAY "dtool search --help"
sleep 0.2
xdotool key Return
sleep 3

xdotool type --delay $DELAY "dtool search demo"
sleep 0.2
xdotool key Return
sleep 3

xdotool type --delay $DELAY "test_password"
sleep 0.2
xdotool key Return
sleep 3

xdotool type --delay $DELAY "dtool readme show s3://test-bucket/5e507882-cf44-42a3-8af0-3b1541a59cc1"
sleep 0.2
xdotool key Return
sleep 3

xdotool type --delay $DELAY "dtool query --help"
sleep 0.2
xdotool key Return
sleep 3

xdotool type --delay $DELAY 'dtool query '"'"'{"readme.owners.name":{"$regex":"Hörmann"}, "readme.creation_date":{"$regex":"^2024"}}'"'"
sleep 0.2
xdotool key Return
sleep 3

xdotool type --delay $DELAY 'dtool query '"'"'{"readme.owners.name":{"$regex":"H.*rmann"}, "readme.creation_date":{"$regex":"^2024"}}'"'"
sleep 0.2
xdotool key Return
sleep 3

xdotool type --delay $DELAY "dtool readme edit s3://test-bucket/5e507882-cf44-42a3-8af0-3b1541a59cc1"
sleep 0.2
xdotool key Return
sleep 3

for run in {1..4}; do
  xdotool key Down
  sleep 0.2
done

for run in {1..29}; do
  xdotool key Right
  sleep 0.2
done

for run in {1..2}; do
  xdotool key BackSpace
  sleep 0.2
done

setxkbmap -layout ${ORIGINAL_KEYBOARD_LAYOUT}
xdotool type --delay $DELAY "ö"
setxkbmap -layout us

xdotool key 'ctrl+o'
sleep 0.2
xdotool key Return
sleep 0.2
xdotool key 'ctrl+x'
sleep 0.2

xdotool type --delay $DELAY 'dtool query '"'"'{"readme.owners.name":{"$regex":"H.*rmann"}, "readme.creation_date":{"$regex":"^2024"}}'"'"
sleep 0.2
xdotool key Return
sleep 3

xdotool type --delay $DELAY "exit"
sleep 0.2
xdotool key Return
sleep 3

xdotool type --delay $DELAY "exit"
sleep 0.2
xdotool key Return

setxkbmap -layout ${ORIGINAL_KEYBOARD_LAYOUT}
