import pandas as pd
from datetime import datetime

#f = open('wapRDA.txt','r', encoding="utf-8") #declara el arhcivo y lo apunta
f = open('wapSDI.txt','r', encoding="utf-8") #declara el arhcivo y lo apunta
msg = f.readline()   #lee primera linea
lst = []   #crea una lista vacia

for msg in f.readlines():   #por cada linea que lea...
    if ' - ' in msg and ': ' in msg:  #valida que la linea sea correcta; elimina el resto
        div1 = msg.split('-')         #hace primera division con "-" y obtiene fecha
        fh = div1[0].strip()
        div2 = div1[1].split(':')     #hace subdivision con ":" y obtiene usuario y texto
        us = div2[0].strip()
        tx = div2[1].strip()
        lst.append([fh, us, tx,])     #agrega el registro a la lista

dataf = pd.DataFrame(lst)                       #convierte toda la lista en DF
dataf.columns=['Fecha-Hora','usuario', 'texto'] #le pone headers al dataframe
#dataf.to_csv('waprda.csv', header=True, index=False, encoding='utf-8') # lo graba en csv
dataf.to_csv('wapsdi.csv', header=True, index=False, encoding='utf-8') # lo graba en csv
f.close()
