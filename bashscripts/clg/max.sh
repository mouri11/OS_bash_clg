#A shell script to find the max of three nos
#!/bin/bash
read -p "Enter first number: " x
echo ""
read -p "Enter second number: " y
echo ""
read -p "Enter third number: " z
echo ""
if (( $x > $y ))
    then if (( $x > $z))
	then echo "$x is the greatest,"
    else echo "$z is the greatest."
    fi	
elif (($y > $z ))
    then echo "$y is the greatest."
    else echo "$z is the greatest."
fi
