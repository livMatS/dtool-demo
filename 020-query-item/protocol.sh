#!/bin/bash -x

# either via cli or gui
dtool query '{"readme.project_id":"2021-10-07-sds-on-au-111-probe-and-substrate-merge-and-approach", "readme.step": {"$regex":"GromacsRelaxation"}}'

dtool ls -v s3://frct-simdata/f61e53e4-8ec1-4d0a-928e-bb973474db89

video_path=$(dtool item fetch s3://frct-simdata/1e387a1a-996b-4099-9196-1f08a99332f7 19b5d409e7c636411028ad8c9c5740988ca21479)

vlc $video_path
