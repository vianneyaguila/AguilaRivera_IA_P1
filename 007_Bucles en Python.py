# Bucle infinito -> secuencia de instrucciones en un programa que se repiten indefinidamente.
# Ejemplo
#while True:
#print("I'm stuck inside a loop ")

# Ejemplo para hallar el número más grande de un conjunto grande de datos ingresadps , este se encuntra en el apartado 3.2.3
#larguest_num = -999999999
#number =int(input("Enter a number or type -1 tu stop: "))
#while number != -1:
#       larguest_num = number
#number = int(input("Enter a number or type -1 to stop: "))
#print("The largest number is: ", larguest_num)

# Ejemplo 3.2.3 
# Se trata de un programa que lee una secuencia de números 

#num_impares = 0
#num_par = 0
#num = int(input("Ingrese un número o escriba 0 para detener: "))
#while num != 0:
#    if num % 2 == 1:
#        num_impares += 1
#    else:
#        num_par += 1
#        num = int(input("Ingresa un número o ecriba 0 para detener: "))
#    print("Los números impares: ", num_impares)
#    print("Los números pares: ", num_par)

# Usar una variable de contador para salir de un bucle, ejemplo:
#contador = 5
#while contador != 0:
#    print("Dentro del bucle.", contador)
#    contador -= 1
#    print("Fuera del bucle." , contador) 

# Adivina el número secreto
num_sec = 777
print("""
+================================+
| Bienvenido a mi juego, muggle! |
| Introduzca un número entero    |
| ¿Y adivina que número tengo?   |
| Entonces, ¿cuál es número?     |
+================================+
""")
while True:
    num_us = int(input("Ingresa un número: "))

    if num_us == num_sec:
        print("¡Bien hecho, muggle! Ahora eres libre")
        break
    else: 
       print("Ja, ja! ¡Estas atrapado en mi circulo!")

#Repetir su código con for
i = 0
while i < 100:
    i += 1

for i in range(100):
    pass
for i in range(10):
    print("El valor de i es actualmente", i)

# El rango de invocación puede estar equipada con dos argumentos, no solamente con uno
#Ejemplo
for i in range(2 , 8):
    print("El valor de i actualmente es: ", i)

for i in range( 2, 8, 3):
    print("El valor de i actualmente es: ", i)
    # el tercer arguemnto es un incremento: se trata de un valor agregado

for i in range(1 , 1):
    print("El valor de i actualmente es: ", i)
    # El valor generado por el rango debe ordenarse en orden ascendente. 

# Ejemplo que realiza algunas potencias 
pot = 1
for expo in range(16):
    print("2 to the power of", expo "is", pot)
    pot *= 2

import time
for i in range(1 , 6):
    print(f"{i} Mississippi")
    time.sleep(1)
print("Ready or nor, here I come!")

print("The brake intruction: ")
for i in range(1 , 6):
    if i == 3:
        break
    print("Inside the loop.", i )
    print("Outside the loop.")
    print("\n La instrucción de continuar: ")
    for i in range(1 , 6):
        if i == 3:
            continue
        print("Inside the loop", i)
        print("Outside the loop.")

largest_num = -99999999
counter = 0
while True:
    number = int(input("Enter a number or type -1 to end the program: "))
    if number == -1: 
        break
    counter += 1
    if number > largest_num:
        largest_num = number

    if counter != 0:
        print("The largest number is", largest_num)
    else:
        print("You haven't entered any number.")

