#!/bin/bash
dir=/logs
out=/logs/temp
d=`date +%Y-%m-%d`
echo "the script begin at $d"

for file in $dir/*$d*; do
    #echo ${file#*$dir/}
    tar -jcf "$file".tar.bz2 $file
    mv "$file".tar.bz2 $out
done

