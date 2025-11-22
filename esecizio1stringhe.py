# Chiedi una frase e inverti l'ordine delle parole
frase = input("Inserisci una frase: ")
parole = frase.split() #.split() senza argomenti divide la stringa sugli spazi: "ciao come stai" --> ["ciao", "come", "stai"]
frase_invertita = " ".join(parole[::-1]) #parole[::-1] --> 	È uno slice con passo -1 → prende la lista al contrario / .join(...) --> Prende tutti gli elementi della lista e li unisce in una stringa, mettendo uno spazio tra uno e l’altro
print(frase_invertita)

# Controlla se la frase è un palindromo (ignora spazi e maiuscole)
frase = input("Inserisci una frase: ")
#1. Normalizza la frase: tutto minuscolo e senza spazi
testo = frase.replace(" ", "").lower()

#2. Confronta il testo con la sua versione invertita
if testo == testo[::-1]:
    print("La frase è un palindromo")
else:
    print("La frase NON è un palindromo")

# replace(" ", "") --> sostituisce tutti gli spazi con una stringa vuota
# .lower() --> converte tutto in minuscolo
# testo[::-1] --> prende la stringa testo al contrario (slice con passo -1)

#Esercizio1: estrapolare il primo e l'umtimo carattere presenti nella parola
testo = "Python"
print("Primo carattere: ", testo[0])
print("ultimo carattere: ", testo[5]) # si può anche inserire [-1], perché prende direttamente l'ultimo carattere senza stare a contare il numero corretto.

#Esercizio2: convertire il maiuscolo e il minuscolo 
testo = "CoMpUtEr"
print(testo.upper()) # per ottenere un output con caratteri tutti MAIUSCOLI si usa questo
print(testo.lower()) # per ottenere un output con caratteri tutti MINUSCOLI si usa questo

#Esercizio3: contare quante volte compare una determinata lettera
testo = "programmazione"
lettera = "a"
conteggio = testo.count(lettera) # .count() --> prende il testo che hai indicato e conta quante volte compare una determinata lettera o sequenza di lettere.
print(f"la lettera '{lettera}' compare {conteggio} volte.") 

#Esercizio4: verificare se una parola inizia e finisce con una lettera sfecifica
testo = "fantastico"
print(testo.startswith("f")) # .startwith --> ci restituisce un boolean e ci dice se effettivamente il testo all'interno della nosta variabile inizia con una determinata lettera.
print(testo.endswith("o")) # .endswith --> ci restituisce un boolean e ci dice se effettivamente il testo all'interno della nosta variabile finisce con una determinata lettera.

#Esercizio4: invertire una stringa
testo = "Python"
print(testo[::-1]) # Python al contrario
print(testo[::-2]) # [::-2] --> vuol dire che deve prendere un carattere ogni due (sempre al contrario) = Python --> nohtyP --> nhy

#Esercizio5: rimuovere gli spazi all'inizio e alla fine della stringa
testo = "       ciao mondo      "
print(testo.strip()) # .strip() --> serve a togliere gli aspazi prima e dopo della stringa (gli spazi vengono considerati come caratteri)

#Esercizio6: prendere le prime tre lettere e ripeterle per 3 volte
parola = "programmazione"
print(parola[:3]*3) # [:3] --> quando non si mette niente prima dei ":" è sottointeso che parta dal primo carattere della stringa - il 3 indica dove si deve fermare e non prendere più in cosniderazione i caratteri (l'ultimo carattere che deve prendere in considerazione è quello prima, in questo caso il numero 2), ricorda che parte dallo "0" e quindi il carattere numero 3 in "programmazione" è la "g".
print(parola[2:10]*3) # [2:10] --> qua prende in considerazione dal carattere numero 2 (quindi il terzo perche si parte dallo 0) e si ferma al carattere numero 9 (abbiamo inserito il 10 come "blocco")
# il *3 indica per quante volte viene moltiplicata la funzione o in questo caso, la parte di funzione che scegliamo
