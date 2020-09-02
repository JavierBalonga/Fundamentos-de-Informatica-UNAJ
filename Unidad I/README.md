![alt text](https://www.unaj.edu.ar/wp-content/uploads/2016/06/logo-unaj-2016-01.jpg)
# Fundamentos de Informatica

## Practica 1
---
### PARTE I: Aspectos Conceptuales
##### Ejercicio 1: ¿Qué diferencias hay entre un lenguaje de máquina y uno de alto nivel?
El lenguaje de maquina o lenguajes ensambladores(asembler) es el lenguaje que la maquina puede interpretar y este varia segun el hardware que se use, dado que segun el procesador que l ejecute las instrucciones del mismo varian.
El lenguaje de alto nivel se caracteriza por expresarse de una manera adecuada para ser leida por una persona.

##### Ejercicio 2: ¿Qué ventajas tiene programar en un lenguaje de alto nivel? ¿Y desventajas?
Las ventajas que tiene estos lenguajes son enormes. En primer lugar, la programacíon en lenguajes de alto nivel es mucho mas facil.
Escribir programas en un lenguaje de alto nivel toma menos tiempo, los programas son mas cortos y mas faciles de leer, y es mas probable que estos programas sean correctos. En segundo lugar, los lenguajes de alto nivel son portables, lo que significa que pueden ejecutarse en tipos diferentes de computadores sin modificacion alguna o con pocas  modificaciones.
Las desventajas estan en dado que el computador solo puede ejecutar programas en lenguaje maquina, los lenguajes de alto nivel requieren de ser traducidos a  lenguaj de maquina antes de ser ejecutados.

##### Ejercicio 3: Necesito ejecutar un programa que me permite hacer gráficos estadísticos.
###### (a) Si el programa está escrito en lenguaje C++ (Lenguaje compilado), ¿necesito el compilador de C++?
Los Lenguajes compilados como `C++` requieren de que el **codigo fuente**(el que esta escrito en alto nivel) sea compilado a **codigo ejecutable**(el lenguaje de bajo nivel) en su totalidad antes de ser ejecutado, si el programa de este tipo **ya esta compilado** para ser trabajado en mi computador, **no requiere de ningun compilador**, pero si estuviera en estado de codigo fuente, primero deve de ser compilado y luego antes de ser ejecutado, en este caso si se requeriria del compilador.

###### (b) Si el programa está escrito en lenguaje Python (lenguaje interpretado), ¿necesito el intérprete de Python?
En un leguaje como `Python`(**lenguaje interpretado**) funcionan leyendo cada instruccion, traduciendola a bajo nivel y luego ejecutandola, por lo que siempre requiere de su **intérprete**.

##### Ejercicio 4: Según tu opinión, ¿qué ventajas tiene trabajar con software libre?
Por donde yo lo veo la mayor ventaja de trabjar en un **software libre** esta en la comunidad que esta genera, dado que sus desarrolladores no pusieron barreras al mismo, tampoco hay barreras para la gente que los usa, dado estas caracteristicas los lenguajes de software libre, generan una gran comunidad a su alrededor logrando que siempre haya foros y gente dispuesta enseñar y socorrer a un programador principiante, o incluso generando librerias de acceso publico contribuyendo a aque estos sean muy utiles.

##### Ejercicio 5:¿Qué es un IDE?
**IDLE (Integrated DeveLopment Environment)**
Un IDLE es un entorno gráfico que permite editar y ejecutar programas. No es un lenguaje. Este trae funciones extras como el auto completar código y el coloreado de la sintaxis del lenguaje, pero principalmente son editores de texto que permiten la ejecucion del codigo.

---
### PARTE II: Instalando

##### Instalación de las herramientas necesarias para trabajar. Si bien en las máquinas del gabinete están instaladas todas las herramientas necesarias para trabajar. Vamos a indicar cómo instalar las mismas en otros equipos (para que puedan contar con estas herramientas en otros ámbitos).
##### Ejercicio 6: Desde http://www.python.org, descargue la versión de Python acorde al sistema operativo de su equipo.
Yo a lo tenia instalado, tengo intalado **Anaconda**.

##### Ejercicio 7: Desde http://www.geany.org/ descargue el IDE Geany.
Yo estoy mas acostumbrado a usar **Visual Studio Code**.

##### Ejercicio 8: ¿Puede ejecutar Python desde cualquier directorio de su máquina? ¿Cómo verifica esto? Si no puede hacerlo, actualice lo necesario para que sea posible.
Si lo puedo ejecutar en cualquier lado ya sea con terminal o creando un archivo `.py`.

---
### PARTE III: Primeros pasos con Python
##### Desde el intérprete de Python
##### Ejercicio 9: Indique qué versión es la que tiene instalada en su máquina
```powershell
D:\Javi\Proyectos\Fundamentos de Informatica>python
Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:25:58) [MSC v.1500 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

##### Ejercicio 10: Ejecute las siguientes instrucciones:
###### a) Compare los resultados obtenidos de 2 y 3, de 4 y 5, de 6 y 7.
```powershell
>>> print ("hola Fundamentos")
hola Fundamentos
```

```powershell
>>> print (2 + 3)
5
>>> print ("2" + "3")
23
```
La ejecucion de la instruccion 2 se puede interpretar de la siguiente manera:
Sumar `2` mas `3`, y luego mostrarlo por consola, de esta manera el resultado es `5`.
Mientras la instruccion 3 es la siguiente:
Concatenar `"2"` y `"3"` y luego mostrarlo por consola, de esta manera el resultado es `23`.
Y esto ocurre porque se esta tratando de dos tipos de datos distintos, en la instruccion 2 se tratan de numeros entreos, comunmente llamados **Int** o **Integers**, mientras que en la instruccion 3 se trata de cadenas, comunmente llamados **Str** o **Strings**, su nombre proviene de que son cadenas de caracteres en codigo [ASCII](https://elcodigoascii.com.ar/).

```powershell
>>> print (2* (3+5))
16
>>> print (2 * 3 + 5)
11
```
La instruccion 4 se puede interpretar de la siguiente manera:
Sumar `3` y `5`, multiplicar por `2`, y luego mostrarlo por consola, el resultado es `16`.
Mientras la instruccion 5 se puede interpretar de la siguiente manera:
Multiplicar `2` y `3`,Sumar `5`, y luego mostrarlo por consola, el resultado es `11`.
Por lo que queda demostrado que las reglas de precedencia funcionan haciendo que se ejecute primero lo que esta adentro de los parentesis `()`.

```powershell
>>> print (3 * "Hola")
HolaHolaHola
>>> print ("Hola" * 3)
HolaHolaHola
```
El resultado es el mismo, (el de concatenar 3 veces la misma cadena), la unica diferencia es la de cambiar de lugar los operandos pero, al mejor sentido de la propiedad multiplicacion en matematica, el orden de los factores no altera el producto.

###### b) Qué pasó en las consignas 8 y 9?
```powershell
>>> PRINT ("hola")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'PRINT' is not defined
```
En la instruccion 8 el error esta dado porque el lenguaje no reconoce la **funcion** `PRINT`, seguramente la funcion que se quiso llamar es `print`, las mayusculas hacen que sean funciones ditintas.

```powershell
>>> print (hola)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'hola' is not defined
```
En la instruccion 9 el error esta dado porque no hay nada declarado con la plabara `hola`, basicamente cuando uno no usa `""` lo que se esta llamando es una declaracion de algo.


##### Ejercicio 11: Ejecute las siguientes instrucciones:
```powershell
>>> "hola Fundamentos"
'hola Fundamentos'
>>> 2+3
5
```
###### a) ¿Pudo hacerlo?
Si, sin problema, y se debe a que los interpretes si las declaraciones son simples el solo se encarga de mostrarlo por pantalla.

###### b) Compare con 1 y 2 del ejercicio anterior.
La unica diferencia es que aca no se llama la **funcion global** `print`

---
### Desde la consola
##### Ejercicio 12: Ejecute las instrucciones guardadas en el archivo anterior ( programa.py) desde la consola. (Para esto, ubicado en la carpeta creada anteriormente y donde guardó el archivo -por ejemplo practica Fundamentos- ejecute el comando python programa.py). Explique por qué debe anteponer el comando python.
.../practica_Fundamentos/programa.py:
```Python
print("hola Fundamentos")
print(2 + 3)
print("2" + "3")
print(2* (3+5))
print(2 * 3 + 5)
print(3 * "Hola")
print("Hola" * 3)
PRINT("hola")
print(hola)
"hola Fundamentos"
2+3
```
```powershell
(base) D:\Javi\Proyectos\practica_Fundamentos>python programa.py
hola Fundamentos
5
23
16
11
HolaHolaHola
HolaHolaHola
Traceback (most recent call last):
  File "programa.py", line 9, in <module>
    PRINT("hola")
NameError: name 'PRINT' is not defined
```
Andubieron las instrucciones pero las que tienen error detienen la ejecucion

---
### Desde Geany
##### Ejercicio 13: Genere un nuevo archivo y tipee las siguientes instrucciones:
```Python
print "Hola"
print " Vamos a trabajar un rato con Geany"
```
###### a) Intente ejecutar este código. ¿Pudo hacerlo?
No, la funcion print me exigue que pasa los **parametros** dentro de paraentesis `()`

###### b) Guarde el archivo con el nombre primer_programa.py (Cree primero una carpeta en su disco donde guardará los programas Python, por ejemplo: practica_Fundamentos)
.../practica_Fundamentos/primer_programa.py:
```Python
print("Hola");
print(" Vamos a trabajar un rato con Geany");
```

###### c) ¿Puede ver algún cambio en el código de su programa?
No excepto por los cambios de color que ayudan a la lectura

###### d) Ahora intente ejecutar el código. ¿Pudo hacerlo?
si perfectamente
```Python
\practica_Fundamentos>python primer_programa.py
Hola
 Vamos a trabajar un rato con Geany
```

---
### PARTE IV: para debatir entre todos
##### Entre todos, den las razones y justificaciones para defender esto:
###### a) Python es multiplataforma
Su código fuente **es ejecutable entre varios sistema operativos**, por lo que si, **es multiplataforma**.

###### b) Se puede ejecutar el mismo programa .py tanto en Windows como en Linux
Si siempre y cuendo este instalado su interprete en el sistema.

###### c) Python tiene tipado dinámico
Cuando se declaran **las variables en phyton estas pueden almacenar datos de todo tipo**, asi que se puede afirmar que **es de tipado dinámico**

###### d) Python es software libre
Python es un software libre debido a tiene una **licencia de software libre**, esta es un documento que **otorga** al receptor de una pieza de software **derechos** extensivos **para modificar y redistribuir ese software**.

###### e) Python es un lenguaje de alto nivel
En Python los algoritmos se expresan de una manera **adecuada a la capacidad cognitiva humana**, por lo que entra dentro de las caracteristicas de **un lenguaje de alto nivel**.

[GitHub personal](https://github.com/JavierBalonga/Fundamentos-de-Informatica-UNAJ/)  
[Siguiente Unidad](https://github.com/JavierBalonga/Fundamentos-de-Informatica-UNAJ/tree/master/Unidad%20II)