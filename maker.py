import json
import sys
from os import system, name

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def esportaCSV(jsFile):
    dict={}
    filecsv=""
    with open(jsFile,"r") as json_file:
        dict=json.load(json_file)
    lista=list(dict.keys())
    for i in range(len(lista)):
        filecsv=filecsv+lista[i]
        if i < len(lista):
            filecsv=filecsv+","
    filecsv=filecsv+"\n"
    for i in range(len(dict[lista[0]])):
        for c in range(len(lista)):
            filecsv=filecsv+dict[lista[c]][i]
            if c < len(lista):
                filecsv=filecsv+","
        filecsv=filecsv+"\n"
    csvname=input("nome del filce csv> ")
    f=open(csvname,"w")
    f.write(filecsv)
    f.close()

def ricerca(jsFile):
    dict={}
    with open(jsFile,"r") as json_file:
        dict=json.load(json_file)
    lista=list(dict.keys())
    print(lista)
    while True:
        ricerca=input("> ")
        try:
            listRic=ricerca.split(",")
            break
        except:
            print("[chiave],[valore da ricercare]")
    chiave=""
    trovato=False
    corrispondenza=False
    try:
        for i in range(len(lista)):
            if listRic[0]==lista[i]:
                chiave=listRic[0]
                trovato=True
    except:
        print("Valori immessi non validi.\n[chiave],[valore da ricercare]")
    stampa=""
    if trovato:
        try:
            for i in range(len(dict[chiave])):
                if listRic[1] in dict[chiave][i]:#dict[chiave][i]==listRic[1]:
                    for c in range(len(lista)):
                        stampa=stampa+lista[c]+": "+dict[lista[c]][i]+"\n"
                        corrispondenza=True
        except:
            print("Valori immessi non validi.\n[chiave],[valore da ricercare]")
        print(stampa)
    if not(corrispondenza):
        print("Nessuna corrispondenza")

def comandi(jsFile):
    comando=input("> ")
    if comando=="I":
        insert(jsFile)
    elif comando=="R":
        ricerca(jsFile)
    elif comando=="CSV":
        esportaCSV(jsFile)
    elif comando=="L":
        print("leggi")
    elif comando=="E":
        sys.exit()
    else:
        print("Comando non riconosciuto.\nComandi disponibili: I inserisci dati - R ricerca - L leggi - E esci")

def pydb():
    #make a .py file to manage your light db
    nomeGest=input("Nome del gestionale> ")
    jsFile=input("Inserisci il nome del file JSON> ")
    dict={}
    with open(jsFile,"r") as json_file:
        dict=json.load(json_file)
    fileGest={}
    keyN="0"
    fileGest[keyN]="import maker\n"
    keyN=str(int(keyN)+1)
    fileGest[keyN]="maker.clear()\n"
    keyN=str(int(keyN)+1)
    fileGest[keyN]="#coder Porcari Daniele\n"
    keyN=str(int(keyN)+1)
    fileGest[keyN]="print(\"light DB gestionale costruito con maker\")\n"
    keyN=str(int(keyN)+1)
    fileGest[keyN]="print(\"\")\n"
    file=''
    kDict=list(dict.keys())
    keyN=str(int(keyN)+1)
    fileGest[keyN]="print(\"Comandi disponibili: I inserisci dati - R ricerca - CSV Esporta file in csv - E esci\")\n"
    keyN=str(int(keyN)+1)
    fileGest[keyN]="jsFile=\""+jsFile+"\"\n"
    keyN=str(int(keyN)+1)
    fileGest[keyN]="while True:\n\tmaker.comandi(jsFile)"
    chiavi=list(fileGest.keys())
    for i in range(len(chiavi)):
        file=file+fileGest[chiavi[i]]
    print(file)
    f=open(nomeGest,"w")
    f.write(file)
    f.close()
    return

def makeJSON(jsFile):
    dict={}
    exit=False
    while not(exit):
        chiave=input("key> ")
        if chiave=='#e':
            exit=True
        else:
            lista=[]
            dict[chiave]=lista
    with open(jsFile,"w") as json_file:
        json.dump(dict, json_file)

def insert(jsFile):
    dict={}
    with open(jsFile,"r") as json_file:
        dict=json.load(json_file)
    klist=list(dict.keys())
    print(klist)
    exit=False
    while not(exit):
        chiave=input("key> ")
        if chiave=='#e':
            exit=True
        else:
            val=input("val> ")
            for i in range(len(klist)):
                if chiave==klist[i]:
                    dati=[]
                    dati=dict[chiave]
                    dati.append(val)
                    dict[chiave]=dati
                    with open(jsFile,"w") as json_file:
                        json.dump(dict, json_file)

if __name__=="__main__":
    makeJSON("prova.json")
    insert("prova.json")
