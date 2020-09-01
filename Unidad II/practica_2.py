import math
ejercicios = []
ejercicios.append(None)
# Ejercicio 1: ¿Qué efecto hace la instrucción input()? 
# Si necesita ingresar un número entero desde el teclado, cómo lo haría?
def ejercicio1():
    entero = input("Por favor ingrese un entero --> ")
    try:
        entero = int(entero)
    except:
        print("'" + entero + "' no es un entero valido")
    print("Su entro es " + str(entero))
ejercicios.append(ejercicio1)

ejercicios.append(None)

# Ejercicio 3: Pedir que se ingrese un número e imprimir el triple
def ejercicio3():
    entero = input("Por favor ingrese un entero --> ")
    try:
        entero = int(entero)
    except:
        print("'" + entero + "' no es un entero valido")
        return
    print("el triple es:")
    print(entero * 3)
ejercicios.append(ejercicio3)

# Ejercicio 4: Pedir que se ingrese un número e imprimir la mitad
def ejercicio4():
    entero = input("Por favor ingrese un entero --> ")
    try:
        entero = int(entero)
    except:
        print("'" + entero + "' no es un entero valido")
        return
    print("la mitad es:")
    print(entero / 2)
ejercicios.append(ejercicio4)

# Ejercicio 5: Pedir que se ingrese 3 notas e imprimir el promedio. 
# Recordar que el promedio es la suma de los números dividido la cantidad.
def ejercicio5():
    print("ingresa tres notas para ser promediadas")
    try:
        primerNota = float(input("primera nota --> "))
    except:
        print("no es una nota valida")
        return
    try:
        segundaNota = float(input("segunda nota --> "))
    except:
        print("no es una nota valida")
        return
    try:
        terceraNota = float(input("tercera nota --> "))
    except:
        print("no es una nota valida")
        return
    print("el promedio es:")
    print((primerNota + segundaNota + terceraNota) / 3)
ejercicios.append(ejercicio5)

# Ejercicio 6: Pedir base y altura de un triángulo y mostrar el área del mismo
def ejercicio6():
    print("Ingrese base y altura del triangulo para calcular su area")
    try:
        ancho = float(input("base --> "))
    except:
        print("no es una altura valida")
        return
    try:
        altura = float(input("altura --> "))
    except:
        print("no es una altura valida")
        return
    print("el area del tirangulo es:")
    print(altura * ancho / 2)
ejercicios.append(ejercicio6)

# Ejercicio 7: Pedir el diámetro de un círculo y calcular su área y perímetro. 
# Recordar que Perímetro = π * Diámetro , Área = π * radio2. 
# Por último, el diámetro = 2 * radio
def ejercicio7():
    print("ingrese el diametro de una circunferencia para calcular su area y su perimetro")
    try:
        diametro = float(input("diametro --> "))
    except:
        print("no es un diametro valido")
        return
    print("su area es:")
    print(math.pi * diametro ** 2)
    print("su perimetro es:")
    print(math.pi * diametro)
ejercicios.append(ejercicio7)

# Ejercicio 8: Pedir 2 números y mostrar la división entre ellos y el resto.
def ejercicio8():
    print("ingrese numerador y divisor para calular la division y su resto")
    try:
        num1 = float(input("numerador --> "))
    except:
        print("no es un numero valido")
        return
    try:
        num2 = float(input("divisor --> "))
    except:
        print("no es un numero valido")
        return
    print("division:")
    print(num1 / num2)
    print("resto:")
    print(num1 % num2)
ejercicios.append(ejercicio8)

# Ejercicio 9: Pedir alto, ancho y largo de una pileta. 
# Calcular el volumen y la cantidad de litros que tiene. 
# (saber que 1000 cm3=1 litro)
def ejercicio9():
    print("ingrese alto, ancho y largo de una pileta para calcular su volumen")
    try:
        alto = float(input("alto en cm --> "))
    except:
        print("no es un numero valido")
        return
    try:
        ancho = float(input("ancho en cm --> "))
    except:
        print("no es un numero valido")
        return
    try:
        largo = float(input("largo en cm --> "))
    except:
        print("no es un numero valido")
        return
    print("volumen:")
    volumen = alto * ancho * largo
    print(str(volumen) + " cm³")
    print(str(volumen / 1000) + " litros")
ejercicios.append(ejercicio9)

# Ejercicio 10: Pedir ancho y largo de un terreno y 
# mostrar cuántos paneles de pasto hay que comprar (son de 60x60 cm)
def ejercicio10():
    print("ingrese ancho y largo de un terreno para calcular la cantidad de paneles de pasto")
    try:
        ancho = float(input("ancho en m --> "))
    except:
        print("no es un numero valido")
        return
    try:
        largo = float(input("ancho en largo --> "))
    except:
        print("no es un numero valido")
        return
    print("vas a necesitar unos " + str(math.ceil(ancho / 0.6 * largo / 0.6)) + " paneles de pasto si es que se pueden aprovechar los recortes")
ejercicios.append(ejercicio10)

# Ejercicio 11: Pedir datos de 4 productos comprados, con su cantidad y 
# precio unitario y mostrar cuánto se gasta por cada producto y el total
def ejercicio11():
    productos = []
    print("Por favor ingrese sus productos con la siguiente estructura separado por comas")
    print("producto, cantidad, precio unitario")
    productos.append(input().split(","))
    productos.append(input().split(","))
    productos.append(input().split(","))
    productos.append(input().split(","))
    try:
        productos[0][1] = int(productos[0][1])
        productos[1][1] = int(productos[1][1])
        productos[2][1] = int(productos[2][1])
        productos[3][1] = int(productos[3][1])
        productos[0][2] = float(productos[0][2])
        productos[1][2] = float(productos[1][2])
        productos[2][2] = float(productos[2][2])
        productos[3][2] = float(productos[3][2])
    except:
        print("algun dato fue ingresado ingresado incorrectamente")
        return
    productos[0].append(productos[0][1]*productos[0][2])
    productos[1].append(productos[1][1]*productos[1][2])
    productos[2].append(productos[2][1]*productos[2][2])
    productos[3].append(productos[3][1]*productos[3][2])
    print("cantidad\tprecio\tsubtotal\tproducto")
    print(str(productos[0][1]) + "\t\t" + str(productos[0][2]) + "\t" + str(productos[0][3]) + "\t\t" + str(productos[0][0]))
    print(str(productos[1][1]) + "\t\t" + str(productos[1][2]) + "\t" + str(productos[1][3]) + "\t\t" + str(productos[1][0]))
    print(str(productos[2][1]) + "\t\t" + str(productos[2][2]) + "\t" + str(productos[2][3]) + "\t\t" + str(productos[2][0]))
    print(str(productos[3][1]) + "\t\t" + str(productos[3][2]) + "\t" + str(productos[3][3]) + "\t\t" + str(productos[3][0]))
    print("total: " + str(productos[0][3] + productos[1][3] + productos[2][3] + productos[3][3]))
ejercicios.append(ejercicio11)

# Ejercicio 12: Diseña un programa que, a partir del valor del lado de un cuadrado (3 metros),  
# muestre el valor de su perímetro (en metros) y el de su área (en metros cuadrados).
# (El perímetro debe darte 12 metros y el área 9 metros cuadrados.)
def ejercicio12():
    lado = 3
    print("si el lado de el cuadrado vale " + str(lado) + "m")
    perimetro = lado * 4
    print("su perimetro debe valer " + str(perimetro) + "m")
    area = lado ** 2
    print("y su area debe valer " + str(area) + "m²")
ejercicios.append(ejercicio12)

# Ejercicio 13: Pedir que se ingrese un nombre e imprimir un saludo, ejemplo: 'hola Juan'
def ejercicio13():
    nombre = str(input("por favor ingrese su nombre --> "))
    nombre = nombre.capitalize()
    print("hola " + nombre)
ejercicios.append(ejercicio13)

# Ejercicio 14: Pedir tres palabras y mostrar un texto con las iniciales de las tres.
def ejercicio14():
    print("por favor ingrese tres palabras, se mostrarn las iniciales de las tres.")
    palabra1 = input(" --> ")
    palabra2 = input(" --> ")
    palabra3 = input(" --> ")
    print((palabra1[0] + palabra2[0] + palabra3[0]).upper())
ejercicios.append(ejercicio14)

# Ejercicio 15: Pedir un verbo en infinitivo y mostrar su terminación (ar, er o ir)
def ejercicio15():
    verbo = input("ingrese un verbo en infinitivo -- > ")
    verbo = verbo.strip()
    print(verbo[len(verbo) - 2: len(verbo)])
ejercicios.append(ejercicio15)

# Ejercicio 16: Pedir nombre, apellido, nro. de alumno y comisión que desea suscribirse. 
# Mostrar el siguiente mensaje 
# "La solicitud de inscripción a la comisión <comision> solicitada por el alumno <apellido>, <nombre> está siendo procesada"
def ejercicio16():
    print("Ingrese nombre, apellido, nro. de alumno y comisión que desea suscribirse")
    nombre = input("nombre --> ")
    apellido = input("apellido --> ")
    nroAlumno = input("nro. de alumno --> ")
    comision = input("comisión --> ")
    print("La solicitud de inscripción a la comisión " + comision + " solicitada por el alumno " + apellido + " " + nroAlumno + ", " + nombre + " está siendo procesada")
ejercicios.append(ejercicio16)

# Ejercicio 17: Pedir cuatro datos, quién, qué hizo, cuándo y cómo. 
# Mostrar la siguiente noticia: 
# "Última noticia!, la persona xx, en el dia xx, hizo xx, de la siguiente manera xx"
def ejercicio17():
    print("Por favor responda las perguntas de sobre el hecho")
    quien = input("¿quién fue el actor del hecho? --> ")
    que = input("¿qué hizo? --> ")
    cuando = input("¿cuándo lo hizo? --> ")
    como = input("¿cómo lo hizo? --> ")
    print("Última noticia!, la persona " + quien + ", en el dia " + cuando + ", hizo " + que + ", de la siguiente manera " + como)
ejercicios.append(ejercicio17)

# Ejercicio 18: Pedir nombre, apellido de una persona y el día, mes, año en que nació. 
# Armarle una clave con esos datos (su clave seria sus iniciales seguido de un guión bajo 
# y de su año de nacimiento) y mostrarla.
def ejercicio18():
    print("Por favor ingrese su nombre, apellido y el día, mes y año en que nació.")
    nombre = input("Nombre --> ").strip()
    apellido = input("Apellido --> ").strip()
    day = int(input("Facha de Nacimiento: Dia --> "))
    month = int(input("Facha de Nacimiento: Mes --> "))
    year = int(input("Facha de Nacimiento: Año --> "))
    print((nombre[0] + apellido[0] + "_" + str(day) + str(month) + str(year)).upper())
ejercicios.append(ejercicio18)

# Ejercicio 19: Mostrar 5 veces la cadena "Hola"
def ejercicio19():
    print("Hola " * 5)
ejercicios.append(ejercicio19)

# Ejercicio 20:Ejecutar los siguientes códigos. 
# ¿Cuál es el resultado de las siguientes ejecuciones?. 
# Justificar
ejercicios.append([])
def ejercicio20_a():
    print("tupla=(1,True,['a','b','c'], \"hola\")\ntupla[1]=False\n\nno se puede asignar valor a una tupla")
ejercicios[20].append(ejercicio20_a)

def ejercicio20_b():
    tupla=(1,True,['a','b','c'], "hola")
    tupla[2][0]='b'
    print(tupla)
    # pero si se puede asignar una valor a una lista que esta dentro de una tupla
ejercicios[20].append(ejercicio20_b)

# Ejercicio 21: Dada la siguiente estructura: 
# lista=[1,True,['a','b','c'], "hola"]
# Ejecutar la siguientessentencias y describir los resultados.
ejercicios.append([])
def ejercicio21_a():
    lista=[1,True,['a','b','c'], "hola"]
    print (lista[2])
ejercicios[21].append(ejercicio21_a)

def ejercicio21_b():
    lista=[1,True,['a','b','c'], "hola"]
    print (lista [4])
ejercicios[21].append(ejercicio21_b)

def ejercicio21_c():
    lista=[1,True,['a','b','c'], "hola"]
    lista.append (False)
    print (lista)
ejercicios[21].append(ejercicio21_c)

# Ejercicio 22: 
def ejercicio22():
    lista=[1,True,['a','b','c'], "hola"]
    del lista[2]
    print (lista)
ejercicios.append(ejercicio22)

# Ejercicio 23: Dada la siguiente información, elija una estructura de datos que 
# permita guardarla adecuadamente
# - Guerra del Peloponeso 431 a.C
# - Revolución de Mayo 1810 d.C
# - Llegada de los españoles a América 1492 d.C
# - Comienzo de la construcción de la gran Muralla China 214 a.C
def ejercicio23():
    lista=[["Guerra del Peloponeso", 431, "a.C"],
        ["Revolución de Mayo", 1810, "d.C"],
        ["Llegada de los españoles a América", 1492, "d.C"],
        ["Comienzo de la construcción de la gran Muralla China", 214, "a.C"]]
    print(lista[0])
    print(lista[1])
    print(lista[2])
    print(lista[3])
ejercicios.append(ejercicio23)

# Ejercicio 24: Escriba un programa que reciba un nombre ingresado por el usuario e 
# imprima en la pantalla un saludo.
# En pantalla debe aparecer "¡Hola xxx!"
def ejercicio24():
    print("Hola!, ¿como te llamas?")
    nombre = input("Tu: --> ")
    print("¡Hola " + nombre + "!")
ejercicios.append(ejercicio24)
# ¿Hizo uso de variables? ¿Cuáles?
# Si, 'nombre', que es donde almaceno el nombre del usuario
# ¿Hizo uso de valores? ¿Cuáles?
# Si, use varios "Hola!, ¿como te llamas?", "Tu: --> ", "¡Hola " y "!"
# ¿Hizo uso de operadores? ¿Cuáles?
# Si, use el operador + que como los operandos son cadenas funciona para concatenar los mismos
# ¿Qué sentencias utilizó?

# Ejercicio 25: Escriba un programa que reciba un nombre y una edad ingresado por 
# el usuario e imprima en la pantalla un texto con la información ingresada por el usuario.
# En pantalla debe aparecer " Su nombre es xxx y su edad es xx"
def ejercicio25():
    print("Hola!, ¿como te llamas?")
    nombre = input("Tu: --> ")
    print("¡Hola " + nombre + "!")
    print("¿que edad tienes?")
    edad = input(nombre + ": --> ")
    print(" Su nombre es " + nombre + " y su edad es " + edad)
ejercicios.append(ejercicio25)
# ¿Hizo uso de variables? ¿Cuáles?
# Si, 'nombre' y 'edad'
# ¿Hizo uso de valores? ¿Cuáles?
# Si, "Hola!, ¿como te llamas?", "Tu: --> ", "¡Hola ", "!", "¿que edad tienes?",
# ": --> ", " Su nombre es ", " y su edad es "
# ¿Hizo uso de operadores? ¿Cuáles?
# Si, el operador '+' que se usa para concatenar en estos casos
# ¿Qué sentencias utilizó?

# Ejercicio 26: Ejecute el siguiente código e indique, en cada caso, con qué valor finaliza 
# la variable x. Justifique su respuesta.
ejercicios.append([])
def ejercicio26_a():
    x= 10
    X= x**2
    print (x)
ejercicios[26].append(ejercicio26_a)

def ejercicio26_b():
    x=30
    # x= x % 4
    print (x)
ejercicios[26].append(ejercicio26_b)

def ejercicio26_c():
    a= "4"
    b= "3"
    x= a + b
    print (x)
ejercicios[26].append(ejercicio26_c)

def ejercicio26_d():
    a= "4"
    b= 3
    x= a * b
    print (x)
ejercicios[26].append(ejercicio26_d)

def ejercicio26_e():
    a= 4
    b= 3
    x= "a" * b
    print (x)
ejercicios[26].append(ejercicio26_e)

# Ejercicio 27 : Ejecute el siguiente código y diga qué hace y qué elementos de programación 
# se utilizan: variables, valores, operadores y sentencias.
ejercicios.append([])
def ejercicio27_a():
    print

    ('hola')
ejercicios[27].append(ejercicio27_a)

def ejercicio27_b():
    print (2)
ejercicios[27].append(ejercicio27_b)

def ejercicio27_c():
    print("nombre=input('Ingr\n\nese un nombre')\nprint (nombre)\n\nFile \"practica_2.py\", line 420\n    nombre=input('Ingr\n                     ^\nSyntaxError: EOL while scanning string literal")
ejercicios[27].append(ejercicio27_c)

def ejercicio27_d():
    print("\nedad=input('Ingrese la\n\nedad')\nprint (edad)\n\n  File \"practica_2.py\", line 433\n    edad=input('Ingrese la\n                         ^\nSyntaxError: EOL while scanning string literal")
ejercicios[27].append(ejercicio27_d)

def ejercicio27_e():
    print (2*3)
ejercicios[27].append(ejercicio27_e)

def ejercicio27_f():
    print (4%2)
ejercicios[27].append(ejercicio27_f)

def ejercicio27_g():
    print("\nnum1=input('Ingrese un\n\nnúmero')\nnum2=input('Ingrese otro\nnúmero')\nprint (num1+num2)\n\n  File \"practica_2.py\", line 454\n    num1=input('Ingrese un\n                         ^\nSyntaxError: EOL while scanning string literal")
ejercicios[27].append(ejercicio27_g)

def ejercicio27_h():
    print("\nnum1=int(input('Ingrese\n\nun número'))\nnum2=int(input('Ingrese\notro número'))\nprint (num1+num2)\n\n  File \"practica_2.py\", line 469\n    num1=int(input('Ingrese\n                          ^\nSyntaxError: EOL while scanning string literal")
ejercicios[27].append(ejercicio27_h)

ejercicios.append([])
def ejercicio28_1():
    print("5 // 2")
    resul = 5 // 2
    print(resul)
ejercicios[28].append(ejercicio28_1)

def ejercicio28_2():
    print("7.2 * 9.8")
    resul = 7.2 * 9.8 
    print(resul)
ejercicios[28].append(ejercicio28_2)

def ejercicio28_3():
    print("7 - 3.1")
    resul = 7 - 3.1
    print(resul)
ejercicios[28].append(ejercicio28_3)

def ejercicio28_4():
    print("10.45 + 7")
    resul = 10.45 + 7
    print(resul)
ejercicios[28].append(ejercicio28_4)

def ejercicio28_5():
    print("\"republica \" + \"argentina\"")
    resul = "republica " + "argentina"
    print(resul)
ejercicios[28].append(ejercicio28_5)

def ejercicio28_6():
    print("\"argentina \" * 3")
    resul = "argentina " * 3
    print(resul)
ejercicios[28].append(ejercicio28_6)

# Ejercicio 29: Si se tiene las variables n1=124.25 y n2= "33.40". Realizar las conversiones
# necesarias para saber la división entera entre ellos y el resto.
def ejercicio29():
    n1 = 124.25
    n2 = "33.40"
    n2 = float(n2)
    print("Division Entera: " + str(n1 // n2))
    print("Resto: " + str(n1 % n2))
ejercicios.append(ejercicio29)

# Ejercicio 30: Pedir 5 palabras y mostrar la cantidad de letras que tienen en total
def ejercicio30():
    print("Ingrese 5 palabras, para contar sus letras")
    palbras = input("Palabra 1 --> ")
    palbras += input("Palabra 2 --> ")
    palbras += input("Palabra 3 --> ")
    palbras += input("Palabra 4 --> ")
    palbras += input("Palabra 5 --> ")
    print("Estas suman " + str(len(palbras)) + " letras en total")
ejercicios.append(ejercicio30)

# Ejercicio 31: Pedir el cuit que tiene la siguiente forma xx/dni/x. Extraer y mostrar el dni.
def ejercicio31():
    print("Ingrese su cuit con la extructura xx/dni/x")
    cuit = str(input(" --> "))
    a = cuit.index("/") + 1
    b = cuit.index("/", a)
    print("Su DNI es :'" + cuit[a:b] + "'")
ejercicios.append(ejercicio31)

# Ejercicio 32: Mostrar el código ASCII de los caracteres "A", "a" y "0"
def ejercicio32():
    print("El codigo ASCII de 'A' es " + str(ord('A')))
    print("El codigo ASCII de 'a' es " + str(ord('a')))
    print("El codigo ASCII de '0' es " + str(ord('0')))
ejercicios.append(ejercicio32)

# Ejercicio 33: Pedir la cuenta de mail al usuario y mostrar por separado su usuario y su dominio.
def ejercicio33():
    print("Por favor ingrese su mail")
    print("ejemplo: 'MyMail@ejemplo.com'")
    mail = input("Mail: --> ")
    print("Usuario: '" + mail[0:mail.index("@")] + "'")
    print("Dominio: '" + mail[mail.index("@")+ 1: len(mail)] + "'")
ejercicios.append(ejercicio33)

# Menu:
def menu():
    exit = False
    while (not exit):
        print()
        print("¿Que ejercicio quiere ejecutar? sino use 'exit' para salir")
        ejercicio = input("Ejercicio ")
        if (ejercicio == "exit"):
            exit = True
        else:
            try:
                ejercicio = int(ejercicio)
                if(ejercicio == 2 or ejercicio > 33):
                    print("El ejercicio " + str(ejercicio) + " no esta en el programa")
                elif(ejercicio == 20):
                    print("'a' o 'b'")
                    indice = str(input(" -->"))
                    if (indice == "a"): ejercicios[ejercicio][0]()
                    if (indice == "b"): ejercicios[ejercicio][1]()
                elif(ejercicio == 21):
                    print("'a', 'b', 'c'")
                    indice = str(input(" -->"))
                    if (indice == "a"): ejercicios[ejercicio][0]()
                    if (indice == "b"): ejercicios[ejercicio][1]()
                    if (indice == "c"): ejercicios[ejercicio][2]()
                elif(ejercicio == 26):
                    print("'a', 'b', 'c', 'd', 'e'")
                    indice = str(input(" -->"))
                    if (indice == "a"): ejercicios[ejercicio][0]()
                    if (indice == "b"): ejercicios[ejercicio][1]()
                    if (indice == "c"): ejercicios[ejercicio][2]()
                    if (indice == "d"): ejercicios[ejercicio][3]()
                    if (indice == "e"): ejercicios[ejercicio][4]()
                elif(ejercicio == 27):
                    print("'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'")
                    indice = str(input(" -->"))
                    if (indice == "a"): ejercicios[ejercicio][0]()
                    if (indice == "b"): ejercicios[ejercicio][1]()
                    if (indice == "c"): ejercicios[ejercicio][2]()
                    if (indice == "d"): ejercicios[ejercicio][3]()
                    if (indice == "e"): ejercicios[ejercicio][4]()
                    if (indice == "f"): ejercicios[ejercicio][5]()
                    if (indice == "g"): ejercicios[ejercicio][6]()
                    if (indice == "h"): ejercicios[ejercicio][7]()
                elif(ejercicio == 28):
                    print("'1', '2', '3', '4', '5' o '6'")
                    indice = str(input(" -->"))
                    if (indice == "1"): ejercicios[ejercicio][0]()
                    if (indice == "2"): ejercicios[ejercicio][1]()
                    if (indice == "3"): ejercicios[ejercicio][2]()
                    if (indice == "4"): ejercicios[ejercicio][3]()
                    if (indice == "5"): ejercicios[ejercicio][4]()
                    if (indice == "6"): ejercicios[ejercicio][5]()
                    if (indice == "7"): ejercicios[ejercicio][6]()
                else:
                    ejercicios[ejercicio]()
            except:
                print("esa no es la palabra magica XD")

menu()