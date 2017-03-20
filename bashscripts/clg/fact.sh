#To calculate !n
#!/bin/bash
f=1
fact()
{
    read -p "Emter a number: " n 
    while (($n > 0))
    do
	let "f*=n"
	let "n-=1"
	echo "$f"
    done
    echo "$f"
}
fact $n 
