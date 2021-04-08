import maker
import sys
        
maker.clear()
print("LightDB - by Porcari Daniele")
print("Comandi: n nuovo database - a aggiungi dati al db esistente - c costruisci file python per gestione db - e esci")
while True:
    comando=input("> ")
    if comando=="n":
        file=input("nome del db> ")
        maker.makeJSON(file)
    elif comando=="a":
        file=input("nome del db> ")
        maker.insert(file)
    elif comando=="c":
        maker.pydb()
    elif comando=="e":
        sys.exit()
