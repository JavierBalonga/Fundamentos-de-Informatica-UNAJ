![alt text](https://www.unaj.edu.ar/wp-content/uploads/2016/06/logo-unaj-2016-01.jpg)
# Fundamentos de Informatica

## Practica 2
---
### PARTE I: Aspectos Conceptuales
##### Ejercicio 1: ¿Qué efecto hace la instrucción input()? Si necesita ingresar un número entero desde el teclado, cómo lo haría?
La instrucción `input()` sirve para solicitarle al usuario el ingreso de un valor.
```Py
    entero = input("Por favor ingrese un entero --> ")
    try:
        entero = int(entero)
    except:
        print("'" + entero + "' no es un entero valido")
    print("Su entro es " + str(entero))
```
```powershell
Por favor ingrese un entero --> 2
Su entro es 2
```

##### Ejercicio 2: Defina la diferencia entre una lista y una tupla. ¿En qué casos utilizarías cada una?
- lista: Una lista es una estructura de datos lo especial de las listas es que nos permiten almacenar cualquier tipo de valor como enteros, cadenas y hasta otras funciones, y sus datos son mutables, para declarar la misma se deve utilizar corchetes y separar los elementos con una coma`[e0, e1, ...]`, sus metodos son los siguientes:
    Metodo	    Descripcion
    `append()`  Agrega un elemento al final de la lista
    `clear()`   Borra todos los elementos de la lista
    `copy()`    Regresa una copia de la lista
    `count()`   Regresa la cantidad de elementos que sean iguales al parametro que se pase
    `extend()`  Agrega elementos de otra lista(u otro elemento iterable) que se pasa como parametro al final de la lista actual
    `index()`   Regresa el indice del primer elemento que coincide con el parametro que se le pase
    `insert()`  Agrega en la posicion que se pase como primer parametro el elemento que se pase como segundo parametro
    `pop()`     Quita el elemento de una posicion especifica que se pase como parametro
    `remove()`  Quita el primer elemento que coincida con el parametroq ue se le pase 
    `reverse()` Invierte los elementos de la lista
    `sort()`    Ordenta la lista
Para llamar un metodo devo hacerlo de la siguiente manera
```Py
myList = [1, 4, 2, 3] 
myList.sort()
print(myList)
```

- Tupla: Una tupla es una estructura de datos inmutables, lo que quiere decir que esta una vez es declarada no puede ser modificada, para declarar la misma se deve utilizar parentesis y separar los elementos con una coma`(e0, e1, ...)`, sus metodos son los siguientes:
    Metodo      Descripcion
    `count()`   Regresa la cantidad de elementos que sean iguales al parametro que se pase
    `index()`   Regresa el indice del primer elemento que coincide con el parametro que se le pase
Para llamar un metodo devo hacerlo de la siguiente manera
```Py
myList = (1, 4, 2, 3) 
print(myList.index(4))
```


---
### PARTE II: Trabajamos sobre los tipos de datos:
#### -Numéricos
##### Ejercicio 3: Pedir que se ingrese un número e imprimir el triple
```Py
    entero = input("Por favor ingrese un entero --> ")
    try:
        entero = int(entero)
    except:
        print("'" + entero + "' no es un entero valido")
        return
    print("el triple es:")
    print(entero * 3)
```
```powershell
Por favor ingrese un entero --> 4
el triple es:
12
```
##### Ejercicio 4: Pedir que se ingrese un número e imprimir la mitad
```py
    entero = input("Por favor ingrese un entero --> ")
    try:
        entero = int(entero)
    except:
        print("'" + entero + "' no es un entero valido")
        return
    print("la mitad es:")
    print(entero / 2)
```
```powershell
Por favor ingrese un entero --> 5
la mitad es:
2.5
```

##### Ejercicio 5: Pedir que se ingrese 3 notas e imprimir el promedio. Recordar que el promedio es la suma de los números dividido la cantidad.
```py
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
```
```powershell
ingresa tres notas para ser promediadas
primera nota --> 7
segunda nota --> 5
tercera nota --> 8
el promedio es:
6.666666666666667
```

##### Ejercicio 6: Pedir base y altura de un triángulo y mostrar el área del mismo
```py
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
```
```powershell
Ingrese base y altura del triangulo para calcular su area
base --> 5
altura --> 3
el area del tirangulo es:
7.5
```

##### Ejercicio 7: Pedir el diámetro de un círculo y calcular su área y perímetro.  
##### Recordar que Perímetro = π * Diámetro , Área = π * radio2. Por último, el diámetro = 2 * radio
```py
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
```
```powershell
ingrese el diametro de una circunferencia para calcular su area y su perimetro
diametro --> 10
su area es:
314.1592653589793
su perimetro es:
31.41592653589793
```

##### Ejercicio 8: Pedir 2 números y mostrar la división entre ellos y el resto.
```py
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
```
```powershell
ingrese numerador y divisor para calular la division y su resto
numerador --> 10
divisor --> 4
division:
2.5
resto:
2.0
```

##### Ejercicio 9: Pedir alto, ancho y largo de una pileta. Calcular el volumen y la cantidad de litros que tiene.  
##### (saber que 1000 cm3=1 litro)
```py
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
```
```powershell
ingrese alto, ancho y largo de una pileta para calcular su volumen
alto en cm --> 10
ancho en cm --> 10
largo en cm --> 100
volumen:
10000.0 cm³
10.0 litros
```

##### Ejercicio 10: Pedir ancho y largo de un terreno y mostrar cuántos paneles de pasto hay que comprar (son de 60x60 cm)
```py
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
```
```powershell
ingrese ancho y largo de un terreno para calcular la cantidad de paneles de pasto
ancho en m --> 10
ancho en largo --> 100
vas a necesitar unos 2778 paneles de pasto si es que se pueden aprovechar los recortes
```

##### Ejercicio 11: Pedir datos de 4 productos comprados, con su cantidad y precio unitario y mostrar cuánto se gasta por cada producto y el total
```py
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
```
```powershell
Por favor ingrese sus productos con la siguiente estructura separado por comas
producto, cantidad, precio unitario
mouse,2,100
teclado,1,400
auriculares,1,200
monitor,1,5000
cantidad        precio  subtotal        producto
2               100.0   200.0           mouse
1               400.0   400.0           teclado
1               200.0   200.0           auriculares
1               5000.0  5000.0          monitor
total: 5800.0
```

##### Ejercicio 12: Diseña un programa que, a partir del valor del lado de un cuadrado (3 metros), muestre el valor de su perímetro (en metros) y el de su área (en metros cuadrados). (El perímetro debe darte 12 metros y el área 9 metros cuadrados.)
```py
    lado = 3
    print("si el lado de el cuadrado vale " + str(lado) + "m")
    perimetro = lado * 4
    print("su perimetro debe valer " + str(perimetro) + "m")
    area = lado ** 2
    print("y su area debe valer " + str(area) + "m²")
```
```powershell
si el lado de el cuadrado vale 3m
su perimetro debe valer 12m
y su area debe valer 9m²
```

#### -Cadenas de texto
##### Ejercicio 13: Pedir que se ingrese un nombre e imprimir un saludo, ejemplo: 'hola Juan'
```py
    nombre = str(input("por favor ingrese su nombre --> "))
    nombre = nombre.capitalize()
    print("hola " + nombre)
```
```powershell
por favor ingrese su nombre --> javier
hola Javier
```

##### Ejercicio 14: Pedir tres palabras y mostrar un texto con las iniciales de las tres.
```py
    print("por favor ingrese tres palabras, se mostrarn las iniciales de las tres.")
    palabra1 = input(" --> ")
    palabra2 = input(" --> ")
    palabra3 = input(" --> ")
    print((palabra1[0] + palabra2[0] + palabra3[0]).upper())
```
```powershell
por favor ingrese tres palabras, se mostrarn las iniciales de las tres.
 --> Universidad
 --> nacional
 --> arturo
UNA
```

##### Ejercicio 15: Pedir un verbo en infinitivo y mostrar su terminación (ar, er o ir)
```py
    verbo = input("ingrese un verbo en infinitivo -- > ")
    verbo = verbo.strip()
    print(verbo[len(verbo) - 2: len(verbo)])
```
```powershell
ingrese un verbo en infinitivo -- > programar
ar
```

##### Ejercicio 16: Pedir nombre, apellido, nro. de alumno y comisión que desea suscribirse. Mostrar el siguiente mensaje "La solicitud de inscripción a la comisión <comision> solicitada por el alumno <apellido>, <nombre> está siendo procesada"
```py
    print("Ingrese nombre, apellido, nro. de alumno y comisión que desea suscribirse")
    nombre = input("nombre --> ")
    apellido = input("apellido --> ")
    nroAlumno = input("nro. de alumno --> ")
    comision = input("comisión --> ")
    print("La solicitud de inscripción a la comisión " + comision + " solicitada por el alumno " + apellido + " " + nroAlumno + ", " + nombre + " está siendo procesada")
```
```powershell
Ingrese nombre, apellido, nro. de alumno y comisión que desea suscribirse
nombre --> javier
apellido --> balonga
nro. de alumno --> 1234-5
comisión --> 17
La solicitud de inscripción a la comisión 17 solicitada por el alumno balonga 1234-5, javier está siendo procesada
```

##### Ejercicio 17: Pedir cuatro datos, quién, qué hizo, cuándo y cómo. Mostrar la siguiente noticia: "Última noticia!, la persona xx, en el dia xx, hizo xx, de la siguiente manera xx"
```py
    print("Por favor responda las perguntas de sobre el hecho")
    quien = input("¿quién fue el actor del hecho? --> ")
    que = input("¿qué hizo? --> ")
    cuando = input("¿cuándo lo hizo? --> ")
    como = input("¿cómo lo hizo? --> ")
    print("Última noticia!, la persona " + quien + ", en el dia " + cuando + ", hizo " + que + ", de la siguiente manera " + como)
```
```powershell
Por favor responda las perguntas de sobre el hecho
¿quién fue el actor del hecho? --> Javier Balonga
¿qué hizo? --> la paractica 2
¿cuándo lo hizo? --> de hoy
¿cómo lo hizo? --> y en la compu
Última noticia!, la persona Javier Balonga, en el dia de hoy, hizo la paractica 2, de la siguiente manera y en la compu
```

##### Ejercicio 18: Pedir nombre, apellido de una persona y el día, mes, año en que nació. Armarle una clave con esos datos (su clave seria sus iniciales seguido de un guión bajo y de su año de nacimiento) y mostrarla.
```py
    print("Por favor ingrese su nombre, apellido y el día, mes y año en que nació.")
    nombre = input("Nombre --> ").strip()
    apellido = input("Apellido --> ").strip()
    day = int(input("Facha de Nacimiento: Dia --> "))
    month = int(input("Facha de Nacimiento: Mes --> "))
    year = int(input("Facha de Nacimiento: Año --> "))
    print((nombre[0] + apellido[0] + "_" + str(day) + str(month) + str(year)).upper())
```
```powershell
Por favor ingrese su nombre, apellido y el día, mes y año en que nació.
Nombre --> Javier
Apellido --> balonga
Facha de Nacimiento: Dia --> 7
Facha de Nacimiento: Mes --> 5
Facha de Nacimiento: Año --> 1994
JB_751994
```

##### Ejercicio 19: Mostrar 5 veces la cadena "Hola"
```py
    print("Hola " * 5)
```
```powershell
Hola Hola Hola Hola Hola
```

#### -Listas y tuplas
##### Ejercicio 20:Ejecutar los siguientes códigos. ¿Cuál es el resultado de las siguientes ejecuciones?. Justificar
###### a) 
```Py
tupla=(1,True,['a','b','c'], "hola")
tupla[1]=False
```
```powershell
Traceback (most recent call last):
  File "practica_2.py", line 278, in <module>
    tupla[1]=False
TypeError: 'tuple' object does not support item assignment
```

###### b) 
```Py
tupla=(1,True,['a','b','c'], "hola")
tupla[2][0]='b'
```
```powershell
(1, True, ['b', 'b', 'c'], 'hola')
```

##### Ejercicio 21: Dada la siguiente estructura: 
```Py
lista=[1,True,['a','b','c'], "hola"]
```

##### . Ejecutar la siguientessentencias y describir los resultados.
###### a) 
```Py
print (lista[2])
```
```powershell
['a', 'b', 'c']
```

###### b) 
```Py
print (lista [4])
```
```powershell
  File "practica_2.py", line 298, in <module>
    print (lista [4])
NameError: name 'lista' is not defined
```

###### c) 
```Py
lista.append (False)
print (lista)
```
```powershell
[1, True, ['a', 'b', 'c'], 'hola', False]
```

##### Ejercicio 22: 
```Py
lista=[1,True,['a','b','c'], "hola"]
del lista[2]
print (lista)
```
```powershell
Ejercicio 22
[1, True, 'hola']
```
##### Ejercicio 23: Dada la siguiente información, elija una estructura de datos que permita guardarla adecuadamente
- Guerra del Peloponeso 431 a.C
- Revolución de Mayo 1810 d.C
- Llegada de los españoles a América 1492 d.C
- Comienzo de la construcción de la gran Muralla China 214 a.C  
Yo elegi las listas, pero tambien con tuplas hubiera andado
```Py
    lista=[["Guerra del Peloponeso", 431, "a.C"],
        ["Revolución de Mayo", 1810, "d.C"],
        ["Llegada de los españoles a América", 1492, "d.C"],
        ["Comienzo de la construcción de la gran Muralla China", 214, "a.C"]]
    print(lista[0])
    print(lista[1])
    print(lista[2])
    print(lista[3])
```
```powershell
['Guerra del Peloponeso', 431, 'a.C']
['Revolución de Mayo', 1810, 'd.C']
['Llegada de los españoles a América', 1492, 'd.C']
['Comienzo de la construcción de la gran Muralla China', 214, 'a.C']
```

### PARTE III Datos, Variables y Tipos de Datos:
##### Ejercicio 24: Escriba un programa que reciba un nombre ingresado por el usuario e imprima en la pantalla un saludo.  
##### En pantalla debe aparecer "¡Hola xxx!"  
##### ¿Hizo uso de variables? ¿Cuáles?
Si, `nombre`, que es donde almaceno el nombre del usuario
##### ¿Hizo uso de valores? ¿Cuáles?
Si, use varios `"Hola!, ¿como te llamas?"`, `"Tu: --> "`, `"¡Hola "` y `"!"`
##### ¿Hizo uso de operadores? ¿Cuáles?
Si, use el operador `+` que como los operandos son cadenas funciona para concatenar los mismos
##### ¿Qué sentencias utilizó?
```Py
    print("Hola!, ¿como te llamas?")
    nombre = input("Tu: --> ")
    print("¡Hola " + nombre + "!")
```
```powershell
Hola!, ¿como te llamas?
Tu: --> Javier
¡Hola Javier!
```

##### Ejercicio 25: Escriba un programa que reciba un nombre y una edad ingresado por el usuario e imprima en la pantalla un texto con la información ingresada por el usuario.  
##### En pantalla debe aparecer " Su nombre es xxx y su edad es xx"  
##### ¿Hizo uso de variables? ¿Cuáles?
Si, `nombre` y `edad`
##### ¿Hizo uso de valores? ¿Cuáles?
Si, `Hola!, ¿como te llamas?`, `Tu: --> `, `¡Hola `, `!`, `¿que edad tienes?`, `: --> `, ` Su nombre es `, ` y su edad es `
##### ¿Hizo uso de operadores? ¿Cuáles?
Si, el operador `+` que se usa para concatenar en estos casos
##### ¿Qué sentencias utilizó?
```py
    print("Hola!, ¿como te llamas?")
    nombre = input("Tu: --> ")
    print("¡Hola " + nombre + "!")
    print("¿que edad tienes?")
    edad = input(nombre + ": --> ")
    print(" Su nombre es " + nombre + " y su edad es " + edad)
```
```powershell
Hola!, ¿como te llamas?
Tu: --> Javier
¡Hola Javier!
¿que edad tienes?
Javier: --> 26
 Su nombre es Javier y su edad es 26
```

##### Ejercicio 26: Ejecute el siguiente código e indique, en cada caso, con qué valor finaliza la variable x. Justifique su respuesta.
###### a)
```Py
x= 10
X= x**2
print (x)
```
```powershell
10
```
El valor que toma `x` es `10` porque en la segunda instruccion se le asigna una valor a `X` que no es lo mismo que `x` uno es mayuscula y el otro misnuscula

###### b)
```Py
x=30
# x= x % 4
print (x)
```
```powershell
30
```
`x` toma el valor de `30`, la segunda linea es un comentario

###### c)
```Py
a= "4"
b= "3"
x= a + b
print (x)
```
```powershell
43
```
`x` toma el valor de la `"43"`, concatenacion de `a` y `b` `"4"+"3"`

###### d)
```Py
a= "4"
b= 3
x= a * b
print (x)
```
```powershell
444
```
`x` toma el valor de `"444"`,la concatenacion de tres veces `a`, dado que `b` tiene asignado el valor numerico `3`, y `b` tiene `"4"`

###### e)
```Py
a= 4
b= 3
x= "a" * b
print (x)
```
```powershell
aaa
```
`x`toma el valor de `"aaa"`, el triple de la cadena`"a"` porque cuando se usa `""` se refiere a una cadena, y cuando no se usa se refiere a otro elemento declarado

##### Ejercicio 27 : Ejecute el siguiente código y diga qué hace y qué elementos de programación se utilizan: variables, valores, operadores y sentencias.
###### a)
```Py
print ('hola')
```
```powershell
```
- Que hace?:  
    imprime `hola` en la consola
- Variables:  
    No hay
- Valores  
    `'hola'`
- Operadores  
    No hay
- Sentencias  
    `>>> print`
    `>>> ('hola')`


###### b)
```Py
print (2)
```
```powershell
2
```
- Que hace?:  
    Imprime el valor `2`
- Variables:  
    No hay
- Valores  
    `2`
- Operadores  
    No hay
- Sentencias  
    `>>> print (2)`

###### c)
```Py
nombre=input('Ingrese un nombre')
print (nombre)
```
```powershell
Ingrese un nombreJavier
Javier
```
- Que hace?:  
    Solicita un valor con el prompt`'Ingrese un nombre'` y lo imprime por consola
- Variables:  
    `nombre`
- Valores  
    `'Ingrese un nombre'`
- Operadores  
    No hay
- Sentencias  
    `>>> nombre=input('Ingrese un nombre')`
    `>>> print (nombre)`

###### d)
```Py
edad=input('Ingrese la edad')
print (edad)
```
```
Ingrese la edad26
26
```
- Que hace?:  
    Solicita un valor con el prompt`'Ingrese la edad'` y lo imprime por consola
- Variables:  
    `edad`
- Valores  
    `'Ingrese la edad'`
- Operadores  
    
- Sentencias  
    `>>> edad=input('Ingrese la edad')`
    `>>> print (edad)`

###### e)
```Py
print (2*3)
```
```powershell
6
```
- Que hace?:  
    multiplica los valores `2` y `3` y lo imprime en la consola
- Variables:  
    No hay
- Valores  
    `2`, `3`
- Operadores  
    `*`
- Sentencias  
    `>>> print (2*3)`

###### f)
```Py
print (4%2)
```
```powershell
0
```
- Que hace?:  
    Calcula el resto de `4` entre `2` y lo imprime en la consola
- Variables:  
    No hay
- Valores  
    `4`, `2`
- Operadores  
    `%`
- Sentencias  
    `>>> print (4%2)`

###### g)
```Py
num1=input('Ingrese un número')
num2=input('Ingrese otro número')
print (num1+num2)
```
```powershell
Ingrese un número7
Ingrese otro número3
73
```
- Que hace?:  
    Solicita dos valores con los prompt`'Ingrese un número'`, `'Ingrese otro número'`, los concatena y los imprime por consola
- Variables:  
    `num1`, `num2`
- Valores  
    `'Ingrese un número'`, `'Ingrese otro número'`
- Operadores  
    `+`
- Sentencias  
    `>>> num1=input('Ingrese un número')`
    `>>> num2=input('Ingrese otro número')`
    `>>> print (num1+num2)`

###### h)
```Py
num1=int(input('Ingrese un número'))
num2=int(input('Ingrese otro número'))
print (num1+num2)
```
```powershell
Ingrese un número7
Ingrese otro número3
10
```
- Que hace?:  
    Solicita dos valores con los prompt`'Ingrese un número'`, `'Ingrese otro número'`, los convierte a enteros, los suma y los imprime por consola
- Variables:  
    `num1`, `num2`
- Valores  
    `'Ingrese un número'`, `'Ingrese otro número'`
- Operadores  
    `+`
- Sentencias  
    `>>> num1=int(input('Ingrese un número'))`
    `>>> num2=int(input('Ingrese otro número'))`
    `>>> print (num1+num2)`

##### Ejercicio 28: Asígnele a las variables num1 y num2 los distintos valores indicados en la tabla.
##### Realice las siguientes cuentas con las operaciones indicadas almacenando el resultado en la variable resul.
#####  En la tabla que aparece a continuación coloque los resultados obtenidos y justifíquelo.

X|Valor de num1|Valor de num2|Operación|Valor de resul|Justificación
-|-------------|-------------|---------|--------------|-------------
1|5|2|`//`|2|se divide num1 por num2 y se los redondea para abajo
2|7.2|9.8|`*`|70.56|multiplica los operandos
3|7|3.1|`-`|3.9|resta los operandos
4|10.45|7|`+`|17.45|suma los operandos
5|"republica "|"argentina"|`+`|"republica argentina"|como son cadenas concatena los operandos
6|"argentina "|3|`*`|"argentina argentina argentina"|aca se concatena las veces de num2 la cadena original

### PARTE IV: Aplicando funciones y métodos a los tipos de datos
##### Ejercicio 29: Si se tiene las variables n1=124.25 y n2= "33.40". Realizar las conversiones necesarias para saber la división entera entre ellos y el resto.
```Py
    n1 = 124.25
    n2 = "33.40"
    n2 = float(n2)
    print("Division Entera: " + str(n1 // n2)
    print("Resto: " +n1 % n2)
```
```powershell
Division Entera: 3
Resto: 24.050000000000004
```

##### Ejercicio 30: Pedir 5 palabras y mostrar la cantidad de letras que tienen en total
```Py
    print("Ingrese 5 palabras, para contar sus letras")
    palbras = input("Palabra 1 --> ")
    palbras += input("Palabra 2 --> ")
    palbras += input("Palabra 3 --> ")
    palbras += input("Palabra 4 --> ")
    palbras += input("Palabra 5 --> ")
    print("Estas suman " + str(len(palbras)) + " letras en total")
```
```powershell
Ingrese 5 palabras, para contar sus letras
Palabra 1 --> hola
Palabra 2 --> como
Palabra 3 --> estas?
Palabra 4 --> yo
Palabra 5 --> bien
Estas suman 20 letras en total
```

##### Ejercicio 31: Pedir el cuit que tiene la siguiente forma xx/dni/x. Extraer y mostrar el dni.
```Py
    print("Ingrese su cuit con la extructura xx/dni/x")
    cuit = str(input(" --> "))
    a = cuit.index("/") + 1
    b = cuit.index("/", a)
    print("Su DNI es :'" + cuit[a:b] + "'")
```
```powershell
Ingrese su cuit con la extructura xx/dni/x
 --> 00/38000000/0
Su DNI es :'38000000'
```

##### Ejercicio 32: Mostrar el código ASCII de los caracteres "A", "a" y "0"
```Py
    print("El codigo ASCII de 'A' es " + str(ord('A')))
    print("El codigo ASCII de 'a' es " + str(ord('a')))
    print("El codigo ASCII de '0' es " + str(ord('0')))
```
```powershell
El codigo ASCII de 'A' es 65
El codigo ASCII de 'a' es 97
El codigo ASCII de '0' es 48
```

##### Ejercicio 33: Pedir la cuenta de mail al usuario y mostrar por separado su usuario y su dominio.
```Py
    print("Por favor ingrese su mail")
    print("ejemplo: 'MyMail@ejemplo.com'")
    mail = input("Mail: --> ")
    print("Usuario: '" + mail[0:mail.index("@")] + "'")
    print("Dominio: '" + mail[mail.index("@")+ 1: len(mail)] + "'")
```
```powershell
Por favor ingrese su mail
ejemplo: 'MyMail@ejemplo.com'
Mail: --> javierb@gmail.com
Usuario: 'javierb'
Dominio: 'gmail.com'
```

[GitHub personal](https://github.com/JavierBalonga/Fundamentos-de-Informatica-UNAJ/)  
[Siguiente Unidad](https://github.com/JavierBalonga/Fundamentos-de-Informatica-UNAJ/tree/master/Unidad%20III)