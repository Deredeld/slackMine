#!/bin/bash
while ! python2.7 /home/norman/slack/slackMine/mining.py
do
  sleep 1
  echo "Restarting program..."
done

