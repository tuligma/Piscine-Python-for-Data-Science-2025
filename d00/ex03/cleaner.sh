#!/bin/bash

file="../ex02/hh_sorted.csv"

# awk -F',' 'gsub(/Junior/, "Junior", $3); gsub(/Middle/, "Middle", $3); gsub(/Senior/, "Senior", $3);'
(head -n 1 $file && tail -n +2 $file | \
 awk -v FPAT='([^,]+)|(\"[^\"]+\")' -v OFS=, '
 	{
		if ($3 ~ /Junior/ && /Middle/) {
			$3 = "\"Junior/Middle\""
		} else if ($3 ~ /Middle/ && /Senior/) {
			$3 = "\"Middle/Senior\""
		} else if ($3 ~ /Senior/ && /Junior/) {
			$3 = "\"Junior/Senior\""
		}else if ($3 ~ /Junior/) {
			$3 = "\"Junior\""
		} else if ($3 ~ /Middle/) {
			$3 = "\"Middle\""
		} else if ($3 ~ /Senior/) {
			$3 = "\"Senior\""
		} else {
			$3 = "\"-\""
		}
		
		
		print
 	}') > hh_positions.csv