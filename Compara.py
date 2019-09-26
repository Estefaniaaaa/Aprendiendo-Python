# Compara.py
# Autor: Eilen Estefania Esquivel Camacho
# Fecha de creación: 16/09/2019

# Una variable es un nombre que se refiere a un valor.
numero1=input("Número 1:")
numero2=input("Número 2:")
salida="Números proporcionados: {} y {}. {}."

# La estructura de control if y else permite que un programa ejecute unas instrucciones 
# cuando se cumple una condición y 
# otras instrucciones cuando no se cumple esa condición.
if (numero1==numero2):
    # Entra aquí si los números capturados son iguales.
   print(salida.format(numero1, numero2, "Los números son iguales"))
else:
    # Condicionales anidadas,if dentro de otro if.
    # Si los números no son iguales.
    if numero1>numero2:
       # Reporta si el primer númeroes mayor al segundo.
else:
    # O de lo contrario, si el primero no es mayor al segundo.
    print(salida.format(numero1, numero2,"El mayor es el segundo".))   
# El tipo de una variable es el tipo del valor al que se refiere.
