![alt text](https://www.unaj.edu.ar/wp-content/uploads/2016/06/logo-unaj-2016-01.jpg)
# Fundamentos de Informática

## Practica 5
---
### Parte I : Aspectos Conceptuales
#### a) ¿Que estructuras de control conoce? ¿En qué se diferencian?
Conozco en lo que va de la materia los condicionales, los bucles `while` y los `for`.  
Un condicional es una estructura de control cuya logica es la de: **Si se cumple la ***condicion*** ejecuta este bloque de instrucciones, ***sino*** ejecuta este otro bloque**.
Un Bucle `while` es la iteracion de un bloque de instrucciones **mientras** se siga cumpliendo una condicion.
Y un bucle `for` es la iteracion de un bloque de instrucciones para todos los elementos de una estructura de datos iterable.
#### b) ¿Qué tipo de sentencias puedo escribir dentro del cuerpo de una estructura de control?
Las que quiera mientras siga respetando la forma de escritura de python, y tenga los recaudos para no meterme en una iteracion infinita.
#### c) ¿Se puede escribir una estructura de control dentro de otra?
Si, pero hay que tener los recudos suficientes para no meterse en un codigo demasiado lento o que pueda tener iteraciones infinitas.
---
### Parte II: Ahora practicamos
#### Ejercicio 1: Escribir un programa que muestre la tabla de multiplicar de un número introducido por teclado por el usuario.
```py
print("Ingrese un numero para mostrar su tabla de multiplicar")
num = int(input("Numero --> "))
for i in range(11):
    print(str(num) + " * " + str(i) + " = " + str(num * i))
```
```powershell
Ingrese un numero para mostrar su tabla de multiplicar
Numero --> 2
2 * 0 = 0
2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
2 * 6 = 12
2 * 7 = 14
2 * 8 = 16
2 * 9 = 18
2 * 10 = 20
```
#### Ejercicio 2: Escribir un programa que calcule la sumatoria desde 0 hasta m, donde m es un número introducido por el usuario desde el teclado.
```py
print("Ingrese un numero para calcular la sumatoria de 0 hasta dicho numero")
num = int(input("Numero --> "))
suma = 0
for i in range(num + 1):
    suma += i
print("La sumatoria da " + str(suma))
```
```powershell
Ingrese un numero para calcular la sumatoria de 0 hasta dicho numero
Numero --> 7
La sumatoria da 28
```
#### Ejercicio 3: Escribir un programa que muestre la tabla de los códigos ASCII. Los códigos ASCII van de 0 a 255
```py
texto = ""
for i in range(256):
    if(i % 10 == 0): texto += "\n"
    texto += str(i) + "=" + "'" + chr(i) + "' | "
print(texto)
```
```powershell

0='' | 1='╔' | 2='╗' | 3='╚' | 4='╝' | 5='║' | 6='═' | 7='' | 8=' | 9='        ' |
10='
' | 14='' | 15='' | 16='' | 17='' | 18='' | 19='' |
20='' | 21='' | 22='' | 23='' | 24='' | 25='' | 26='' | 27='?' | 28='' | 29='' |
30='' | 31='' | 32=' ' | 33='!' | 34='"' | 35='#' | 36='$' | 37='%' | 38='&' | 39=''' |
40='(' | 41=')' | 42='*' | 43='+' | 44=',' | 45='-' | 46='.' | 47='/' | 48='0' | 49='1' |
50='2' | 51='3' | 52='4' | 53='5' | 54='6' | 55='7' | 56='8' | 57='9' | 58=':' | 59=';' |
60='<' | 61='=' | 62='>' | 63='?' | 64='@' | 65='A' | 66='B' | 67='C' | 68='D' | 69='E' |
70='F' | 71='G' | 72='H' | 73='I' | 74='J' | 75='K' | 76='L' | 77='M' | 78='N' | 79='O' |
80='P' | 81='Q' | 82='R' | 83='S' | 84='T' | 85='U' | 86='V' | 87='W' | 88='X' | 89='Y' |
90='Z' | 91='[' | 92='\' | 93=']' | 94='^' | 95='_' | 96='`' | 97='a' | 98='b' | 99='c' |
100='d' | 101='e' | 102='f' | 103='g' | 104='h' | 105='i' | 106='j' | 107='k' | 108='l' | 109='m' |
110='n' | 111='o' | 112='p' | 113='q' | 114='r' | 115='s' | 116='t' | 117='u' | 118='v' | 119='w' |
120='x' | 121='y' | 122='z' | 123='{' | 124='|' | 125='}' | 126='~' | 127='' | 128='' | 129='' |
130='' | 131='' | 132='
                       ' | 133='
' | 134='' | 135='' | 136='' | 137='' | 138='' | 139='' |
140='' | 141='' | 142='' | 143='' | 144='' | 146='' | 147='' | 148='' | 149='' |
150='' | 151='' | 152='' | 154='' | 155=' 156='' | 157='
160=' ' | 161='¡' | 162='¢' | 163='£' | 164='¤' | 165='¥' | 166='¦' | 167='§' | 168='¨' | 169='©' |
170='ª' | 171='«' | 172='¬' | 173='­' | 174='®' | 175='¯' | 176='°' | 177='±' | 178='²' | 179='³' |
180='´' | 181='µ' | 182='¶' | 183='·' | 184='¸' | 185='¹' | 186='º' | 187='»' | 188='¼' | 189='½' |
190='¾' | 191='¿' | 192='À' | 193='Á' | 194='Â' | 195='Ã' | 196='Ä' | 197='Å' | 198='Æ' | 199='Ç' |
200='È' | 201='É' | 202='Ê' | 203='Ë' | 204='Ì' | 205='Í' | 206='Î' | 207='Ï' | 208='Ð' | 209='Ñ' |
210='Ò' | 211='Ó' | 212='Ô' | 213='Õ' | 214='Ö' | 215='×' | 216='Ø' | 217='Ù' | 218='Ú' | 219='Û' |
220='Ü' | 221='Ý' | 222='Þ' | 223='ß' | 224='à' | 225='á' | 226='â' | 227='ã' | 228='ä' | 229='å' |
230='æ' | 231='ç' | 232='è' | 233='é' | 234='ê' | 235='ë' | 236='ì' | 237='í' | 238='î' | 239='ï' |
240='ð' | 241='ñ' | 242='ò' | 243='ó' | 244='ô' | 245='õ' | 246='ö' | 247='÷' | 248='ø' | 249='ù' |
250='ú' | 251='û' | 252='ü' | 253='ý' | 254='þ' | 255='ÿ' |
```
#### Ejercicio 4: Escribir un programa que lea letras del teclado indefinidamente hasta que el usuario ingrese “fin” e imprima el código ASCII de las mismas.
```py
print("Ingrese la letra que usted guste para ver su codigo ASCII")
print("O use 'fin' para salir")
fin = False
while(not fin):
    fin = False
    letras = str(input("Letra -->"))
    if (letras == "fin"): fin = True
    else: 
        codigos = ""
        for letra in letras:
            codigos += str(ord(letra)) + ","
        print(codigos)
```
```powershell
Ingrese la letra que usted guste para ver su codigo ASCII
O use 'fin' para salir
Letra -->a
97,
Letra -->A
65,
Letra -->B
66,
Letra -->askldnalskdnlak\
97,115,107,108,100,110,97,108,115,107,100,110,108,97,107,92,
Letra -->fin
```
#### Ejercicio 5: Escribir un programa que calcule el promedio de N números ingresados por el usuario. (AYUDA: al comenzar el programa debe preguntar la cantidad de números a ingresar, luego iterar y leer tantos números del teclado como se indicó al inicio.)
```py
print("Cuantos numeros desa promediar?")
cantidad = int(input("Cantidad --> "))
suma = 0
for i in range(cantidad):
    suma += float(input("Numero " + str(i + 1) + " --> "))
print("El promedio es de " + str(suma / cantidad))
```
```powershell
Cuantos numeros desa promediar?
Cantidad --> 5
Numero 1 --> 6
Numero 2 --> 7
Numero 3 --> 8
Numero 4 --> 9
Numero 5 --> 6
El promedio es de 7.2
```
#### Ejercicio 6: Escriba un programa que lea nombres de personas hasta que se ingrese el nombre “zzz”. Debe imprimir la cantidad de nombres que comienzan con “A”.
```py
print("Ingrese tantos nombres como guste")
print("Solo los nombres que comienzan con 'A' seran contabilizados")
print("Use 'zzz' al finalizar")
cantNombresA = 0
zzz = False
while(not zzz):
    zzz = False
    Nombre = str(input("Nombre --> "))
    if(Nombre == "zzz"): zzz = True
    elif(Nombre[0] == "A" or Nombre[0] == "a"): cantNombresA += 1
print("Hay " + str(cantNombresA) + " que comienzan con 'A'")
```
```powershell
Ingrese tantos nombres como guste
Solo los nombres que comienzan con 'A' seran contabilizados
Use 'zzz' al finalizar
Nombre --> Alejandro
Nombre --> Adrian
Nombre --> alfredo
Nombre --> javier
Nombre --> hernan
Nombre --> zzz
Hay 3 que comienzan con 'A'
```
#### Ejercicio 7: Escriba un programa que lea números de documentos de identidad de personas hasta que se ingrese el número “999”. Debe imprimir la cantidad de números de documentos menores que 20.000.000.
```py
print("Ingrese numeros de documentos de identidad")
print("Solo los numeros de documentos menores a 20.000.000 seran contabilizados")
print("Use '999' al finalizar")
cantDNI = 0
exit = False
while(not exit):
    exit = False
    DNI = int(input("DNI --> ").replace(".",""))
    if(DNI == 999): exit = True
    elif(DNI < 20000000): cantDNI += 1
print("Hay " + str(cantDNI) + " DNIs menores a 20.000.000")
```
```powershell
Ingrese numeros de documentos de identidad
Solo los numeros de documentos menores a 20.000.000 seran contabilizados
Use '999' al finalizar
DNI --> 38000000
DNI --> 19000000
DNI --> 999
Hay 1 DNIs menores a 20.000.000
```
#### Ejercicio 8: Escriba un programa que reciba del usuario su nombre, apellido y patente hasta que ingrese AAA, e imprima si está exento de impuesto o no. Tener en cuenta que los autos cuyas patentes empiezan con R, S y T no deben pagar impuesto.
```py
print("Ingrese nombre, apellido y patente o use 'AAA' para finalizar")
print("Hagalo con la siguiente estructura:")
print(" --> Nombre,Apellido,Patente")
Usuarios = []
exit = False
while(not exit):
    exit = False
    Usuario = str(input(" --> "))
    if(Usuario == "AAA"): exit = True
    else:
        Usuario = Usuario.split(",")
        Usuario[0] = ((Usuario[0].replace(" ", "")).lower()).capitalize()
        Usuario[1] = ((Usuario[1].replace(" ", "")).lower()).capitalize()
        Usuario[2] = (Usuario[2].replace(" ", "")).upper()
        if (Usuario[2][0] == "R" or Usuario[2][0] == "S" or Usuario[2][0] == "T"):
            Usuario.append(False)
        else:
            Usuario.append(True)
        Usuarios.append(Usuario)
print("       Nombre       |      Apellido      |      Patente       |      Impuesto      ")
print("--------------------|--------------------|--------------------|--------------------")
for u in Usuarios:
    texto = u[0].center(20) + "|" + u[1].center(20) + "|" + u[2].center(20) + "|"
    if (u[3]):
        texto += ("Imponible").center(20)
    else:
        texto += ("Exento").center(20)
    print(texto)
```
```powershell
       Nombre       |      Apellido      |      Patente       |      Impuesto
--------------------|--------------------|--------------------|--------------------
       Javier       |      Balonga       |       RSW666       |       Exento
      Gabriel       |       Perez        |       AJK999       |     Imponible
```
#### Ejercicio 9: Escriba un programa que solicite códigos postales de localidades e imprima si esa localidad es La Plata, Florencio Varela u otra. Recordar que el código postal de La Plata es 1900 y el de Florencio Varela es: 1887. El programa termina cuando se ingresa el código postal 0.
```py
codigosPostales = [
    [1160,'Buenos Aires'], [1161,'Buenos Aires'], [1439,'Tapiales'], [1607,'Villa Adelina'], [1611,'Don Torcuato'],
    [1625,'Belen de Escobar'], [1629,'Pilar (Buenos Aires)'], [1633,'Fatima (Buenos Aires)'], [1638,'Vicente Lopez'],
    [1640,'Martinez (Buenos Aires)'], [1642,'San Isidro (Buenos Aires)'], [1643,'Beccar'], [1664,'San Miguel (Buenos Aires)'],
    [1704,'Ramos Mejia'], [1708,'Moron (Buenos Aires)'], [1712,'Castelar'], [1723,'Mariano Acosta (Buenos Aires)'],
    [1727,'Marcos Paz (Buenos Aires)'], [1761,'Pontevedra (Buenos Aires)'], [1804,'Ezeiza'], [1806,'Tristan Suarez'],
    [1812,'Tristan Suarez'], [1842,'Esteban Echeverria'], [1875,'Wilde (Buenos Aires)'], [1878,'Quilmes'], [1886,'Ranelagh'],
    [1887,'Florencio Varela'], [1889,'Ranelagh'], [1894,'Pereyra'], [1900,'La Plata'], [1925,'Gonnet (La Plata)'],
    [2705,'Rojas (Argentina)'], [2720,'Colon'], [6015,'General Viamonte'], [6455,'Carlos Tejedor'], [6612,'Suipacha (Buenos Aires)'],
    [6700,'Jose Maria Jauregui'], [6720,'San Andres de Giles'], [7000,'Tandil'], [7130,'Ciudad de Chascomus'], [7167,'Pinamar'],
    [7414,'Laprida (provincia de Buenos Aires)'], [7521,'San Cayetano (Buenos Aires)'], [7600,'Sierra de los Padres'],
    [8000,'Bahia Blanca'], [8153,'Monte Hermoso']
]
print("Ingrese codigos postales para averiguar la localidad")
print("Use '0' al finalizar")
exit = False
while(not exit):
    exit = False
    codigo = int(input("Codigos Postal  --> "))
    if(codigo == 0): exit = True
    else:
        for cod in codigosPostales:
            if (cod[0] == codigo):
                print("Localidad: " + cod[1])
                break
```
```powershell
Ingrese codigos postales para averiguar la localidad
Use '0' al finalizar
Codigos Postal  --> 1886
Localidad: Ranelagh
Codigos Postal  --> 1900
Localidad: La Plata
Codigos Postal  --> 1887
Localidad: Florencio Varela
Codigos Postal  --> 1160
Localidad: Buenos Aires
Codigos Postal  --> 0
```
#### Ejercicio 10​: Definir una función que imprima los primeros cien números enteros. ¿Se le ocurre otra forma de hacerlo?
```py
def primeros_cien_numeros_enteros():
    texto = ""
    for i in range(100):
        texto += str(i) + "\t"
    print(texto)
primeros_cien_numeros_enteros()
```
Si Tambien se puede hacer con un bucle `while`
```powershell
0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51  52  53  54  55  56  57  58  59  60  61  62  63  64  65  66  67  68  69  70  71  72  73  74  75  76  77  78  79  80  81  82  83  84  85  86  87  88  89  90  91  92  93  94  95  96  97  98  99
```
#### Ejercicio 11​: Implementar una función que muestre todos los múltiplos de n entre n y m.  
#### ambos inclusive, donde n y m son parámetros de la función.
```py
def multiplosDe(n, m):
    print("Los multiplos de " + str(n) + " entre " + str(n) + " y " + str(m) + " son:")
    i = 1
    multiplo = 0
    texto = ""
    while (multiplo <= m):
        multiplo = i * n
        texto += str(multiplo) + "\t"
        i += 1
    print(texto)
multiplosDe(2, 100)
```
```powershell
Los multiplos de 2 entre 2 y 100 son:
2   4   6   8   10  12  14  16  18  20  22  24  26  28  30  32  34  36  38  40  42  44  46  48  50  52  54  56  58  60  62  64  66  68  70  72  74  76  78  80  82  84  86  88  90  92  94  96  98  10  01  02
```
---
### Parte III: Ahora practicamos con Colecciones
#### Ejercicio 12: Dada la siguiente lista [1, 14, 56, 43, 23, 46, 58, 123, 67] escribir un programa que muestre el número más alto.
```py
list = [1, 14, 56, 43, 23, 46, 58, 123, 67]
print("Dada la siguiente lista:")
print(list)
max = list[0]
for element in list:
    if (max < element): max = element
print("el numero mas alto es " + str(max))
```
```powershell
Dada la siguiente lista:
[1, 14, 56, 43, 23, 46, 58, 123, 67]
el numero mas alto es 123
```
#### Ejercicio 13: Escriba un programa que solicite nombres de localidades y códigos postales al usuario hasta que se ingresa el código postal 0. Debe generar una lista con todos los valores ingresados e imprimirla.
```py
print("Ingrese localidades y codigos postales para agregar a la lista, o use '0' al finalizar")
print("Por ejemplo:")
print(" --> 1160,Buenos Aires")
codigosPostales = []
exit = False
while(not exit):
    exit = False
    codigo = str(input(" --> "))
    if(codigo == "0"): exit = True
    else:
        codigo = codigo.split(",")
        codigo[0] = int(codigo[0])
        codigosPostales.append(codigo)
print("Codigo postal|          Localidad           ")
print("-------------|------------------------------")
for c in codigosPostales:
    texto = (str(c[0])).center(13) + "|" + c[1].center(30)
    print(texto)
```
```powershell
Ingrese localidades y codigos postales para agregar a la lista, o use '0' al finalizar
Por ejemplo:
 --> 1160,Buenos Aires
 --> 1886,Ranelagh
 --> 1887,Florencio Varela
 --> 0
Codigo postal|          Localidad
-------------|------------------------------
     1886    |           Ranelagh
     1887    |       Florencio Varela
```
#### Ejercicio 14: ​Realice un programa para manejar equipos de fútbol.
##### a) Definir una función que arme una lista con la información de los equipos. De cada equipo se quiere guardar el nombre del equipo, puntaje en la tabla de posiciones y la cantidad de goles a favor. El ingreso finaliza cuando se lee el nombre del equipo igual a ‘ZZZ’.
##### b) Usando la lista anterior, imprimir la cantidad de goles a favor que tienen los equipos que están en la primera y última posición de la lista.
##### c) ​Imprimir el nombre del equipo Campeón de la lista del ejercicio anterior.
```py
equipos = []
def armar_lista_equipos():
    print("Ingrese cada equipo de futbol, con us datos separados por ','")
    print("Al terminar use 'ZZZ' para terminar la lista")
    print(" --> Equipo,Puntaje,Goles")
    exit = False
    while(not exit):
        exit = False
        equipo = str(input(" --> "))
        if(equipo == "ZZZ"): exit = True
        else:
            equipo = equipo.split(",")
            equipo[1] = int(equipo[1])
            equipo[2] = int(equipo[2])
            equipos.append(equipo)
    ordenado = False
    while(not ordenado):
        ordenado = True
        for i in range(len(equipos) - 1):
            if(equipos[i][1] > equipos[i + 1][1]):
                aux = equipos[i]
                equipos[i] = equipos[i+1]
                equipos[i+1] = aux
                ordenado = False

def imprimir_goles_primera_y_ultima():
    print("            Equipo            |  Goles   ")
    print("------------------------------|----------")
    print(equipos[0][0].center(30) + "|" + str(equipos[0][2]).center(10))
    print(equipos[len(equipos)-1][0].center(30) + "|" + str(equipos[len(equipos)-1][2]).center(10))

def imprimir_equipo_campeon():
    print(equipos[len(equipos)-1][0] + " es el campeon!")

exit = False
while(not exit):
    exit = False
    print("Menu:")
    print("1- Armar lista de equipos")
    print("2- Imprimir goles del primer y ultimo equipo de la tabla")
    print("3- Imprimir equipo campeon")
    print("4- Salir")
    op = int(input(" --> "))
    if(op == 1): armar_lista_equipos()
    elif(op == 2): imprimir_goles_primera_y_ultima()
    elif(op == 3): imprimir_equipo_campeon()
    elif(op == 4): exit = True
```
```powershell
Menu:
1- Armar lista de equipos
2- Imprimir goles del primer y ultimo equipo de la tabla
3- Imprimir equipo campeon
4- Salir
 --> 1
Ingrese cada equipo de futbol, con us datos separados por ','
Al terminar use 'ZZZ' para terminar la lista
 --> Equipo,Puntaje,Goles
 --> Boca,100,7
 --> River,200,13
 --> Estudiantes,75,6
 --> ZZZ
Menu:
1- Armar lista de equipos
2- Imprimir goles del primer y ultimo equipo de la tabla
3- Imprimir equipo campeon
4- Salir
 --> 2
            Equipo            |  Goles
------------------------------|----------
         Estudiantes          |    6
            River             |    13
Menu:
1- Armar lista de equipos
2- Imprimir goles del primer y ultimo equipo de la tabla
3- Imprimir equipo campeon
4- Salir
 --> 3
River es el campeon!
Menu:
1- Armar lista de equipos
2- Imprimir goles del primer y ultimo equipo de la tabla
3- Imprimir equipo campeon
4- Salir
 --> 4
```
---
### Parte IV: Ahora practicamos con menús
#### Ejercicio 15: ​Escriba un programa que le solicite al usuario que elija una opción del siguiente menú y, de acuerdo a la opción elegida, le solicite los datos restantes para imprimir el área de la figura elegida:
> Menú de opciones
> 1.- Círculo
> 2.- Cuadrado
> 3.- Rectángulo
```py
    def area_circulo():
        print("Inserte el diametro")
        diam = float(input("Diametro --> "))
        print("Su area es de " + str(diam ** 2 * 3.14159265359))

    def area_cuadrado():
        print("Ingrese la distancia del lado")
        lado = float(input("Lado --> "))
        print("Su area es de " + str(lado ** 2))

    def area_rectangulo():
        print("Ingrese la ditancia de sus lados")
        lado1 = float(input("Lado 1 --> "))
        lado2 = float(input("Lado 2 --> "))
        print("Su area es de " + str(lado1 * lado2))

    exit = False
    while(not exit):
        exit = False
        print("Menu de opciones")
        print("El area de que figura geometrica desea calcular")
        print("1.- Circulo")
        print("2.- Cuadrado")
        print("3.- Rectangulo")
        print("4- Salir")
        op = int(input(" --> "))
        if(op == 1): area_circulo()
        elif(op == 2): area_cuadrado()
        elif(op == 3): area_rectangulo()
        elif(op == 4): exit = True
```
```powershell
Menu de opciones
El area de que figura geometrica desea calcular
1.- Circulo
2.- Cuadrado
3.- Rectangulo
4- Salir
 --> 1
Inserte el diametro
Diametro --> 20
Su area es de 1256.637061436
Menu de opciones
El area de que figura geometrica desea calcular
1.- Circulo
2.- Cuadrado
3.- Rectangulo
4- Salir
 --> 2
Ingrese la distancia del lado
Lado --> 4
Su area es de 16.0
Menu de opciones
El area de que figura geometrica desea calcular
1.- Circulo
2.- Cuadrado
3.- Rectangulo
4- Salir
 --> 3
Ingrese la ditancia de sus lados
Lado 1 --> 5
Lado 2 --> 10
Su area es de 50.0
Menu de opciones
El area de que figura geometrica desea calcular
1.- Circulo
2.- Cuadrado
3.- Rectangulo
4- Salir
 --> 4
```
#### Ejercicio 16​: Escriba un programa que le solicite al usuario que ingrese un monto de dinero y una opción del siguiente menú. De acuerdo a la opción elegida, imprima cuanto equivale el monto en dólares, en euros y en reales. Utilizar las funciones ya definidas en el ejercicio 14 de la práctica 3 (convertir_a_dolar, convertir_a_euro y convertir_a_real).
```py
    def funcion_convertir(tasaCambio):
        def nueva_funcion_convertir(pesos):
            return tasaCambio * pesos
        return nueva_funcion_convertir
    # Tasas de cambios segun el BNA 02/09/2020
    convertir_a_dolar = funcion_convertir(73.25)
    convertir_a_euro = funcion_convertir(84.00)
    convertir_a_real = funcion_convertir(1250.00)
    print("Ingrese un monto en pesos")
    pesos = float(input("Monto --> "))
    print("A que moneda quiere hacer la conversion")
    print("1.- Dolar")
    print("2.- Euro")
    print("3.- Real")
    op = int(input("Opcion --> "))
    if(op == 1): print("Son " + str(convertir_a_dolar(pesos)) + " Dolares")
    if(op == 2): print("Son " + str(convertir_a_euro(pesos)) + " Euro")
    if(op == 3): print("Son " + str(convertir_a_real(pesos)) + " Real")
```
```powershell
Ingrese un monto en pesos
Monto --> 100
A que moneda quiere hacer la conversion
1.- Dolar
2.- Euro
3.- Real
Opcion --> 1
Son 7325.0 Dolares
```
#### Ejercicio 17​:
##### a) Definir una función que permita el ingreso de números por teclado hasta ingresar el 0, y retorne esa lista.
```py
    def ingreso_de_numeros():
        print("Ingrese los numeros a enlistar")
        numeros = []
        exit = False
        while(not exit):
            exit = False
            num = float(input("Numero --> "))
            if (num == 0): exit = True
            else:
                numeros.append(num)
        return numeros
```
##### b) Definir una función que reciba como parámetro una lista de números y retorne como resultado el promedio.
```py
    def promedio(numeros):
        if(len(numeros) != 0):
            suma = 0
            for num in numeros:
                suma += num
            return suma / len(numeros)
        else: return 0
```
##### c) Definir una función que reciba como parámetro una lista de números y retorne como resultado la suma de los números.
```py
    def sumatoria(numeros):
        suma = 0
        for num in numeros:
            suma += num
        return suma
```
##### d) Definir una función que reciba como parámetro una lista de números y retorne el número más grande de la lista (máximo).
```py
    def maximo(numeros):
        maxi = numeros[0]
        for num in numeros:
            if(maxi < num): maxi = num
        return maxi
```
##### e) Definir una función que reciba como parámetro una lista de números y retorne el número más pequeño de la lista (mínimo).
```py
    def minimo(numeros):
        mini = numeros[0]
        for num in numeros:
            if(mini > num): mini = num
        return mini
```
##### Utilizar las funciones definidas anteriormente para construir un programa que permita elegir
##### una opción del siguiente menú:
> 1. Ver el promedio de los números
> 2. Ver la suma de los números
> 3. Ver la cantidad de números
> 4. Ver el número máximo
> 5. Ver el número mínimo
```py
    print("*********     Menu     **********")
    print("1. Ingreso de numeros")
    print("2. Ver el promedio de los numeros")
    print("3. Ver la suma de los numeros")
    print("4. Ver la cantidad de numeros")
    print("5. Ver el numero maximo")
    print("6. Ver el numero minimo")
    print("7. Exit")
    numeros = []
    exit = False
    while(not exit):
        exit = False
        op = int(input("Opcion --> "))
        if(op == 1): numeros = ingreso_de_numeros()
        elif(op == 2): promedio(numeros)
        elif(op == 3): sumatoria(numeros)
        elif(op == 4): len(numeros)
        elif(op == 5): maximo(numeros)
        elif(op == 6): minimo(numeros)
        elif(op == 7): exit = True
```
```powershell
*********     Menu     **********
1. Ingreso de numeros
2. Ver el promedio de los numeros
3. Ver la suma de los numeros
4. Ver la cantidad de numeros
5. Ver el numero maximo
6. Ver el numero minimo
7. Exit
Opcion --> 1
Ingrese los numeros a enlistar
Numero --> 3
Numero --> 5
Numero --> 4
Numero --> 7
Numero --> 9
Numero --> 0
*********     Menu     **********
1. Ingreso de numeros
2. Ver el promedio de los numeros
3. Ver la suma de los numeros
4. Ver la cantidad de numeros
5. Ver el numero maximo
6. Ver el numero minimo
7. Exit
Opcion --> 2
El promedio es 5.6
*********     Menu     **********
1. Ingreso de numeros
2. Ver el promedio de los numeros
3. Ver la suma de los numeros
4. Ver la cantidad de numeros
5. Ver el numero maximo
6. Ver el numero minimo
7. Exit
Opcion --> 3
La suma es 28.0
*********     Menu     **********
1. Ingreso de numeros
2. Ver el promedio de los numeros
3. Ver la suma de los numeros
4. Ver la cantidad de numeros
5. Ver el numero maximo
6. Ver el numero minimo
7. Exit
Opcion --> 4
Hay 5 numeros.
*********     Menu     **********
1. Ingreso de numeros
2. Ver el promedio de los numeros
3. Ver la suma de los numeros
4. Ver la cantidad de numeros
5. Ver el numero maximo
6. Ver el numero minimo
7. Exit
Opcion --> 5
El maximo es 9.0
*********     Menu     **********
1. Ingreso de numeros
2. Ver el promedio de los numeros
3. Ver la suma de los numeros
4. Ver la cantidad de numeros
5. Ver el numero maximo
6. Ver el numero minimo
7. Exit
Opcion --> 6
El minimo es 3.0
*********     Menu     **********
1. Ingreso de numeros
2. Ver el promedio de los numeros
3. Ver la suma de los numeros
4. Ver la cantidad de numeros
5. Ver el numero maximo
6. Ver el numero minimo
7. Exit
Opcion --> 7
```
[GitHub personal](https://github.com/JavierBalonga/Fundamentos-de-Informatica-UNAJ/)  