read -p "Enter a file/directory name: " name

if [ -d $name ]
then
	echo "Directory"
elif [ -f $name ]
then
	echo "File"
else
	echo "NOT PRESENT"
fi
