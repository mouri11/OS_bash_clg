read -p "Enter directory name: " dir
mkdir $dir
cd $dir

# Accept number of files to be present
read -p "Enter number of files to be added: " n

for i in $( seq 1 $n );
do
	read -p "Enter name of the file: " name
	touch $name
done

#$#

#$@

ls -l

chmod +x *

ls -l

cd ..
pwd
