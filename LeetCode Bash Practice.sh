# Valid Phone Numbers.sh
grep -P "^(\(\d{3}\) |\d{3}-)\d{3}-\d{4}$" file.txt


# Tenth Line
sed "10q;d" file.txt | sed -n "10p" file.txt


