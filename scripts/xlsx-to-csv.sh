#!/bin/sh

Convert(){
    max=0
    for file in ../data/xlsx/*.xlsx ; do
        echo "$file"
        filename=$(basename $file .xlsx)
        echo $filename 
        ssconvert $file ../data/csv/$filename.csv
    done
}



Convert