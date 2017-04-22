#!/bin/bash
fibo()
{
	a=3
	b=5
	read -p "Enter no of terms to generate: " n
	echo -n "$a "
	echo -n "$b "
	n=$((n-2))
	until [ $n -eq 0 ]
	do
		c=$(($a+$b))
		echo $c|bc
		a=$b
		b=$c
		n=$((n-1))
	done
	echo ""
}
fibo $n
