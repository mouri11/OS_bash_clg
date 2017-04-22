#!/bin/bash
read -p "Enter first number:" a
echo ""
read -p "Enter second number:" b
echo ""
read -p "Enter third number:" c
echo ""
if [ $a -gt $b ]
	then if [ $a -gt $c ]
		then echo "$a is the greatest"
	else echo "$c is the greatest"
	fi
elif [ $b -gt $c ]
	then echo "$b is the greatest"
	else echo "$c is the greatest"
fi
