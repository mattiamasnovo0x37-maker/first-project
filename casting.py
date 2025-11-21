# Esercizio 1: convertire un dato in float
n_int = 10

n_float = float(n_int)

print(n_int, n_float)

# Esercizio 2: partendo da un float e convertirlo in un intero
n_float = 9.7

n_int = int(n_float)
print(n_int)

# Esercizio 3: partendo da una stringa e convertirla in un dato intero
n_str = "123"
n_int = int(n_str)
print(n_int)

# Esercizio 4: partendo da una stringa e convertendola in un float
num_str = "3.14"
num_float = float(num_str)
print(num_float)

# Esercizio 5 (di testa mia): parto da un float e lo trasformo in una stringa
num1_float = 3.144
num2_str = str(num1_float)
print(num2_str)

# Esempio di errore di Casting
n_str = "ciao"
try:
    num_int = int(n_str)
except ValueError:
    print("non puoi convertirte 'ciao' in intero")
    
