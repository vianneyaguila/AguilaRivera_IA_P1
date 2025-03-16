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

nombre = input("Agrega el nombre de la flor: ")
if nombre == "Spathiphyllum":
 print(" Sí -¡Spatiphyllum es la mejor flor!")
elif nombre == "spathiphyllum":
   print("No, quiero una Spathiphyllu grande")
else:
   print("Spathiphyllum! No", nombre + "!") 

#Fundamentos de instrucción if-else
income = float(input("Enter de annual income: "))
if income < 85528:
   tax = income * 0.18 -556.02
tax = round(tax, 0)
print("The tax is: ", tax, "thalers1" )

# Fundamentos de la declaración de if-elif-else
year = int(input("Enter a year: "))
if year < 1582:
   print("Not within the Gregorian calendar period")
else:
   if year % 4 !=0:
      print("Common Year")
   elif year % 100 != 0:
      print("Leap year")
   elif year % 400 != 0:
      print("Common year")
   else:
      print("Leap yaer")