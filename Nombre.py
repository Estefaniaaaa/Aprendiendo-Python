# Nombre.py
# Autor: Eien Estefania Esquivel Camacho
# Fecha de creación: 16/09/2019

# La función input() permite obtener texto escrito por teclado.
# Al llegar a la función, el programa se detiene esperando que se escriba algo y 
# se pulse la tecla Intro.

nombre=input("Nombre:")
apellidos=input ("Apellidos:")


# Se concatean los valores str, junto con la libertad " "
nombreCompleto=nombre+" "+apellidos

# Se asigna a la variable la representación en mayúsculas
#de lo que contenía.
nombreCompleto.upper()
print(nombreCompleto)
