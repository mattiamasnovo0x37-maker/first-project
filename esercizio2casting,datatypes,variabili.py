# Esercizio1
nome = "Mattia"
età = 22
città = "Bolzano"
print(nome, età, città)

#Esercizio2: creare una variabile "X", darle un valore e aggiornarla con un nuovo valore
x = 5
print(x)
x = 10
print(x)

#Esercizio3: creare tre variabili intere + la loro somma
x = 17
y = 37
z = 54
somma = x + y + z
print(int(somma))
print(type(somma))

#Esercizio4: lo scambio di valori
x = 20
y = 15
x,y = y,x
print(x,y)

#Esercizio5: calcolo dell'aria di un rettangolo
base = 5
altezza = 10
area = base * altezza
print("area rettangolo:", area)

#Esercizio6: somma di un numero intero con un decimale
a = 10
b = 3.5
print(a + b)
#print(type(a, b, a + b)) --> versione sbagliata
print(type(a), type(b), type(a + b)) #Giusta, corretta con ChatGPT

#Esercizio7: calcolo della media di tre dati
x, y, z = 10, 40, 30
media = (x + y + z)/3
print("media:", media)

#Esercizio8: concatenazione di stringhe
s1 = "mi piace"
s2 = " giocare a calcio"
s3 = " per fama, soldi e figa"
print(s1 + s2 + s3)

#Esercizio9: ripetizione di tre stringhe
print("ciao " *3)

#Esercizio10: usare i boolean per verificare se un numero è maggiore di un altro
a =  15
b = 30
c = 45
print(a < b)
print(b > c)
print(a < c)
