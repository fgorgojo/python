import numpy as np

# 1. Crear un array
# np.array() convierte una lista de Python en un array de NumPy
precios = np.array([10.5, 12.0, 11.2, 13.8])
print(f"Array de precios: {precios}")
var = "HFDSAFD"
print(f"variable ${var}")

x1, y1 = None, None
def funcion(x,y):
    global x1, y1
    if x==x1 and y==y1:
        print("Usando valor en cache")
        return x1+y1
    else:
        print("Calculando nuevo valor")
        x1, y1 = x, y
        return x + y    

print(funcion(3,4))
print(funcion(3,4))
print(funcion(5,6)) 

def f1(*args):
    print("Funcion f1",type(args))
    
print(f1(3,3,4,5,6))

a=8
l = [1,2,3]
aa=3
def fun(a :int ,b : list[int]) -> int:
    b.append(7)
    a=2
    return a+1

print(fun(aa,l))
print("FICHEROS")

# with open("resources/pru.txt","r") as f:
#     contenido = f.read()
#     print(contenido)  
from pathlib import Path
print(Path('resources/pru.txt').read_text())  