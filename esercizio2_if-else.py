# Verifica se un numero è multiplo di 3.
n = 9
if n % 3 == 0:
    print("Il numero inserito è multiplo di tre ")
else:
    print("Il numero inserito non è multiplo di tre ")

# Verifica il voto che è stato inserito raggiunge la sufficienza.
voto = 22
if voto >= 18:
    print("Il voto è sufficiente, ESAME SUPERATO")
else:
    print("Il voto non è sufficiente, BOCCIATO")

# Controlla se un carattere è una vocale oppure una consonante.
c = "a"
if c in "aeiou":
    print("vocale")
else:
    print("consonante")

# Verifica se un numero è positivo, negativo oppure uguale a 0:
n = 0
if n > 0:
    print("positivo")
elif n < 0:
    print("negativo")
else:
    print("uguale a zero")

# Verifica il maggiore di tre numeri.
a, b, c = 7, 3, 9
if a >= b and a >= c:
    print("A è il maggiore dei tre numeri")
elif a <= b and b >= c:
    print("B è il maggiore dei tre numeri")
else:
    print("C è il maggiore dei tre numeri")

# Calcola il prezzo di un biglietto.
età = 70
if età < 12:
    prezzo = 5
elif età < 65:
    prezzo = 10
else:
    prezzo = 7
print("Prezzo biglietto è: ", prezzo, "€")

# Classificazione di un triangolo.
a, b, c = 5, 5, 3
if a == b == c:
    print("Il triangolo è equilatero")
elif a == b or b == c or a == c:
    print("Il triangolo è isoscele")
else:
    print("Il tiangolo è scaleno")
# È stata messa la variaile "a == b or b == c or a == c" perché if:
# 1. Verifica prima se "a == b == c" è True o False (ricordiamoci che python parte dall'alto con la verifica).
# 2. Se nota che è falsa, passa a verificare se "a == b or b == c or a == c" è True o False.
# 3. In alternativa se anche nella seconda non trova riscontro, finisce per stampare la terza.
# I vari triangolo sono stati messi in questo determinato ordine per non creare troppe variabili e rendere tutto più compatto.

