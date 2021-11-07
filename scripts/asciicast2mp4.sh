#!/bin/bash
# create mp4 video from asciinema recording
# needs slop, https://github.com/naelstrof/slop, select window to record by mouse click
# needs ffmpeg
WINDOW_TITLE=dtool-demo
function title { PROMPT_COMMAND="echo -ne \"\033]0;$1\007\""; }
title "${WINDOW_TITLE}"
export PS1='> '
clear
VIDEO_SIZE=$(slop -f '-video_size %wx%h -i +%x,%y')
ffmpeg -f x11grab -framerate 25 ${VIDEO_SIZE} -y recording.mp4 > /dev/null 2>&1 &
asciinema play -i 1 -s 2 recording.cast
kill %1
