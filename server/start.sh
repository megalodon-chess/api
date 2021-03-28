#!/bin/bash

nohup python3 ./buildbot.py > ./buildbot.out &
nohup python3 ./connection.py > ./connection.out &
