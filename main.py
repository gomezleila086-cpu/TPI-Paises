import csv


def cargar_paises():
    paises = []

    try:
        with open("paises.csv", "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)

            for fila in lector:
                pais = {
                    "nombre": fila["nombre"],
                    "poblacion": int(fila["poblacion"]),
                    "superficie": int(fila["superficie"]),
                    "continente": fila["continente"]
                }

                paises.append(pais)

    except FileNotFoundError:
        print("Error: no se encontró el archivo paises.csv")

    except ValueError:
        print("Error: el CSV tiene datos con formato incorrecto")

    return paises


def guardar_paises(paises):

    with open("paises.csv", "w", newline="", encoding="utf-8") as archivo:

        campos = ["nombre", "poblacion", "superficie", "continente"]

        escritor = csv.DictWriter(archivo, fieldnames=campos)

        escritor.writeheader()

        escritor.writerows(paises)


def agregar_pais(paises):

    nombre = input("Ingrese el nombre del país: ").strip()

    while nombre == "":
        print("El nombre no puede estar vacío.")
        nombre = input("Ingrese el nombre del país: ").strip()

    try:
        poblacion = int(input("Ingrese la población: "))
        superficie = int(input("Ingrese la superficie en km²: "))

    except ValueError:
        print("Error: debe ingresar números enteros.")
        return

    continente = input("Ingrese el continente: ").strip()

    while continente == "":
        print("El continente no puede estar vacío.")
        continente = input("Ingrese el continente: ").strip()

    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }

    paises.append(nuevo_pais)

    guardar_paises(paises)

    print("País agregado correctamente.")


def actualizar_pais(paises):

    nombre = input("Ingrese el nombre del país a actualizar: ").strip().lower()

    for pais in paises:

        if pais["nombre"].lower() == nombre:

            try:
                pais["poblacion"] = int(input("Ingrese la nueva población: "))
                pais["superficie"] = int(input("Ingrese la nueva superficie en km²: "))

            except ValueError:
                print("Error: debe ingresar números enteros.")
                return

            guardar_paises(paises)

            print("País actualizado correctamente.")
            return

    print("No se encontró el país.")


def buscar_pais(paises):

    busqueda = input("Ingrese el nombre del país a buscar: ").strip().lower()

    encontrados = []

    for pais in paises:
        if busqueda in pais["nombre"].lower():
            encontrados.append(pais)

    if len(encontrados) == 0:
        print("No se encontraron países.")
    else:
        for pais in encontrados:
            print(pais)


def filtrar_paises(paises):

    print("\n1. Continente")
    print("2. Rango de población")
    print("3. Rango de superficie")

    opcion = input("Seleccione una opción: ")

    encontrados = []

    try:

        if opcion == "1":

            continente = input("Ingrese el continente: ").strip().lower()

            for pais in paises:
                if pais["continente"].lower() == continente:
                    encontrados.append(pais)

        elif opcion == "2":

            minimo = int(input("Población mínima: "))
            maximo = int(input("Población máxima: "))

            for pais in paises:
                if minimo <= pais["poblacion"] <= maximo:
                    encontrados.append(pais)

        elif opcion == "3":

            minimo = int(input("Superficie mínima: "))
            maximo = int(input("Superficie máxima: "))

            for pais in paises:
                if minimo <= pais["superficie"] <= maximo:
                    encontrados.append(pais)

        else:
            print("Opción inválida.")
            return

    except ValueError:
        print("Debe ingresar números válidos.")
        return

    if len(encontrados) == 0:
        print("No se encontraron países.")
    else:
        for pais in encontrados:
            print(pais)


def ordenar_paises(paises):

    print("\n1. Nombre")
    print("2. Población")
    print("3. Superficie")

    opcion = input("Seleccione una opción: ")

    orden = input("Ascendente (A) o Descendente (D): ").upper()

    descendente = orden == "D"

    if opcion == "1":
        ordenados = sorted(paises, key=lambda p: p["nombre"], reverse=descendente)

    elif opcion == "2":
        ordenados = sorted(paises, key=lambda p: p["poblacion"], reverse=descendente)

    elif opcion == "3":
        ordenados = sorted(paises, key=lambda p: p["superficie"], reverse=descendente)

    else:
        print("Opción inválida.")
        return

    for pais in ordenados:
        print(pais)


def mostrar_estadisticas(paises):

    mayor = max(paises, key=lambda p: p["poblacion"])
    menor = min(paises, key=lambda p: p["poblacion"])

    promedio_poblacion = sum(p["poblacion"] for p in paises) / len(paises)

    promedio_superficie = sum(p["superficie"] for p in paises) / len(paises)

    continentes = {}

    for pais in paises:

        continente = pais["continente"]

        if continente in continentes:
            continentes[continente] += 1
        else:
            continentes[continente] = 1

    print("\n=== ESTADÍSTICAS ===")

    print("País con mayor población:", mayor["nombre"])

    print("País con menor población:", menor["nombre"])

    print("Promedio de población:", promedio_poblacion)

    print("Promedio de superficie:", promedio_superficie)

    print("\nCantidad de países por continente:")

    for continente, cantidad in continentes.items():
        print(continente, ":", cantidad)


def mostrar_menu():

    print("\n=== GESTIÓN DE PAÍSES ===")
    print("1. Agregar país")
    print("2. Actualizar país")
    print("3. Buscar país")
    print("4. Filtrar países")
    print("5. Ordenar países")
    print("6. Mostrar estadísticas")
    print("7. Salir")


def main():

    paises = cargar_paises()

    while True:

        mostrar_menu()

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            agregar_pais(paises)

        elif opcion == "2":
            actualizar_pais(paises)

        elif opcion == "3":
            buscar_pais(paises)

        elif opcion == "4":
            filtrar_paises(paises)

        elif opcion == "5":
            ordenar_paises(paises)

        elif opcion == "6":
            mostrar_estadisticas(paises)

        elif opcion == "7":
            print("Programa finalizado.")
            break

        else:
            print("Opción inválida.")


main()