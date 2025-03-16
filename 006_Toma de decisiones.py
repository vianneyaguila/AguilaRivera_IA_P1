# Comparación de igualdad de operadores, (=)-> es un operador de asignación, mientras que (==) -> hace referencia a comparación.
print("Igualdad: el operador igual a (==)")
var = 0
print (var == 0)
var = 1
print (var == 0)

# (!=) -> este operrador hace referencia a "distitno de", también para comparar los valore de dos operandos.
print("Desigualdad: el operador disitnto de (!=)")
var1 = 0
print(var1 != 0)
var1 = 1
print(var1 !=0)

# Variables de LAB: preguntas y respuestas
print("Variables de LAB: preguntas y ejecución condicional")
n = int( input("Ingresa cualquier número: "))
print ( n >= 100 )

#Analisis de ejemplos de códigos
Num1 = int(input("Añada el primer número: "))
Num2 = int(input("Añada el segundo número: "))
Num3 = int(input("Añada el tercer número: "))
Numero_mayor = Num1
if Num2 > Numero_mayor:
    Numero_mayor = Num2
if Num3 > Numero_mayor:
    Numero_mayor = Num3
print("El número mayor es: ", Numero_mayor)

