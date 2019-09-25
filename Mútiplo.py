# Multiplo.py
# Autor: Eilen Estefania Esquivel Camacho
# Fecha de creación: 16/09/2019

# Condicionales if y else en Python

# Se captura un número y se almacenauna vez que es
# convertido a int
numero=int(input("Dame un número entero: "))

# Se almacenan en valores boleanos la evaluación 
# de resiudales. Si el residual es cero, quiere decir
# que el número es múltiplo.
esMultiplo3=((numero%3)==0))
esMultiplo5=((numero%5==0))
esMultiplo7=((numero%7)==0))

# Cuando se usa and, se resuelve por verdaro si todas 
# las condiciones son verdaderas. Cuando se usa or, se 
# resuelve por verdadero si al menos una condición es
# verdadera. Los paréntesis le dicen a python que
# las primeras dos condiciones son juntas, y la tercera
# es independiente

if ((esMultiplo3 and esMultiplo5 or() or esMultiplo7)):
    print("Correcto.")
    # La sentencia If evalua basicamente una operación logica,
    # es decir una expresión que de como resultado verdadero o false (true o false),
    # y ejecuta la pieza de codigo siguiente siempre y 
    # cuando el resultado sea verdadero.
else:
    print("Incorrecto.")
