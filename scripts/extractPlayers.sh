#!/bin/sh

CurrentPlayers(){
   #echo Inserisci l\'anno della stagione corrente \in formato 2021-22  
   #read varname
   #awk -F "," '{print $3} ' ../data/csv/Statistiche_Fantacalcio_$varname.csv > ../data/playerNames/names.csv
   rm names.csv
   awk -F "," '{print $3} ' ../data/csvStats/Statistiche_Fantacalcio_2021-22.csv > ../data/anoritmo/names.csv
   rm ../data/anoritmo/PlayerStats.csv 

}


PlayersStats(){
   IFS=''
   while read p; do
        echo $p
        for file in ../data/csvStats/*.csv ; do
        filename=$(basename $file .csv)
        echo $filename        
        mydate=$(echo -n $filename | tail -c 8)
        echo $mydate
        #awk -v d="$mydate" -F"," 'BEGIN { OFS = "," } {$5=d; print}' $file  > ../data/temp/$filename.csv
        awk '{print $1,$2,$3,$4,$5,$6,$7,$8,$9,$10,$11,$12,$13,$14,$15,$16,$17,F}' FS=, OFS=, F="$mydate" $file  > ../data/temp/$filename.csv
        grep $p, ../data/temp/$filename.csv >>../data/anoritmo/PlayerStats.csv 
        done
   done <../data/anoritmo/names.csv

}


CurrentPlayers
PlayersStats
rm ../data/temp/*.csv
 #   for file in ../data/xlsx/*.xlsx ; do
 #       echo "$file"
 #       filename=$(basename $file .xlsx)
 #       echo $filename 
 #       ssconvert $file ../data/csv/$filename.csv
 #   done
