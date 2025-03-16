#La función input() con un argumento 
#print("Tell me anything...")
#anything = input
#print ("Hmm..." , anything, "...Really?")

# El resultado de la función input()
#anything1 = input("Tell me anything")
#print("Hmm...", anything1, "...Really?")

#Conversión de tipos
#Cualquier_cosa = float( input ("Ingrese un número:"))
#algo = Cualquier_cosa ** 2
#print(Cualquier_cosa, "Elevdo a la potencia de 2 es:", algo) 

#Ejemplo del curso sobre como calcular la longitud de una hipotenusa
#leg_a = float( input ( "Ingrese la longitud del primer tramo: "))
#leg_b = float(input ( "Ingrese la longitud del segundo tramo: "))
#hipotenusa = (leg_a **2 + leg_b**2) ** .5
#print( "La longitud de la hipotenusa es:", hipotenusa) 

# Convertores de tipos una vez más
# Cambio en el ejemplo de como calcular la logitud de una hipotenusa 
#leg1_a = float( input ( "Ingrese la longitud del primer tramo: "))
#leg1_b = float(input ( "Ingrese la longitud del segundo tramo: "))
#print( " La longitud de la hipotenusa es " + str ((leg1_a ** 2 + leg1_b ** 2))) 

##Operadores de cadena
#Name = input( "Puede regalarme su nombre, por favor? ")
#Apellido = input( "Puede regalarme su apellido, por favor? ")
#print(" Gracias ")
#print( " \n Su nombre es " + Name + " " + Apellido + " .")

# Ejemplo de un dibujo de un rectángulo 
#print ("+" + 10 * "-" + "+")
#print (("|" + " " * 10 + "|\n") * 5, end="")
#print ("+" + 10 * "-" + "+") 

# LAB entradas y salidad simples
#a2 = float( input(" Agregue el primer valor: "))
#b2 = float( input(" Agregue el seguno valor: "))
#print ("Suma: ", a2 + b2)
#print ("Resta: ", a2 - b2)
#print ("Multiplicación: ", a2 * b2)
#print ("División: ", a2 / b2)

# Operadores de expresiones LAB
#x1 = float( input("Ingresa el valor:"))
#ry = 1 /( x1 + 1 / ( x1 + 1  / ( x1 + 1 / x1 )))
#print ("El resultado de ry es: ", ry)

# LAB Operadores y Expresiones LAB 2
Hora = int ( input ("Tiempo de inicio en horas: "))
Min = int ( input ( "Tiempo de inicio en minutos: "))
D_evento = int ( input ("Duración del evento: "))

Hora = Hora + Min // 60
Min = Min + D_evento

Min = Min % 60
Hora = Hora % 24
print (Hora, ":", Min, sep="")

