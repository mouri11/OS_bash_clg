gcd()
{
	read -p "Enter first: " a
	read -p "Enter second number: " b
	r=1
	until [ $r -eq 0 ]
	do
		let "r= $a % $b "
		a=$b
		b=$r
	done
	echo "HCF is: "$a
}

gcd $a $b
