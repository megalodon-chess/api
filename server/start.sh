#!/bin/bash

nohup python3.8 ./buildbot.py > ./buildbot.out &
nohup python3.8 ./connection.py > ./connection.out &
