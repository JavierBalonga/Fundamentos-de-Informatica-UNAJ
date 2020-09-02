def ejercicio1():
    print("Ingrese un numero por favor")
    print("Para ver si es positivo, negativo o cero")
    num = int(input())
    if (num > 0):
        print(str(num) + " es un numero positivo")
    elif (num < 0):
        print(str(num) + " es un numero negativo")
    else: print(str(num) + " es cero")

def ejercicio2():
    print("Ingrese un numero por favor")
    print("Para ver si es divisible por 6")
    num = int(input())
    if(num % 6 == 0):
        print(str(num) + " es divisible por 6")
    else:
        print(str(num) + " no es divisible por 6")

def ejercicio3():
    print("Ingrese un numerador y un divisor para ver si estos son divisibles")
    n = int(input("Numerador --> "))
    m = int(input("Divisor --> "))
    if(n % m == 0):
        print(str(n) + " es divisible por " + str(m))
    else:
        print(str(n) + " no es divisible por " + str(m))

def ejercicio4():
    print("Ingrese un numero del 1 al 7 coorespondiente al dia de la semana")
    n = int(input("Numero --> ")) % 7
    if(n == 0): print("Sábado")
    elif(n == 1): print("Domingo")
    elif(n == 2): print("Lunes")
    elif(n == 3): print("Martes")
    elif(n == 4): print("Miercoles")
    elif(n == 5): print("Jueves")
    elif(n == 6): print("Viernes")

def ejercicio5():
    print("Ingrese la cantidad de pasajeros a viajar")
    print("Para determinar el medio de transporte")
    cantPasajeros = int(input("cantidad de pasajeros: "))
    if(cantPasajeros < 2): print("Bicicleta")
    elif(cantPasajeros < 3): print("Moto")
    elif(cantPasajeros < 5): print("Auto")
    elif(cantPasajeros < 13): print("Camioneta")
    elif(cantPasajeros < 41): print("Colectivo")
    elif(cantPasajeros < 201): print("Avión")
    else: print("No hay un transporte con tanta capacidad") 

def ejercicio6():
    print("Ingrese su año de nacimiento")
    edad = 2020 - int(input("Año nacimiento: "))
    if(edad < 2): print("Usted es un Bebé !!!???")
    elif(edad <= 12): print("Menor")
    elif(edad <= 18): print("Adolescente")
    elif(edad <= 45): print("Adulto")
    elif(edad <= 60): print("Veterano")
    else: print("Abuelo")

def ejercicio7():
    print("Ingrese su sexo biologico y altura")
    sex = str(input("Sexo --> "))
    if(sex == "poco" or sex == "mucho"):
        print("Jajaja ya encerio -_-")
        sex = str(input("Sexo --> "))
    if(sex == "Femenino"):
        altura = int(input("Altura(cm) --> "))
        if(altura < 145): print("jaja Petisa! XD")
        elif(altura < 170): print("señorita usted teien una altura Normal")
        else: print("Señorita usted es mas alta que el promedio D:")
    if(sex == "Masculino"):
        altura = int(input("Altura(cm) --> "))
        if(altura < 160): print("Hola chiquitin n_n")
        elif(altura < 190): print("Que Haces flaco! tenes una estatura Normal")
        else: print("Ehh ... Disculpe usted señor, tiene una estatura envidiable")
    else:
        altura = int(input("Altura(cm) --> "))
        if(altura < 157): print("Usted es petisx")
        elif(altura < 180): print("Usted tiene una estatura normal")
        else: print("Usted es altx")

def ejercicio8():
    print("Ingrese un numero entero para ver si éste es el doble de un número impar")
    num = int(input("Numero --> "))
    if(num % 2 == 0 and not num % 4 == 0):
        print(str(num) + " es el doble de un número impar")
    else:
        print(str(num) + " no es el doble de un número impar")


def ejercicio9():
    print("Ingrese un caracter para ser clasificado")
    caracter = str(input("caracter --> "))
    caracter = caracter[0]
    if(caracter.isalpha()): print(caracter + " es una letra")
    elif(caracter.isdecimal()): print(caracter + " es una dígito")
    else: print(caracter + " es un carácter especial u otro tipo de carácter")

def ejercicio10():
    print("Ingrese el largo de los 3 lados de un triangulo")
    lado1 = float(input("Lado 1 --> "))
    lado2 = float(input("Lado 2 --> "))
    lado3 = float(input("Lado 3 --> "))
    if (lado1 > lado2 + lado3):
        print("Con esos lados no se forma un triangulo!")
    elif(lado2 > lado1 + lado3):
        print("Con esos lados no se forma un triangulo!")
    elif(lado3 > lado1 + lado2):
        print("Con esos lados no se forma un triangulo!")
    else:
        print("Genial con esos lados se puede formar un tirangulo")

def ejercicio11():
    print("Ingrese un caracter del alfabeto")
    char = str(input("Caracter --> "))[0]
    if (char.isalpha()):
        if(char.isupper()):
            print(char + " es una MAYÚSCULA")
        else:
            print(char + " es una MINÚSCULA")

def ejercicio12():
    print("Ingrese un año para saber si es bisiesto")
    year = int(input("Año --> "))
    if(year % 4 == 0):
        if(year % 100 != 0):
            print(str(year) + " es un año bisiesto")
        else:
            if(year % 400 == 0):
                print(str(year) + " es un año bisiesto")
            else:
                print(str(year) + " NO es un año bisiesto")
    else:
        print(str(year) + " es NO año bisiesto")

def ejercicio13():
    print("Cuanto duro la llamada telefónica?")
    seg = int(input("Duracion(seg) -->"))
    if(seg < 60): 
        print("El costo de la llamada es de $1,10")
    else:
        print("El costo de la llamada es de $" + str(1.10 + ((seg - 60) // 15) * 0.25))

def ejercicio14():
    print("Cual es sexo biologico y Edad?")
    sex = str(input("Sexo --> "))
    if(sex == "poco" or sex == "mucho"):
        print("Jajaja ya encerio -_-")
        sex = str(input("Sexo --> "))
    if(sex == "Femenino"):
        edad = int(input("Edad --> "))
        print("Su ritmo cardiaco durante los ejercicios aeróbicos de de ser de " + str((220 - edad) / 10) + " cada 10seg")
    if(sex == "Masculino"):
        edad = int(input("Edad --> "))
        print("Su ritmo cardiaco durante los ejercicios aeróbicos de de ser de " + str((210 - edad) / 10) + " cada 10seg")

exit = False
while(not exit):
    try:
        print()
        print("Que Ejercicio quiere ejecutar? sino use 'exit' para salir")
        ej = input("Ejercicio ")
        if(ej == "exit"): exit = True
        else:
            ej = int(ej)
            if(ej == 1): ejercicio1()
            elif(ej == 2): ejercicio2()
            elif(ej == 3): ejercicio3()
            elif(ej == 4): ejercicio4()
            elif(ej == 5): ejercicio5()
            elif(ej == 6): ejercicio6()
            elif(ej == 7): ejercicio7()
            elif(ej == 8): ejercicio8()
            elif(ej == 9): ejercicio9()
            elif(ej == 10): ejercicio10()
            elif(ej == 11): ejercicio11()
            elif(ej == 12): ejercicio12()
            elif(ej == 13): ejercicio13()
            elif(ej == 14): ejercicio14()
            else: print("El Ejercicio " + str(ej) + " no esta en el programa")
    except:
        print("No no no! esa no es la palabra magica XD")