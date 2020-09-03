![alt text](https://www.unaj.edu.ar/wp-content/uploads/2016/06/logo-unaj-2016-01.jpg)
# Fundamentos de Informática

## Practica 4
---
### PARTE I : Aspectos Conceptuales
#### 1. ¿Qué son las sentencias condicionales? ¿Para qué se utilizan?
Una sentencia condicional es una estructura de control, donde si se cumpliera una condicion, se puede ejecutar un bloque de instrucciones u otro, y se utilizan para controlar el flujo del programa dotandolo de mas inteligencia y asi que no sea una simple ejecucion secuencial.
#### 2. ¿Qué tipo de dato hay en la condición? ¿Como haría si se necesita evaluar mas de una condición?
En la condicion el dato que se evaluea es un booleano, que puede ser solo verdadero o falso, si se necesita de evaluar mas una condicion se puede usar los operadores logicos `or` y `and`
#### 3. ¿Cómo se sabe que sentencias deben ejecutarse si la condición se cumple?
Si la condicion se sumple las sentencias a ejecutarse deben identarse armando un bloque nuevo
#### 4. Si utilizo una sentencia if,
#### ¿Cuántas sentencias elif puede tener? ¿Qué condiciones deben cumplir?
Se puede agragar tantas sentencias `elif` como se quiera, siempre que se aplique bien la identacion para respetar los bolques, la sentencia `elif` debe tener la misma identacion que el `if`
#### ¿Cuántas sentencias else puede tener?¿Se puede ubicar en cualquier lugar?
Una, debe ubicarse debajo del `if` o del ultimo `elif` con la misma identacion que estos
#### 5. ¿Se puede tener dentro de una sentencia if, otra sentencia if? ¿Y dentro del else?
Si, y tambien, en ambos casos hay que declararlas en su respectivo bloque
---
### PARTE II: Ahora practicamos
#### Ejercicio 1: Escribir un programa que lee un número ingresado por el usuario en pantalla y muestre si es positivo, negativo o cero
```py
print("Ingrese un numero por favor")
print("Para ver si es positivo, negativo o cero")
num = int(input())
if (num > 0):
    print(str(num) + " es un numero positivo")
elif (num < 0):
    print(str(num) + " es un numero negativo")
else: print(str(num) + " es cero")
```
```powershell
Ingrese un numero por favor
Para ver si es positivo, negativo o cero
2
2 es un numero positivo
```
#### Ejercicio 2: ​Escribir un programa que me indique si un número es divisible por 6
```py
print("Ingrese un numero por favor")
print("Para ver si es divisible por 6")
num = int(input())
if(num % 6 == 0):
    print(str(num) + " es divisible por 6")
else:
    print(str(num) + " no es divisible por 6")
```
```powershell
Ingrese un numero por favor
Para ver si es divisible por 6
12
12 es divisible por 6
```
#### Ejercicio 3: Escribir un programa que lea dos números “n” y “m” y determine si m es divisible por n.
```py
print("Ingrese un numerador y un divisor para ver si estos son divisibles")
n = int(input("Numerador --> "))
m = int(input("Divisor --> "))
if(n % m == 0):
    print(str(n) + " es divisible por " + str(m))
else:
    print(str(n) + " no es divisible por " + str(m))
```
```powershell
Ingrese un numerador y un divisor para ver si estos son divisibles
Numerador --> 5
Divisor --> 4
5 no es divisible por 4
```
#### Ejercicio 4: Diseñar un programa que dado un número de 1 a 7 determine el día de la semana que representa:  
#### 1- Domingo a 7 – Sábado.  
#### ¿Qué pasa si ingreso un número mayor que 7?
```py
print("Ingrese un numero del 1 al 7 coorespondiente al dia de la semana")
n = int(input("Numero --> ")) % 7
if(n == 0): print("Sábado")
elif(n == 1): print("Domingo")
elif(n == 2): print("Lunes")
elif(n == 3): print("Martes")
elif(n == 4): print("Miercoles")
elif(n == 5): print("Jueves")
elif(n == 6): print("Viernes")
```
```powershell
Ingrese un numero del 1 al 7 coorespondiente al dia de la semana
Numero --> 3
Martes
```
#### Ejercicio 5: ​Dada la siguiente tabla
Transporte|#Pasajeros
----------|----------
Bicicleta|1
Moto|2
Auto|4
Camioneta|12
Colectivo|40
Avión|200
#### Escribir un programa que dada la cantidad de personas a viajar, determine el medio de transporte
```py
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
```
```powershell
Ingrese la cantidad de pasajeros a viajar
Para determinar el medio de transporte
cantidad de pasajeros: 20
Colectivo
```
#### Ejercicio 6: Desarrollar un programa en el ingrese un año de nacimiento y me indique si la persona es bebé, menor, adolescente, adulto, veterano, abuelo
Tipo|Edad
----|----
Bebé|< 2 años
Menor|> 2 y <=12
Adolescente|>12 y <=18
Adulto|>18 y <=45
Veterano|>45 y <=60
Abuelo|>60
```py
print("Ingrese su año de nacimiento")
edad = 2020 - int(input("Año nacimiento: "))
if(edad < 2): print("Usted es un Bebé !!!???")
elif(edad <= 12): print("Menor")
elif(edad <= 18): print("Adolescente")
elif(edad <= 45): print("Adulto")
elif(edad <= 60): print("Veterano")
else: print("Abuelo")
```
```powershell
Ingrese su año de nacimiento
Año nacimiento: 1994
Adulto
```
#### Ejercicio 7: ​Dada la siguiente tabla
Sexo|Altura (cm)|Clasificacion
----|-----------|-------------
Femenino|< 145 cm|Petisa
Femenino|>145 y <170|Normal
Femenino|>170|Alta
Masculino|<160 cm|Petisa
Masculino|>160 y <190|Normal
Masculino|> 190|Alta
#### Escriba un programa que, leyendo del teclado los valores de sexo y altura, determine si es una persona petisa, normal o alta.
```py
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
```
```powershell
Ingrese su sexo biologico y altura
Sexo --> Masculino
Altura(cm) --> 175
Que Haces flaco! tenes una estatura Normal
```
#### Ejercicio 8: Diseña un programa que, dado un número entero, determine si éste es el doble de un número impar. (Ejemplo: 14 es el doble de 7, que es impar.)
```py
print("Ingrese un numero entero para ver si éste es el doble de un número impar")
num = int(input("Numero --> "))
if(num % 2 == 0 and not num % 4 == 0):
    print(str(num) + " es el doble de un número impar")
else:
    print(str(num) + " no es el doble de un número impar")
```
```powershell
Ingrese un numero entero para ver si éste es el doble de un número impar
Numero --> 14
14 es el doble de un número impar
```
#### Ejercicio 9: Diseñar un programa que dado un carácter imprima en pantalla si es una letra, un dígito, un carácter especial u otro tipo de carácter.
```py
print("Ingrese un caracter para ser clasificado")
caracter = str(input("caracter --> "))
caracter = caracter[0]
if(caracter.isalpha()): print(caracter + " es una letra")
elif(caracter.isdecimal()): print(caracter + " es una dígito")
else: print(caracter + " es un carácter especial u otro tipo de carácter")
```
```powershell
Ingrese un caracter para ser clasificado
caracter --> a
a es una letra
```
#### Ejercicio 10: Dadas 3 longitudes, decir mediante un mensaje si se forma o no un triángulo (cada lado tiene que ser menor que la suma de los otros dos)
```py
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
    print("Genial con esos lados se puede formar un triangulo")
```
```powershell
Ingrese el largo de los 3 lados de un triangulo
Lado 1 --> 10
Lado 2 --> 5
Lado 3 --> 4
Con esos lados no se forma un triangulo!
```
#### Ejercicio 11: Diseña un programa Python que lea un carácter cualquiera desde el teclado, y muestre el mensaje @Es una MAYÚSCULA cuando el carácter sea una letra mayúscula y @Es una MINÚSCULA cuando sea una minúscula. En cualquier otro caso, no mostrará mensaje alguno. (Considera únicamente letras del alfabeto)  
#### Pista​: aunque parezca una obviedad, recuerda que una letra es minúscula si está entre la ’a’ y la ’z’, y mayúscula si está entre la ’A’ y la ’Z’.
```py
print("Ingrese un caracter del alfabeto")
char = str(input("Caracter --> "))[0]
if (char.isalpha()):
    if(char.isupper()):
        print(char + " es una MAYÚSCULA")
    else:
        print(char + " es una MINÚSCULA")
```
```powershell
Ingrese un caracter del alfabeto
Caracter --> A
A es una MAYÚSCULA
```
#### Ejercicio 12: Escribir un programa que dado un año determine si es bisiesto o no. Un año es bisiesto si es múltiplo de 4 (por ejemplo 1984). Los años múltiplos de 100 no son bisiestos, salvo si ellos son también múltiplos de 400 (2000 es bisiesto, pero 1800 no lo es).
```py
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
```
```powershell
Ingrese un año para saber si es bisiesto
Año --> 2000
2000 es un año bisiesto
```
#### Ejercicio 13: Dado la duración (en segundos) de una llamada telefónica, calcular su costo, de la siguiente manera: El primer minuto $1,10, luego $0,25 cada fracción de 15 segundos (un cuarto de minuto).
```py
print("Cuanto duro la llamada telefónica?")
seg = int(input("Duracion(seg) -->"))
if(seg < 60): 
    print("El costo de la llamada es de $1,10")
else:
    print("El costo de la llamada es de $" + str(1.10 + ((seg - 60) // 15) * 0.25))
```
```powershell
Cuanto duro la llamada telefónica?
Duracion(seg) -->600
El costo de la llamada es de $10.1
```
#### Ejercicio 14: Calcular el número de pulsaciones que una persona debe tener por cada 10 segundos de ejercicio aeróbico; la fórmula que se aplica cuando el sexo es femenino es: (220-edad)/10; si el sexo es masculino es: (210-edad)/10.
```py
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
```
```powershell
Cual es sexo biologico y Edad?
Sexo --> Masculino
Edad --> 26
Su ritmo cardiaco durante los ejercicios aeróbicos de de ser de18.4 cada 10seg
```
[GitHub personal](https://github.com/JavierBalonga/Fundamentos-de-Informatica-UNAJ/)  
[Siguiente Unidad](https://github.com/JavierBalonga/Fundamentos-de-Informatica-UNAJ/tree/master/Unidad%20V)