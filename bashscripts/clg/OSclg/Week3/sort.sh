#!/bin/bash
arr=(8 7 9)
sorted=( $( printf "%s\n" "${arr[@]}" | sort -n ) )
echo ${sorted[*]}
