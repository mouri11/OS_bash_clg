#!/bin/bash
gcd()
{
    read -p "Enter the first number: " a
    echo ""
    read -p "Enter the second number:  " b
    echo ""
    r=1
    echo "The gcd of $a and $b is: "
    until [ $r -eq 0 ]
    do
	let "r=  $a % $b "
	a=$b
	b=$r
    done
    echo "$a"
}

gcd $a $b
