def ejercicio1():
    print("Ingrese un numero para mostrar su tabla de multiplicar")
    num = int(input("Numero --> "))
    for i in range(11):
        print(str(num) + " * " + str(i) + " = " + str(num * i))

def ejercicio2():
    print("Ingrese un numero para calcular la sumatoria de 0 hasta dicho numero")
    num = int(input("Numero --> "))
    suma = 0
    for i in range(num + 1):
        suma += i
    print("La sumatoria da " + str(suma))

def ejercicio3():
    texto = ""
    for i in range(256):
        if(i % 10 == 0): texto += "\n"
        texto += str(i) + "=" + "'" + chr(i) + "' | "
    print(texto)

def ejercicio4():
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

def ejercicio5():
    print("Cuantos numeros desa promediar?")
    cantidad = int(input("Cantidad --> "))
    suma = 0
    for i in range(cantidad):
        suma += float(input("Numero " + str(i + 1) + " --> "))
    print("El promedio es de " + str(suma / cantidad))

def ejercicio6():
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

def ejercicio7():
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

def ejercicio8():
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

def ejercicio9():
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

def ejercicio10():
    def primeros_cien_numeros_enteros():
        texto = ""
        for i in range(100):
            texto += str(i) + "\t"
        print(texto)
    primeros_cien_numeros_enteros()

def ejercicio11():
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

def ejercicio12():
    list = [1, 14, 56, 43, 23, 46, 58, 123, 67]
    print("Dada la siguiente lista:")
    print(list)
    max = list[0]
    for element in list:
        if (max < element): max = element
    print("el numero mas alto es " + str(max))

def ejercicio13():
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

def ejercicio14():
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

def ejercicio15():
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

def ejercicio16():
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

def ejercicio17():
    def ingreso_de_numeros():
        print("Ingrese los numeros a enlistar")
        numeros = []
        exit = False
        while(not exit):
            exit = False
            num = float(input("Numero --> "))
            if (num == 0.0): exit = True
            else:
                numeros.append(num)
        return numeros

    def promedio(numeros):
        if(len(numeros) != 0):
            suma = 0
            for num in numeros:
                suma += num
            return suma / len(numeros)
        else: return 0

    def sumatoria(numeros):
        suma = 0
        for num in numeros:
            suma += num
        return suma

    def maximo(numeros):
        maxi = numeros[0]
        for num in numeros:
            if(maxi < num): maxi = num
        return maxi

    def minimo(numeros):
        mini = numeros[0]
        for num in numeros:
            if(mini > num): mini = num
        return mini

    numeros = []
    exit = False
    while(not exit):
        print("*********     Menu     **********")
        print("1. Ingreso de numeros")
        print("2. Ver el promedio de los numeros")
        print("3. Ver la suma de los numeros")
        print("4. Ver la cantidad de numeros")
        print("5. Ver el numero maximo")
        print("6. Ver el numero minimo")
        print("7. Exit")
        exit = False
        op = int(input("Opcion --> "))
        if(op == 1): numeros = ingreso_de_numeros()
        elif(op == 2): print("El promedio es " + str(promedio(numeros)))
        elif(op == 3): print("La suma es " + str(sumatoria(numeros)))
        elif(op == 4): print("Hay " + str(len(numeros)) + " numeros.")
        elif(op == 5): print("El maximo es " + str(maximo(numeros)))
        elif(op == 6): print("El minimo es " + str(minimo(numeros)))
        elif(op == 7): exit = True

exitBigMenu = False
while(not exitBigMenu):
    exitBigMenu = False
    #try:
    print()
    print("Que Ejercicio quiere ejecutar? sino use 'exit' para salir")
    ej = str(input("Ejercicio "))
    if(ej == "exit"): exitBigMenu = True
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
        elif(ej == 15): ejercicio15()
        elif(ej == 16): ejercicio16()
        elif(ej == 17): ejercicio17()
        else: print("El Ejercicio " + str(ej) + " no esta en el programa")
    #except:
        #print("No no no! esa no es la palabra magica XD")