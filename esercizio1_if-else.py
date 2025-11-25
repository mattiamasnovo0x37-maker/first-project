# Verifica se un numero è oisitivo o negativo
x = -10
if x >= 0:
    print("Positivo")
else:
    print("Negativo")

# Verifica quale dei due numeri è quello maggiore
a = 10
b = 7
if a>b:
    print("a è maggiore di b")
else:
    print("b è maggiore di a")

# Controllare se una persona è maggiorenne o no
età = 20
if età >= 18:
    print("sei maggiorenne")
else:
    print("sei minorenne")

# Esercizi da svolgere in autonomia
# 1. Scrivi un programma che:
# • Ha una variabile eta.
# • Se eta < 18 stampa "Sei minorenne".
# • Se eta è almeno 18 ma meno di 65 stampa "Sei adulto".
# • Altrimenti stampa "Sei anziano".

età = 68
if età < 18:
    print("Sei minorenne")
elif età >= 18 and età < 65:
    print("Sei adulto")
else:
    print("Sei anziano")
