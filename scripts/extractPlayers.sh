#!/bin/sh

CurrentPlayers(){
   #echo Inserisci l\'anno della stagione corrente \in formato 2021-22  
   #read varname
   #awk -F "," '{print $3} ' ../data/csv/Statistiche_Fantacalcio_$varname.csv > ../data/playerNames/names.csv
   rm names.csv
   awk -F "," '{print $3} ' ../data/csvStats/Statistiche_Fantacalcio_2021-22.csv > ../data/anoritmo/names.csv

}


PlayersStats(){
   IFS=''
   while read p; do
        echo $p
        for file in ../data/csvStats/*.csv ; do
        grep $p, $file >>../data/temp/stats.csv 
        done
   done <../data/anoritmo/names.csv

}


CurrentPlayers
PlayersStats
 #   for file in ../data/xlsx/*.xlsx ; do
 #       echo "$file"
 #       filename=$(basename $file .xlsx)
 #       echo $filename 
 #       ssconvert $file ../data/csv/$filename.csv
 #   done
