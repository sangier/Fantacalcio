#!/bin/sh

Convert(){
    for file in ../data/xlsx/*.xlsx ; do
        echo "$file"
        filename=$(basename $file .xlsx)
        echo $filename 
        ssconvert $file ../data/csv/$filename.txt 
        tail -n +2 "../data/csv/$filename.txt" >../data/csv/$filename.csv
        rm  "../data/csv/$filename.txt"
    done
}



Convert