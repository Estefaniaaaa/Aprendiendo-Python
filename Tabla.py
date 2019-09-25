# Tabla.py
# Autor: Eilen Estefania Esquivel Camacho
# Fecha de creación: 16/09/2019

# La función input() permite obtener texto escrito por teclado. 
# Al llegar a la función, 
# el programa se detiene esperando que se escriba algo y se pulse la tecla Intro.

# Convertir a entero la funcion int () a un número.
# Es una combinación de tipos datos.
numero=input("Dame un numero del ) al 9: ")
numero=int(numero)
# for ejecuta un bloque de código un número determinado
# de veces, cuando se pide que recorra un rango de 
# valores. El segundo parámetro de range no se incluye
# en la serie de valores. Aquí sería del 1 al 10.
for i in range(1,11):
    # i va variando a cada iteración.
    salida="{} x{} = {}"
    print(salida.format(numero,i,i*numero))
