#!/bin/bash

nohup python ./buildbot.py > ./buildbot.out &
nohup python ./connection.py > ./connection.out &
