#!/bin/bash
clear
read -p "Enter name of directory: " direc
ls $direc -la | grep "^d" && ls $direc -la | grep -v "^d"
