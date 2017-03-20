#!/bin/bash
#A shell script to read a directory name from the terminal and will display 
#only the name and permission of the files
clear
read -p "Enter a valid directory name: " direc
ls -f -l $direc
