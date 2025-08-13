#!/bin/bash


file="../ex03/hh_positions.csv"
read jr md sr < <(awk -F, '
{
	gsub(/"/, "", $3);
	if ($3 ~ /Junior/) jr++; 
	else if ($3 ~ /Middle/) md++;
	else if ($3 ~ /Senior/) sr++
}
END {
		print jr+0, md+0, sr+0
}' "$file")

table="\"name\",\"count\"\n\"Junior\",$jr\n\"Middle\",$md\n\"Senior\",$sr"
echo -e "$table" > hh_uniq_positions.csv
cat hh_uniq_positions.csv

