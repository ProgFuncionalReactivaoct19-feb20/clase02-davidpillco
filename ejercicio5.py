"""
    file: ejemplo5.py
    autor: @davidpillco
"""
datos = (
        (100, 170),
        (200, 180)
)


def anios(x): return x[0]
def estatura(x): return x[1]

def funciones(x): return (anios(x)/12.0, estatura(x)/100)

print(list(map(funciones, datos)))
