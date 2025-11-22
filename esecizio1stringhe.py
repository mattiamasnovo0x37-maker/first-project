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