"""
    file: practica5.py
    autor: @davidpillco
"""
import math
lista = [(10,2), (8,7), (5,4), (3,11), (10,11)]

raiz = lambda x: x[0]
potencia = lambda x: x[1]

funciones = lambda x: (math.sqrt(raiz(x)), potencia(x)**2)

print(list(map(funciones, lista)))


