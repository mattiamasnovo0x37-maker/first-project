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
