# L'AnoRitmo***

## Gli inizi ed il battesimo  

AnoRitmo è il nome con cui gli amici della nostra lega FantaLemon8 hanno battezzato il nostro algoritmo per l'anilisi statistica del fantacalcio. 

Motivati dalle costanti umiliazioni dei primi anni fantacaliscistici, nel 2018 abbiamo deciso di sviluppare uno strumento che ci consentisse di giungere alla fatidica asta del fantacalcio un po` più preparati. 

Gli anni di testing hanno porhanno portato ai segunti risultati: 
- 2018-19 : Fantalemon8,1o Scontri, ? Punti 
- 2019-20 : Fantalemon8,1o Scontri, ? Punti   
- 2020-21 : Fantalemon8,1o Scontri, 1o Coopa
- 2021-22 : Due Partecipazioni  
    -   Fantalemon8, 5o a Scontri, 2o Punti
    -   Fantallorando, 2o a Scontri, 1o Punti, 1o Coppa 

Data la natura dei risultati mostrati, il lettore potrà ben comprendere la ratio della geniale storpiatura, partorita dai nostri amici della lega Fantalemon8, a danno della parola algrotimo in AnoRitmo. Daltronde, il fattore culo è senza dubbio una discriminante nel fantalcacio. Per tale ragione, l'anoritmo è stato pensato per carcare di massimizzare la probabilità di avere culo al fantacalcio.
Con questo idea in mente abbiamo deciso di raccogliere i dati delle precedenti 5 stagioni ed abbiamo cominciaato a giocarci un pò. 

## Lo studio

Per ogni calciatore presente nel listone dell'anno corrente, si prendono i dati, se presenti, delle ultime 5 stagioni. 

Obiettivi: 
- Classificare la Mv e la Fv dei calciatori in una fascia di utilià A,B,C,D.   
- Calcolare la costanza dei calciatori nel corso delle stagioni, classificandola in una fascia di utilità A,B,C,D. 

### Le fasce d'utilità 


| Fascie | Ruolo | Mv           | Fv   |
|--------|-------|--------------|------|
| A      | Att   | Mv > 7.5     | >7.5 |
| B      | Att   | 7.5 > Mv > 7 | V    |
| C      | Att   | 7 > Mv > 6.5 |      |
| A      | Cen   |              |      |
| B      | Cen   |              |      |
| C      | Cen   |              |      |
| A      | Dif   |              |      |
| B      | Dif   |              |      |
| C      | Dif   |              |      |
| A      | Por   |              |      |
|        |       |              |      |
|        |       |              |      |


### Il fattore costanza

Per considerare il fattore continuatà abbiamo calcolato le medie MvH e FvH rispettivamente Media Voto Storica e Fantamedia Vodto storicha e le abbiamo classificate in base alle fasce di utilità. 

### La strategia d'asta 
La strategia d'asta consiste nel cercare di avere la rosa composta per la maggioranza di giocatori appartenenti alla fascia A-Ah. 
La variazione tra la fascia della Mv ed MvH ci fornisce un idea dell'andamento del calciatore in questione. 

Nella nostra lega giochiamo con il modificatore di difesa, e per cui abbiamo scelto di dare priorità a quei reparti dove tali giocatori scarseggiano. 

E.g.  
1000 Credi 
400 Difesa+Portiere
250 Centrocampo 
350 Attacco 

### Come lanciare il programma 





