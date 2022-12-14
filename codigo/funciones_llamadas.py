"""
Funciones en Python. Distintas formas de llamar a una función
"""
path="/home"

def sumar(a,b): 
    global path
    path="hola"
    return a + b

def sumaResta(a,b):
    return a + b, a - b

if __name__ == '__main__':
    s,r = sumaResta(1,3)
    print('suma: ', s, 'resta: ', r)
   
    # 1) Posicional:
    print(sumar(1,2))

    # 2) Nominal:
    print(sumar(b=2, a=1))

    # 3) Tupla:
    t = (1,2)
    print(sumar(t[0],t[1])) # en otros lenguajes
    print(sumar(*t)) # Expandimos la tupla
    L = [1,2]
    print(sumar(*L))
    c = {1,2}
    print(sumar(*c))

    # 4) Con dict:
    d = {"a":1, "b":2}
    print(sumar(**d)) # Expandimos el dict

    L = [(1,3),(4,5),(8,8),(9,0),(6,7)]
    # Obtener una lista con las sumas de los elementos de las tuplas
    # utilizando la función sumar.
    L2 = []
    for t in L:
        L2.append(sumar(*t))
    print(L)
    print(L2)

