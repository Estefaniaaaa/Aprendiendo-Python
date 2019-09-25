# Conversiones.py
# Autor: Eilen Estefania Esquivel Camacho
# Fecha de creación: 16/09/2019

# Se declara una variable str, con una cadana de dígitos 
# Los tipos de datos numéricos almacenan valores numéricos

numero="1234"

# Se muestra el tipo que tiene la variable. La salida de type()
# no es un str, es un dato type.
# type()función para saber a qué clase pertenece una variable o un valor 
print(type(numero))

# Se convierte la cadena a su equivalencia int.
numero=int(numero)

# Se muestra cómo el tipo ha cambiado, aunque sea la misma 
# variable

print(type(numero))

# Se declara un str con meta sustitución (posiciones donde irán
# Valores proporcionados usando format.

salida="El numero utilizado es{}"

# Se muestra el resultado. La meta sustitución hará que donde está 
# {} se coloque el valor de numero.
# los números complejos se incluyen en la categoría de números de Python.
print(salida.format(numero))
