![alt text](https://www.unaj.edu.ar/wp-content/uploads/2016/06/logo-unaj-2016-01.jpg)
# Fundamentos de Informatica

## Practica 3
---
### PARTE I : Aspectos Conceptuales
##### a) ¿Qué ventajas tiene la utilización de funciones?
Las funciones tienen la ventaja de poder particionar el codigo en abstaracciones de funcionalidad, por lo que si hay una parte de mi algoritmo que se vuelve repetitiva o se ve que puede ser aplicable en muchas situaciones se la puede separar a una funcion.
##### b) ¿Hay algún cuidado en el orden en el que se pasan los parámetros a una función?
Si, segun el orden que se pasen los parametros estos en la funcion, cambia el parametro por el que se pasa.
##### c) ¿Cuándo uso la sentencia return?
La sentencia `return` sirve para devolver un valor desde la funcion
##### d) ¿Qué diferencia hay entre la definición y la invocación de una función?
Cuando uno la define, basicamente es la declaracion de la misma al momento de ejecutarse estas instrucciones las mismas no se ejecutan, recien se va a ejecutar cuando se llame esta funcion
##### e) ¿Qué son los parámetros formales y para qué sirven? Ejemplifique.
Los parametros formales son los que se declaran cuando se declara la funcion, y son los que por asi decir resiven los valores de los parametros reales, ejemplificacion al final de la parte I
##### f) ¿Qué son los parámetros reales y para qué sirven? Ejemplifique.
Los parametros reales son los que se ingresan en la funcion al llamarle, y su valor se le es pasado a los parametros formales durante la ejecucion de la funcion, ejemplificacion al final de la parte I
##### g) ¿Qué es el cuerpo de una función? Ejemplifique.
El cuerpo de una funcion es el bloque que contiene la seri de instrucciones que la misma ejecuta, ejemplificacion al final de la parte I
##### h) ¿Existen funciones sin parámetros o argumentos?
Si, algunas funciones no requieren de parametros para ser ejecutadas
##### i) ¿Puede usar una letra o un número como parámetro formal? ¿Y cómo parámetros real?
Como parametro real asi como con las variables las mismas no pueden empezar con un numero, pero si pueden incluir un numero despues del primer caracter, y en los parametros reales se le deben pasar valores, osea numeros, cadenas, etc
##### j) ¿Puedo tener una cantidad distinta de parámetros formales que reales en una función?
Si, se pueden pasar menos parametros reales que los parametros formales que tiene una funcion, por ejemplo podria dejarle definidos valores por default a parametros formales para que si a estos no les son pasados parametros reales tomen los default
**Ejemplificacion:**
```Py
#Declaracion de la funcion
def myFuncion(parametroFormal1, parametroFormal2 = "valor default"):
    #Inicio del cuerpo de la funcion
    print("el parametro formal 2 toma el " + parametroFormal2)
    return "este es el resultado de la funcion con los parametros: " + parametroFormal1 + ", " + parametroFormal2
    #Final del cuerpo de la funcion
#Llamado de la funcion
resultadoDeLaFuncion = myFuncion("parametroReal")
print(resultadoDeLaFuncion)
```
```powershell
el parametro formal 2 toma el valor default
este es el resultado de la funcion con los parametros: parametroReal, valor default
```
---
### PARTE II: Ahora practicamos
##### Ejercicio 1: Mencione los errores en los siguientes códigos:
###### a) 
```Py
def suma(par1, par2):
    print(par1+par2)
suma()
```
No se pasaron parametros reales

###### b)
```Py
def suma(par1, par2):
    print (par1 + par2)
        print(suma(12, 10))
```
La tercera instruccion no respeta la identacion, por lo que esta no esta en el cuerpo de la funcion, y si se ejecutara no va a imprimir nada, porque la funcion `suma` no retorna ningun valor
```powershell
  File "test.py", line 13
    print(suma(12, 10))
    ^
IndentationError: unexpected indent
```

###### c)
```Py
def suma(par1, par2):
    return (par1 + par2)
        suma(12, 10)
```
La tercera instruccion no respeta la identacion, por lo que esta no esta en el cuerpo de la funcion, si se ejecuta la no vamos a notar nada de ella porque no se hace nada con el resultado de la funcion
```powershell
  File "test.py", line 23
    suma(12, 10)
    ^
IndentationError: unexpected indent
```

###### d)
```Py
def suma(par1):
    return (par1 + 2)
suma(12, 10)
```
Se pasaron mas parametros reales que los que admite la funcion
```powershell
  File "test.py", line 32, in <module>
    suma(12, 10)
TypeError: suma() takes 1 positional argument but 2 were given
```

##### Ejercicio 2: Definir una función denominada “imprimir_mensaje” que imprima el siguiente mensaje en pantalla: “Estudiando Fundamentos de Informática en la UNAJ”
```Py
def imprimir_mensaje():
    print("Estudiando Fundamentos de Informatica en la UNAJ")
imprimir_mensaje()
```
```powershell
Estudiando Fundamentos de Informatica en la UNAJ
```
##### Ejercicio 3: Definir una función denominada “retorno_mensaje” que retorne siguiente mensaje: “Estudiando Fundamentos de Informática en la UNAJ”.
```Py
def imprimir_mensaje():
    return "Estudiando Fundamentos de Informatica en la UNAJ"
```
###### a) ¿Cómo hago para mostrar ese mensaje en pantalla?
Para mostrar el mensaje por consola, puedo hacer la siguiente instruccion:
```Py
print(imprimir_mensaje())
```
```powershell
Estudiando Fundamentos de Informatica en la UNAJ
```
###### b) ¿Qué diferencia encuentra con el ejercicio anterior?
La diferencia se hace evidente con los ejercicios anteriores, el primero directamente imprime el mensaje, mientras el segundo lo retorna, por lo que para imprimirlo hay que ejecutar la funcion `print` por fuera de la funcion.
###### c) Si tuvieras que imprimir mensajes como “Estudiando Matemática I en la UNAJ“ y “Estudiando Python en la UNAJ” utilizando la misma función ¿Cómo la modificarías?
```Py
def imprimir_mensaje(curso):
    print("Estudiando " + curso + " en la UNAJ")
imprimir_mensaje("Matemática I")
imprimir_mensaje("Python")
```
```powershell
Estudiando Matemática I en la UNAJ
Estudiando Python en la UNAJ
```
##### Ejercicio 4: Definir una función denominada “imprimo_fecha” que reciba tres cadenas de caracteres que representan un día, un mes y un año e imprima la fecha de la siguiente manera: “ 21 de septiembre de 2012”.
```Py
def imprimir_mensaje(day, month, year):
    print(day + " de " + month + " de " + year)
imprimir_mensaje("21", "septiembre", "2012")
```
```powershell
21 de septiembre de 2012
```
##### Ejercicio 5: Definir una función denominada “cuantos_dias” que reciba el número de mes como parámetro y retorne la cantidad de días que posee. Ejemplo: cuantos_dias(1), debería retornar 31. Ayuda: Pensar en tener una lista de la siguiente manera: [[“enero”,31],[“febrero”, 28], ...]
```Py
def cuantos_dias(month):
    if (month == "Enero"): return 31
    if (month == "Febrero"): return 28
    if (month == "Marzo"): return 31
    if (month == "Abril"): return 30
    if (month == "Mayo"): return 31
    if (month == "Junio"): return 30
    if (month == "Julio"): return 31
    if (month == "Agosto"): return 31
    if (month == "Septiembre"): return 30
    if (month == "Octubre"): return 31
    if (month == "Noviembre"): return 30
    if (month == "Diciembre"): return 31
print(cuantos_dias("Mayo"))
```
```powershell
31
```
No lo hice con la lista porque no lo vi conveniente
##### Ejercicio 6: Definir una función que reciba un número como parámetro y mostrar la tabla de multiplicar de dicho número.
```Py
def tablaDeMultiplicarDe(numero):
    print(str(numero) + " *  1 =  " + str(numero * 1))
    print(str(numero) + " *  2 =  " + str(numero * 2))
    print(str(numero) + " *  3 =  " + str(numero * 3))
    print(str(numero) + " *  4 =  " + str(numero * 4))
    print(str(numero) + " *  5 =  " + str(numero * 5))
    print(str(numero) + " *  6 =  " + str(numero * 6))
    print(str(numero) + " *  7 =  " + str(numero * 7))
    print(str(numero) + " *  8 =  " + str(numero * 8))
    print(str(numero) + " *  9 =  " + str(numero * 9))
    print(str(numero) + " * 10 = " + str(numero * 10))
tablaDeMultiplicarDe(7)
```
```powershell
7 *  1 =  7
7 *  2 =  14
7 *  3 =  21
7 *  4 =  28
7 *  5 =  35
7 *  6 =  42
7 *  7 =  49
7 *  8 =  56
7 *  9 =  63
7 * 10 = 70
```
##### Ejercicio 7: Definir una función que calcule el área de un círculo, otra que calcule el área de un cuadrado y otra que calcule el área de un rectángulo. Analice qué parámetros deberían recibir dichas funciones.
```Py
def AreaDeUnCirculoDeDiametro(diametro):
    return 3.14159265359 * diametro ** 2
def AreaDeUnCuadradoDeLado(lado):
    return lado ** 2
def AreaDeUnRectanguloDeLados(lado1, lado2):
    return lado1 * lado2
print(AreaDeUnCirculoDeDiametro(10))
print(AreaDeUnCuadradoDeLado(7))
print(AreaDeUnRectanguloDeLados(7, 5))
```
```powershell
314.159265359
49
35
```
---
### Ejercicios Complementarios
##### Ejercicio 8: Definir una función llamada calculo_rebaja que reciba dos números, uno con el precio anterior y otro para el precio rebajado y devuelva un número que represente el porcentaje rebajado.
```Py
def calculo_rebaja(precioAnterior, precioRebajado):
    return 1 - precioRebajado / precioAnterior
print(calculo_rebaja(100,80))
```
```powershell
0.19999999999999996
```
##### Ejercicio 9: Definir una función llamada calculo_nuevo_precio que reciba dos números, uno con el precio anterior y otro con el número de porcentaje a aumentar y devuelva el precio aumentado.
```Py
def calculo_nuevo_precio(precioAnterior, porcentajeDeAumento):
    return precioAnterior * (1 + porcentajeDeAumento)
print(calculo_nuevo_precio(100, 0.2))
```
```powershell
120.0
```
##### Ejercicio 10: Definir una función llamada calculo_transporte que reciba cuatro números: la cantidad de alumnos de 1era, 2da y 3er. salita de un jardín de infantes y la cantidad de asientos del transporte escolar. La función debe retornar cuántos micros necesito contratar para una excursión sabiendo que cada salita es acompañada por tres adultos.
```Py
def calculo_transporte(cantAlum1, cantAlum2, cantAlum3, cantAsientos):
    cantPersonas = cantAlum1 + cantAlum2 + cantAlum3 + 9
    micros = cantPersonas // cantAsientos
    if (cantPersonas % cantAsientos > 0): micros = micros + 1
    return micros
print(calculo_transporte(25,28,26,40))
```
```powershell
3
```
##### Ejercicio 11: Definir una función llamada armo_cartel que reciba una cadena de caracteres(para el nombre del producto) y dos números (el precio anterior y el otro para el precio rebajado) e imprima un cartel de la siguiente forma:  
***Atención!!! Gran rebaja para el producto nombre (recibido como parámetro)***  
***Antes: precio anterior (dato recibido como parámetro)***  
***Ahora: precio rebajado (dato recibido como parámetro)***  
```Py
def armo_cartel(cadena, precioAnterior, precioRebajado):
    print("Atención!!! Gran rebaja para el producto nombre " + cadena)
    print("Antes: precio anterior " + str(precioAnterior))
    print("Ahora: precio rebajado " + str(precioRebajado))
armo_cartel("Mause Nisuta", 400, 300)
```
```powershell
Atención!!! Gran rebaja para el producto nombre Mause Nisuta
Antes: precio anterior 400
Ahora: precio rebajado 300
```
##### Ejercicio 12: Definir una función llamada calculo_litros que reciba tres números, el alto, ancho y profundidad (en metros) de una pileta y devuelva la cantidad de litros que tiene.
```Py
def calculo_litros(altoMetros, anchoMetros, profundidadMetros):
    return altoMetros * anchoMetros * profundidadMetros * 1000
print(calculo_litros(2, 1, 0.6))
```
```powershell
1200.0
```
##### Ejercicio 13: Definir una función llamada a_pagar que reciba 4 números: la cantidad de personas, el monto gastado en bebida, el monto gastado en comida y el del alquiler del lugar, y retorne cuánto le toca pagar a cada uno.
```Py
def a_pagar(cantPersonas, gastoBebidas, gastoComida, gastoAlquiler):
    return (gastoBebidas + gastoComida + gastoAlquiler) / cantPersonas
print(a_pagar(3, 1000.0, 7000.0, 12000.0))
```
```powershell
6666.666666666667
```
##### Ejercicio 14: Definir tres funciones llamadas convertir_a_dolar, convertir_a_euro y convertir_a_real. Cada función recibe un parámetro que representa un monto en pesos y devuelve su conversión respectiva.
Me parecia muy debil el codigo si las funciones se limitaban a una tasa de cambio fija, asi que lo hice con una funcion para poder actualizar las tasas de las conversiones
```Py
def funcion_convertir(tasaCambio):
    def nueva_funcion_convertir(pesos):
        return tasaCambio * pesos
    return nueva_funcion_convertir

# Tasas de cambios segun el BNA 02/09/2020
convertir_a_dolar = funcion_convertir(73.25)
convertir_a_euro = funcion_convertir(84.00)
convertir_a_real = funcion_convertir(1250.00)
print(convertir_a_dolar(100))
print(convertir_a_euro(100))
print(convertir_a_real(100))
```
```powershell
7325.0
8400.0
125000.0
```
##### Ejercicio 15: Definir una función llamada calculo_dosis que reciba tres números. Uno para la cantidad de días que debe suministrarse el remedio, el segundo dato para la cantidad de veces por día que debe tomarlo, y el último dato para la cantidad de comprimidos que trae el envase. La función debe devolver verdadero si el envase alcanza para ese tratamiento y falso si no alcanza.
```py
def calculo_dosis(dias, cantVecesPorDia, comprimidosDelEnvase):
    return (dias * cantVecesPorDia) > comprimidosDelEnvase
print(calculo_dosis(7, 3, 16))
```
```powershell
True
```
##### Ejercicio 16: Definir una función llamada precio_con_iva que agrega el IVA (21%) de un producto dado su precio de venta sin IVA.
```py
def precio_con_iva(precioSinIVA):
    return precioSinIVA * 1.21
print(precio_con_iva(100))
```
```powershell
121.0
```

[GitHub personal](https://github.com/JavierBalonga/Fundamentos-de-Informatica-UNAJ/)
[Siguiente Unidad](https://github.com/JavierBalonga/Fundamentos-de-Informatica-UNAJ/tree/master/Unidad%20IV)