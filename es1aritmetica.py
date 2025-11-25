# Dati due numeri a = 15 e b = 4, calcolare: somma, differenza, prodotto e divisione.
a = 15
b = 4
print("somma :", a + b)
print("differenza :", a - b)
print("prodotto :", a * b)
print("divisione :", a / b)
print("divisione senza decimale :", a // b)
print("modulo :", a % b)

# Utilizzare la libreria Math per svolgere operazioni più complesse.
import math
x = 8.7
print("floor :", math.floor(x)) # va sempre verso il basso, puntando verso la prima cifra intera più vicina allo 0.
print("ceil :", math.ceil(x)) # va sempre verso l'alto, puntando verso la prima cifra intera più lontana dallo 0.
print("trunc :", math.trunc(x)) # elimina la parte decimale senza considerare il segno.
print("fabs :", math.fabs(x)) # da indietro il valore assoluto ignorando il segno, non lo prende in considerazione.

# Esercizi da svolgere da solo:
# 1. Chiede all'utente quanti euro ha.
# 2. Chiede il prezzo di un singolo oggetto.
# 3. Usa // per calcolare quante unità può comprare.
# 4. Usa % per calcolare quanti euro restano

# Esercizio 1:
euro = float(input("Quanti euro hai? "))

# Esercizio 2:
prezzo = float(input("quanto costa un singolo oggetto? "))
print("Ho", euro, "euro")
print("Il prezzo di un dingolo oggetto è: ", prezzo, "euro")

# Esercizio 3
prezzo_biscotti = 1.99
contanti_disponibili = 32
print(contanti_disponibili // prezzo_biscotti)

# Esercizio 4
soldi = 32
costo = 1.99
print("In tutto rimarranno: ", soldi % costo, "euro")
