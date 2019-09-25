# Aleatorio.py
# Autor: Eilen Estefania Esquivel Camacho
# Fecha de creación: 16/09/19

# phyton posee muchas librerias listas para utlizarse.
# A dichas librerias les da el nombre de modules (module)
# Para utilizar in modulo en un programa, primero debe 
# Importarse, usando las instrucciones Import.
# La biblioteca random contiene una serie de funciones 
# relacionadas con los valores aleatorios. 
import random

#Se define una variable float, y se le asigna un valor.
numero1=float (10.50)

# En python una función es un conjunto de instrucciones que 
# procesan una tarea específica , como una unidad de ejecución.
# Se declaran con def. Todo el código posicionado a la derecha 
# de la definición, forma parte de la función.
# Una función es un bloque de código con un nombre asociado, 
# que recibe cero o más argumentos como entrada, 
# sigue una secuencia de sentencias, 
# las cuales ejecutan una operación deseada y devuelve un valor 
# y/o realiza una tarea.

def miFunción():
    # Se convierte a float el numero aleatorio generado por
    # random.randrange() (solo está disponible si se importa
    # el módulo random
    numero2=float (random.randrange(1,10))
    # Se utilizan meta sustituciones para mostrar resultados.
    mensaje="La suma de {} y {}"
    print (mensaje.format(numero1,numero2,numero1+numero2))

# Se ejecuta la función definida en el código.
# La función random() genera un número decimal entre 0 y 1 
# (puede generar 0, pero no 1).

# El módulo random permite agragar funcionalidad referente
# al manejo de valores aleatorios
miFunción()
