"""
    file: practica1.py
    autor: @davidpillco
"""
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

valor_par = lambda x: x % 2 == 0
        
print(list(map(valor_par, lista)))

