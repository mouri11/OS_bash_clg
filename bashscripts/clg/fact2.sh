#using recursion for !n
#!/bin/bash
fact()
{
    if [ $l -le 1 ]
    then
	echo 1
    else
	echo $[ $l * `fact $[$l-1]` ]
    fi
}
echo "!$l=" `fact $l`
