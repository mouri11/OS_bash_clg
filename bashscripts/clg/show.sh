#!/bin/bash
#A shell script to read a directory name from the terminal and display director
#ies followed by files in sorted order
clear
read -p "Enter name of directory: " direc
ls $direc -la | grep "^d" && ls $direc -la | grep -v "^d"
