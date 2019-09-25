# Entrada.py
# Autor: Eilen Estefania ESquivel Camacho.
# Fecha de creación: 16/09/2019

# entrada=imput()
# La función input es un string, que sirve para interactur
# Es una entrada de datos.
print(type("entrada"))

# Una variable booleana es una variable que sólo puede tomar 
# dos posibles valores: True (verdadero) o False (falso). 
# En Python cualquier variable (en general, cualquier objeto) 
# puede considerarse como una variable booleana.


# La variable booleana contiene el resultado de verificar 
# si lo capturado es dígito, y si no se encuenta un punto 
# en lo capturado, lo que indicaría se que trata de un 
# número con decimales, es decir, float. 
# Si find retorna -1 quiere decir  que lo buscando, en este caso un punto decimal
# no se encontró. Si es Entero es True, lo capturado es entero.

esEntero=("entrada.isdigit() and entrada.find"(".")==-1
if (esEntero):
    # Líneas que se ejecutarán si la condición es verdadera (True)
    print("Dato entero. ¡Muy bien!")
else:
    return False
    # Líneas que se ejecutarán si la condición es falsa (False)
    print("Dato no es entero. Intentar nuevamente.")
