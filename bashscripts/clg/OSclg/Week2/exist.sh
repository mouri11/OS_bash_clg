#!/bin/bash
read -p "Enter a name of directory or file:" name
echo ""
if [ -f $name ]
	then echo "File is in directory"
elif [ -d $name ]
	then echo "It is a sub-directory"
else echo "Doesn't exist"
fi
