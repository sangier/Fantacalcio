#!/bin/sh

Convert(){
    for file in ../data/xlsxStats/*.xlsx ; do
        echo "Scanning New File.."
        echo "$file"
        filename=$(basename $file .xlsx)
        echo $filename
        echo "Removing Old Output.."
        rm  "../data/csvStats/$filename.csv"
        echo "Converting Files.." 
	    mkdir -p ../data/temp/
        ssconvert $file ../data/temp/$filename.csv
        
        #cat ../data/temp/$filename.txt
        echo "Deleting First two lines.."
        #sed 1,2d ../data/csvStats/$filename.csv
        sed 1,2d "../data/temp/$filename.csv" >../data/csvStats/$filename.csv
        sed -n '2 p' ../data/temp/$filename.csv > ../data/anoritmo/headers.csv
        echo "Removing Temp Files.."
        rm  "../data/temp/$filename.csv"
        echo "Exiting Program.."
    done
}



Convert
