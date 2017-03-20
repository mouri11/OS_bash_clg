#A shell script to read a directory name from the terminal and display directories followed by files in sorted order
#!/bin/bash
clear
read -p "Enter name of directory: " direc
ls $direc -la | grep "^d" && ls $direc -la | grep -v "^d"
