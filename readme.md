# L'AnoRitmo

# Come lanciare il programma 

Download i file delle statistiche delle precenti stagioni e copiale in `data/xlsxStats`.
Nota che c'è una discrepanza tra i dati: 
file anteriori al 2022-23 avevano la riga rm roulo mantra in meno ed inoltre i nomi dei giocatori sono Maiuscoli. 

Quindi scarica i file più recenti. Modificali:
1. Rimuovi colonna RM
2. Rendi UPPERCASE i nomi dei calciatori

Adesso Esegui:
`cd scripts` 
`sudo ./xlsx-to-csv.sh`
`sudo ./extractPlayers.sh`

Infine Esegui: 
python3 anoritmo.py


