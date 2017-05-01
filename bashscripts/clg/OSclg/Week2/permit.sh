#!/bin/bash
read -p "Enter directory name:" direc
ls -l $direc | awk '{print $1, $9}'
