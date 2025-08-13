#!/bin/bash

file="../ex03/hh_positions.csv"
header=$(head -n 1 $file)

tail -n +2 $file | \
awk -F, -v header="$header" '
{ 
	dt_fmt = substr($2, 2, 10)
	out_file = dt_fmt ".csv"

	if (!(out_file in seen)) {
		print header > out_file
		seen[out_file]=1
	}
	print >> out_file
}'
