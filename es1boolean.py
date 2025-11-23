#Esercizio 1: verificare se un numero è positivo
x = 10
risultato = x > 0
print(risultato) #True perché x che equivale a 10 è > di 0.

# Esercizio 2: verifica se due stringhe sono uguali.
s1 = "ciao mondo"
s2 = "ciao mondo"
print (s1 == s2) #True perché i valori sono uguali.
#se ci fosse stato anche solo uno spazio in più, il risultato sarebbe stato False.

# Esercizio 3: verificare se due numeri (A e B) sono positivi
a = 5
b = 10
risultato = (a > 0) and (b > 0)
print(risultato) #True perché entrambi i valori sono > di 0

#Esercizio 1 fatto da solo:
#1. Scrivi un programma che chieda all'utente la sua età e se ha la patente (sì/no).
#2. Il programma deve stampare True se la persona può guidare (età maggiore o uguale a 18 e ha la patente).
#3. Deve stampare False in tutti gli altri casi.
età = int(input("Quanti anni hai? "))                   #età prende il numero (convertito in int).
patente = input("Hai la patente? (si/no) ")             #patente prende la risposta sì/no.

puo_guidare = (età >= 18) and (patente.lower() == "si") #puo_guidare è True solo se eta ≥ 18 e ha risposto "si".
print(puo_guidare)

#Esercizi 2 fatto da solo:
#Un utente può entrare in biblioteca se:
#1. non è in ritardo con la restituzione di libri oppure
#2. ha un abbonamento premium.
#Scrivi un programma che, date due variabili booleane (ritardo e premium), stampi True se l'utente può entrare, altrimenti: False

# Chiedo i dati all'utente
ritardo_input = input("Sei in ritardo con la restituzione? (si/no) ").strip().lower() 
premium_input = input("Hai un abbonamento premium? (si/no) ").strip().lower()
#.strip() --> va a togliere gli spazi iniziali e finali.
#.lower() --> converte tutto in minuscolo.

# Converto le risposte in variabili booleane
# in_ritardo = True se ha risposto "si", False altrimenti
in_ritardo = (ritardo_input == "si")
premium = (premium_input == "si")

# Regola di accesso:
# può entrare se NON è in ritardo oppure se ha premium
accesso_utente = (not in_ritardo) or premium

print(accesso_utente)
