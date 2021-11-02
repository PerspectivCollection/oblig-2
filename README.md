# oblig-2

## Har gjordt 
Jeg har leget en action får at tester skal kjøre etter hver "comit" til github. 
Acton som har blit brukt er fra "Python package" under action. Pakken har opprinelig 
støtte for python 3.7, 3.8, 3.9. Jeg en endret denne til til 3.9. 
Jeg har lagt til "pip install pytest" får å få testene til å fungere. 

## Action fungerer følgende
Den kjører ubuntu som er en linux virutuel maskin eller i en kontainer.
Den bygger også selve python versonen som er brukt, i dette tilfelet er 3.9 i bruk. 
Pakken pip instaleres og sjekkes for oppdatering. 

## kjør testene i terminal 
```
pytest test_leap_year.py
```
