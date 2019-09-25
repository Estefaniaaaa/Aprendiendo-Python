# Acumulado.py
# Autor: Eilen Estefania Esquivel Camacho

# Se declaran las variables de trabajo, con tipo explícito.
# Los números enteros (llamados int).
acumulado=int(0)
numero=str("")

# Al colocar True como condición while, se reforma un
# ciclo infinito que no se romperá hasta que de forma
# explícita se utilice la instrucción break.
# While que nos permite ejecutar ciclos, o bien secuencias periódicas que nos 
# permiten ejecutar código múltiples veces.

# while nos permite realizar múltiples iteraciones basándonos en el resultado 
# de una expresión lógica que puede tener como resultado un valor True o False.
while True:
     numero=input("Dame un número entero: ")
     if numero=="":
        # Si el número es vacío reporta la situación y sale.
        print("Vacío. Salida del programa.")
        break
else:
        # Si se proporcionó valor, acumulado =acumulado + numero
        # Se realiza el cálculo usando suma incluyente (+=)
    acumulado+=int(numero) 
    salida="Monto acumulado: {}"
    print(salida.format(acumulado))

# Cuando el resultado es False
# Un ejemplo seria un contador con un valor inicial de cero,
# cada iteración del while manipula
# esta variable de manera que incremente su valor en 1, 
# por lo que después de su primera iteración el contador tendrá 
# un valor de 1, luego 2, y así sucesivamente.
# Eventualmente cuando el contador llegue a tener un valor de 10,
# la condición del ciclo numero <= 10 sera False, por lo que el ciclo
# terminará arrojando el siguiente resultado.
