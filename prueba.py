# Lista de entradas
entradas = ["8", "ac", "tle", "radar", "racecar", "php", "atcoder", "codeforces", "steam"]

# Itera a través de cada entrada en la lista
for cadena in entradas:
    # Verifica si la cadena es palíndroma utilizando slicing
    if cadena == cadena[::-1]:
        print("YES")
    else:
        print("NO")
