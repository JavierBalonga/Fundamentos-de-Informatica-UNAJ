
def ejercicio0():
    #Declaracion de la funcion
    def myFuncion(parametroFormal1, parametroFormal2 = "valor default"):
        #Inicio del cuerpo de la funcion
        print("el parametro formal 2 toma el " + parametroFormal2)
        return "este es el resultado de la funcion con los parametros: " + parametroFormal1 + ", " + parametroFormal2
        #Final del cuerpo de la funcion
    #Llamado de la funcion
    resultadoDeLaFuncion = myFuncion("parametroReal")
    print(resultadoDeLaFuncion)


def ejercicio2():
    def imprimir_mensaje():
        print("Estudiando Fundamentos de Informatica en la UNAJ")
    imprimir_mensaje()

def ejercicio3a():
    def imprimir_mensaje():
        return "Estudiando Fundamentos de Informatica en la UNAJ"
    print(imprimir_mensaje())

def ejercicio3c():
    def imprimir_mensaje(curso):
        print("Estudiando " + curso + " en la UNAJ")
    imprimir_mensaje("Matemática I")
    imprimir_mensaje("Python")

def ejercicio4():
    def imprimir_mensaje(day, month, year):
        print(day + " de " + month + " de " + year)
    imprimir_mensaje("21", "septiembre", "2012")

def ejercicio5():
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

def ejercicio6():
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

def ejercicio7():
    def AreaDeUnCirculoDeDiametro(diametro):
        return 3.14159265359 * diametro ** 2
    def AreaDeUnCuadradoDeLado(lado):
        return lado ** 2
    def AreaDeUnRectanguloDeLados(lado1, lado2):
        return lado1 * lado2
    print(AreaDeUnCirculoDeDiametro(10))
    print(AreaDeUnCuadradoDeLado(7))
    print(AreaDeUnRectanguloDeLados(7, 5))

def ejercicio8():
    def calculo_rebaja(precioAnterior, precioRebajado):
        return 1 - precioRebajado / precioAnterior
    print(calculo_rebaja(100,80))

def ejercicio9():
    def calculo_nuevo_precio(precioAnterior, porcentajeDeAumento):
        return precioAnterior * (1 + porcentajeDeAumento)
    print(calculo_nuevo_precio(100, 0.2))

def ejercicio10():
    def calculo_transporte(cantAlum1, cantAlum2, cantAlum3, cantAsientos):
        cantPersonas = cantAlum1 + cantAlum2 + cantAlum3 + 9
        micros = cantPersonas // cantAsientos
        if (cantPersonas % cantAsientos > 0): micros = micros + 1
        return micros
    print(calculo_transporte(25,28,26,40))


def ejercicio11():
    def armo_cartel(cadena, precioAnterior, precioRebajado):
        print("Atención!!! Gran rebaja para el producto nombre " + cadena)
        print("Antes: precio anterior " + str(precioAnterior))
        print("Ahora: precio rebajado " + str(precioRebajado))
    armo_cartel("Mause Nisuta", 400, 300)

def ejercicio12():
    def calculo_litros(altoMetros, anchoMetros, profundidadMetros):
        return altoMetros * anchoMetros * profundidadMetros * 1000
    print(calculo_litros(2, 1, 0.6))

def ejercicio13():
    def a_pagar(cantPersonas, gastoBebidas, gastoComida, gastoAlquiler):
        return (gastoBebidas + gastoComida + gastoAlquiler) / cantPersonas
    print(a_pagar(3, 1000.0, 7000.0, 12000.0))

def ejercicio14():
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

def ejercicio15():
    def calculo_dosis(dias, cantVecesPorDia, comprimidosDelEnvase):
        return (dias * cantVecesPorDia) > comprimidosDelEnvase
    print(calculo_dosis(7, 3, 16))

def ejercicio16():
    def precio_con_iva(precioSinIVA):
        return precioSinIVA * 1.21
    print(precio_con_iva(100))

exit = False
while(not exit):
    try:
        print()
        print("Que Ejercicio quiere ejecutar? sino use 'exit' para salir")
        ej = input("Ejercicio ")
        if(ej == "exit"): exit = True
        else:
            ej = int(ej)
            if(ej == 0): ejercicio0()
            if(ej == 1): print("El Ejercicio 1 no esta en el programa")
            if(ej == 2): ejercicio2()
            if(ej == 3): 
                print("item 'a' o 'c'")
                item = str(input("item "))
                if(item == "a"): ejercicio3a()
                if(item == "c"): ejercicio3c()
            if(ej == 4): ejercicio4()
            if(ej == 5): ejercicio5()
            if(ej == 6): ejercicio6()
            if(ej == 7): ejercicio7()
            if(ej == 8): ejercicio8()
            if(ej == 9): ejercicio9()
            if(ej == 10): ejercicio10()
            if(ej == 11): ejercicio11()
            if(ej == 12): ejercicio12()
            if(ej == 13): ejercicio13()
            if(ej == 14): ejercicio14()
            if(ej == 15): ejercicio15()
            if(ej == 16): ejercicio16()
    except:
        print("No no no! esa no es la palabra magica XD")
