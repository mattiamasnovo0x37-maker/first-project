# Prova a scrivere un programma utilizzando il ciclo while che:
# 1. Chiede all'utente di inserire un numero positivo;
# 2. Continua a chiederlo finché l'utente non inserisce un numero positivo (>0);
# 3. Quando il numero è positivo, stampa: "Hai inserito il numero positivo: x";
# 4. Fai terminare il tutto;

# 1. Primo input (chiede all’utente un numero e lo converte in intero).
numero = int(input("Inserisci un numero positivo (numero > 0 per uscire): "))

# 2. Continua finché il numero NON è positivo.
while numero <= 0: #ripeti finché il numero è zero o negativo.
    print("Numero non valido, riprova.")
    numero = int(input("Inserisci un numero positivo (numero > 0 per uscire): "))
# Finché il numero non è positivo: mostra il messaggio di errore e richiede un nuovo numero.

# 3. Qui sei uscito dal while: il numero è sicuramente > 0.
print(f"Hai inserito il numero positivo: {numero}")
# Quando l’utente inserisce finalmente un numero > 0, il ciclo termina.
# Il programma stampa: "Hai inserito il numero positivo: x".

# Esercizio 1: Conta da 1 a 5.
i = 1 
while i <= 5:
    print(i)
    i += 1

# Esercizio 2: Conta i numeri pari da 2 a 10.
i = 2
while i <= 10:
    print(i)
    i += 2

# Esercizio 3: Somma i numeri da 1 a 10.
i = 1
somma = 0
while i <= 10:
    somma += i
    i += 1
    print("somma =", somma)

# Esercizio 4: Stampa la tabellina di un numero.
n = 7
i = 1
while i <= 10:
    print(f"{n} x {i} = {n*i}")
    i += 1

# Esercizio 5: Calcola la somma dei numeri inseriti dall'utente finché non digita il numero 0.
somma = 0
n = int(input("Inserisci un numero (0 per uscire): "))
while n != 0:
    somma += n
    n = int(input("Inserisci un numero (0 per uscire): "))
print("somma totale. ", somma)
#Quando viene riconosciuto che il numero inserito dall'utente è uguale a 0, il ciclo termina e da come risultato la somma dei numeri inseriti in precedenza.

# Esercizio 6: Indovina il numero
segreto = 7
tentativo = int(input("Indovina il numero: "))
while tentativo != segreto:
    tentativo = int(input("Sbagliato! riprova... "))
    print("Hai indovinato!")

# Esercizio 7: Stampa solo numeri dispari fino a 15.
i = 1
while i <= 15:
    print(i)
    i += 2

# Esercizio bonus: calcola la somma delle cifre di un numero.
n = 37541
somma = 0
numero = n          # salvo il numero in una variabile di lavoro

while numero > 0:
    cifra = numero % 10      # prendo l'ultima cifra
    somma = somma + cifra    # la aggiungo alla somma
    numero = numero // 10    # tolgo l'ultima cifra

print("La somma delle cifre di", n, "è:", somma)
# Spiegazione dell'esercizio "somma delle cifre di un numero":
# 1. Parto da un numero n (es. 37541) e imposto somma = 0.
# 2. Copio n in una variabile di lavoro chiamata "numero".
# 3. Finché numero > 0 (ciclo while):
#    - prendo l'ultima cifra con: cifra = numero % 10
#    - aggiungo la cifra alla somma: somma = somma + cifra
#    - tolgo l'ultima cifra dal numero con: numero = numero // 10
# 4. Quando numero diventa 0, il ciclo termina e "somma" contiene
#    la somma di tutte le cifre del numero di partenza.
#    (Per 37541 → 3 + 7 + 5 + 4 + 1 = 20)