#!/bin/bash

file="../ex01/hh.csv"

(head -n 1 $file && tail -n +2 $file | sort -t, -k2,2 -k1,1)  > hh_sorted.csv