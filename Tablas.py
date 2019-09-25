# Tablas.py
# Autor: Eilen Estefania Esquivel Camacho
# Fecha de creación: 16/09/2019

# El for de Pyton itera sobre los items
# de cualquier secuencia (una lista o una cade textos)
# en el orden que aparece la secuencia.

for i in range (1,11):
    encabezado="Tabla del {}"
    print(encabezado,format (i))
    # print sin argumentos es un salto a la línea.
    # Si la lista está vacía, el for no se ejecuta ninguna vez.
    print()
    # Dentro de un for, se pone otro for.
    for j in range (1,11):
        # Aquí, i contiene el numero base de la tabla 
        # y j el elemento de la tabla.
        salida="{} x {}= {}"
        print (salida,format(i,j,i*j))

    else:
        # Al concluir con las iteraciones indicadas
        # se ejecuta este código, que es un salto de
        # línea.
        print()
# For se puede utilizar con cualquier objeto con el que se pueda iterar,
# (ir saltando de elemento en elemento).
