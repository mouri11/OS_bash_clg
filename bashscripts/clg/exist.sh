#A shell script to read a file/directory name from the terminal, check if it is in current directory, and if yes, display if it is a file or directory
#!/bin/bash
read -p "Enter a file or directory name: " arg
echo ""
if [ -f $arg ]
then echo "$arg is a file and it is in current directory."
elif [ -d $arg ]
then echo "$arg is a subdirectory of current directory."
else echo "$arg doesn't exist."
fi
