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
        print("¡"
        ""
        ""
        "Bien hecho, muggle! Ahora eres libre")
        break
    else: 
    print("Ja, ja! ¡Estas atrapado en mi circulo!")




