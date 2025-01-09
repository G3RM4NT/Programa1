'''
print ("Hola mundo")
print ("Hola mundo soy german")
print ("Esto es una suma")
numero_uno = 5
numero_dos = 5
resultado= numero_uno + numero_dos
print (resultado)


#Asignación
mensaje = "Hola"
mensaje += " "
mensaje += "German"
print (mensaje)



#Concatenación
mensaje2 ="Hola"
espacio= " "
nombre="Germancillo"
print(mensaje2+espacio+nombre)

#Concatenación de numeros y texto
numero_uno = 5
numero_dos = 6
resultado1= numero_uno + numero_dos

resultado1 = str(resultado1)

print ("El resultado de la suma es: " + resultado1)

#Busqueda
mensaje3 = "Que pasa hermano"
buscar_subcadena=mensaje3.find("hermano")
print(buscar_subcadena)

#Extraccion
mensaje = "Hola blanca"
extraer=mensaje[0:4]
print (extraer)


#Comparación
mensaje11 = "fortnite"
mensaje22 = "fortnite"
print (mensaje11 == mensaje22 )

#Palabras reservadas
#No ocupar palabras del lenguaje para variables

#Operadores aritmeticos

#Tipos de datos en python

#Entero
numero = 15
print (numero, type(numero))


#Flotante
numero_flotante = 15.5
print (numero_flotante, type(numero_flotante))


#numero complejo
numero_complejo = 5 + 6j
print (numero_complejo, type(numero_complejo))


#tipo de dato string
nombre = "German"  
print (nombre, type(nombre))


#tipo de dato booleano
verdadero_falso = 3 ==3 
print (verdadero_falso, type(verdadero_falso))

#Entrada de datos
palabra = input ("Introduce una palabra:")
num_int = int(input("introduce un numero entero:"))
numero_flotante  = float(input("introduce un numero flotante:"))
print (palabra )
print (num_int )
print (numero_flotante )

#Suma con entrada de datos

Nombre = input ("Introduce tu nombre:")
print("Hola "   +  nombre  + ",  vamos a realizar una suma.")
Num1 = int(input("Introduce el primer numero: "))
Num2 = int(input("Introduce el segundo numero: "))
Res = Num1 + Num2
print("El resultado de la suma es: ", Res )
 
 '''
 
 #Sentencias condicionales simples
'''num_uno = 5
if num_uno ==5:
    print ("El numero es cinco")
    print("Fin")
'''
'''

print ("Sistema para calcular promedio de un alumno.")
nombre = input (" Para comenzar, ¿Cual es tu nombre? ")
matematicas = int(input(nombre +  " ¿Cual es tu calificacion en matematicas?: "))
quimica = int(input(nombre +  " ¿Cual es tu calificacion en quimica?: "))
biologia = int(input(nombre +  " ¿Cual es tu calificacion en biologia?: "))
promedio = (matematicas + quimica + biologia ) /3
promedio = int(promedio)
if promedio >= 6:
     print('Felicidades ' +nombre +  ' "APROBASTE" con un promedio de:  ' , promedio)



print("Fin.")


'''


'''
#Sentencias compuestas clase 11
num_unoo = 8
if num_unoo == 5:
    print ("El numero es cinco")
else:
    print ("El numero NO es cinco")
print("Fin.")

'''


'''

print ("Sistema para calcular promedio de un alumno.")
nombre = input (" Para comenzar, ¿Cual es tu nombre? ")
matematicas = int(input(nombre +  " ¿Cual es tu calificacion en matematicas?: "))
quimica = int(input(nombre +  " ¿Cual es tu calificacion en quimica?: "))
biologia = int(input(nombre +  " ¿Cual es tu calificacion en biologia?: "))
promedio = (matematicas + quimica + biologia ) /3
promedio = int(promedio)
if promedio >= 6:
     print('Felicidades ' +nombre +  ' "APROBASTE" con un promedio de:  ' , promedio)

else: 
    print('Felicidades ' + nombre +  ' Eres un maldito fracasado tuvistes: ' , promedio  )
    


print("Fin.")

'''


#Sentencias condicionales multiples clase 12

'''
num_prin = 3
if num_prin ==1:
    print("El número es UNO.")
elif num_prin==2:    print("El número es DOS")
else:
      print  ("El numero se desconoce")

'''

'''
print ("Convertidor de numeros a letras")

numero= int(  input ("Cual es el numero que deseas convertir?  "))
if numero ==1:
    print("El numero es uno")
elif numero ==2:
    print ("El numero es dos")
   
elif numero ==3:
    print ("El numero es tres")

elif numero ==4:
    print ("El numero es cuatro")

elif numero ==5:
    print ("El numero es cinco")

elif numero ==6:
    print ("El numero es seis")
else: print ("El programa solo puede convertir hasta numero 6")

print ("Fin")
'''
#Desafio conversor clase 13

''' 
print("=================")
print ("Conversor")
print("=================\n" )

print("Menu de opciones \n")
print ("Presiona 1 para convertir de número a palabra")
print ("Presiona 2 para convertir de palabra a número\n")

opcion = int (input ("¿Cual es tu opción deseada: "))

if opcion ==1:
    print("\n Conversor de numero a palabra\n")
    opcion_uno = int (input("¿Cual es el numero que deseas convertir a plabra?: "))
    if opcion_uno ==1:
        print("El numero es 'UNO'")
    elif opcion_uno ==2:
        print("El numero es 'DOS'")
    elif opcion_uno ==3:
        print("El numero es 'TRES'")
    elif opcion_uno ==4:
        print("El numero es 'CUATRO'")
    elif opcion_uno ==5:
        print("El numero es 'CINCO'")
    else:
        print("El numero seleccionado no esta regisrado")



elif opcion ==2:
    print("\n Conversor de palabra a numero\n")

    opcion_dos = input ("¿Cual es la palabra que desea convertir a numero?: ")
    opcion_dos = opcion_dos.lower()
    if opcion_dos == "uno":
        print("El numero es '1'")
    elif opcion_dos =="dos":
        print("El numero es '2'")
    elif opcion_dos =="tres":
        print("El numero es '3'")
    elif opcion_dos =="cuatro":
        print("El numero es '4'")
    elif opcion_dos =="cinco":
        print("El numero es '5'")

    else: print ("El numero seleccionado no esta registrado")




else:
    print("Opcion no disponible.")

print("FIN.")

  '''

  #Clase 14 operadores relacionales

print ("Introduce 2 numeros a comparar: \n ")
num_uno = int(input("Introduce el primer numero:  ")) 
num_dos = int(input("Introduce el segundo numero:  "))

print("\n Los numeros a comparar son: ", num_uno, " y ", num_dos,  )
     
     
     
  

            

    