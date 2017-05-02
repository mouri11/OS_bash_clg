read -p "Enter name of file:" f
read -p "Enter string:" s
echo "Case sensitive"
grep -w $s -c $f
#cat inp.txt | grep -w "tokon" | wc -l

echo "Case sensitive"

grep -i -w $s -c $f
