# Consegna1: Chieda all'utente di inserire un numero intero (esempio dove ho sbagliato)
input("Inserisci un numero intero ") #scritto così non è una varoabile, non c'è x = "Y"
print(input)

# Esempio scritto corretto
numero = int(input("inserisci un numero intero: ")) #così c'è una funzione
print(numero)

# Step in più suggerito da ChatGPT: chiedi un numero all'utente / stampa il doppio e il tipo di valore
numero = int(input("inserisci un numero: "))
doppio = numero * 2 
print("Il doppio è:", doppio, "e il tipo è:", type(doppio)) # ho sbagliato perché non ho messo la virgola (,) dopo "e il doppio è:". è uno sbaglio perché ha la funzione di separatore (1, 2, 3,...)

#Consegna2: Converta questo numero in numero decimale (float) e lo stampi
num_int = 10
num_float = float(num_int)
print(num_float)

# Consiglio di ChatGPT per far risaltare di più il funzionamento del casting
num_int = 10
num_float = float(num_int)
print(num_float, type(num_float))

#Consegna3: Converta lo stesso numero in stringa e lo stampi insieme a un messaggio
# Metto tutto sotto parentesi perché senno mi da errore e mi blocca il terminale.
#n1_float = 37.54
#n1_str = str(n1_float)
#prin...(n1_str with "questo è il mio numero preferito") #ho sbagliato perché "with" non ha nessuna funzione in python


#Esercizio corretto da Chatgpt
#Esempio1
n1_float = 37.54
n1_str = str(n1_float)
print(n1_str, "questo è il mio numero preferito")

#Esempio2
n1_float = 37.54
n1_str = str(n1_float)
print(f"{n1_str} questo è il mio numero preferito") #la f sta per: "formatted string" (o f-string) -->
# --> Vuol dire: “questa stringa contiene dentro le parentesi graffe {} delle espressioni Python da valutare e sostituire nel testo”.
