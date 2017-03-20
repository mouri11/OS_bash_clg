#To generate n fibonacci numbers with initial numbers being 3 and 5
#!/bin/bash
fibo()
{
    a=3
    b=5
    read -p "Enter no. of terms to generate: " n
    echo -n "$a, "
    echo -n "$b, "
    let "n-=2"
    until [ $n -eq 0 ]
    do 
	let "c=$a + $b"
	echo -n "$c, "
	a=$b
	b=$c
	let "n -= 1"
    done
    echo ""
}
fibo $n
