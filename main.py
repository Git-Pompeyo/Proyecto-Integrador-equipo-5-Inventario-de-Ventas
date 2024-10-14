from tabulate import tabulate
import csv
import sys

VENDEDORES_FILE = "vendedores.txt"
VENTAS_FILE = "ventas.txt"
INVENTARIO_FILE = "inventario.txt"

class NotError_SalirDeBucle(Exception):
    pass

inventario = []
ventas = []
vendedores = []

def importar_ventas():
    global ventas
    try:
            with open(VENTAS_FILE, "r") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    id = row['vendedor'] 
                    modelo = row["modelo"]
                    nombre = row["nombre"]
                    cantidad = int(row["cantidad"])

                    venta = {'vendedor': id, 'modelo': modelo , 'nombre': nombre, 'cantidad': cantidad}

                    ventas.append(venta)           
                
    except FileNotFoundError:
            print(f"ERROR: El archivo '{"ventas.txt"}' no se encontró /Ventas")
    except csv.Error:
            print(f"ERROR: Archivo CSV malformado /Ventas")

def importar_vendedores():
    global vendedores
    try:
        with open(VENDEDORES_FILE, "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                id = row['ID']
                nombre = row['Nombre']
                vendedor = {'ID': id, 'Nombre': nombre}
                vendedores.append(vendedor)

    except FileNotFoundError:
        print(f"ERROR: El archivo '{VENDEDORES_FILE}' no se encontró /Vendedores")
    except csv.Error:
        print(f"ERROR: Archivo CSV malformado /Vendedores")


def importar_inventario():
    global inventario
    try:
        with open(INVENTARIO_FILE, "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                modelo = row['modelo']
                nombre = row['nombre']
                cantidad = int(row['cantidad'])
                producto = {'modelo': modelo, 'nombre': nombre, 'cantidad': cantidad}
                inventario.append(producto)

    except FileNotFoundError:
        print(f"ERROR: El archivo '{INVENTARIO_FILE}' no se encontró /Inventario")
    except csv.Error:
        print(f"ERROR: Archivo CSV malformado /Inventario")

def agregar_venta():

    
    modelo = input("Dime el modelo del auto: ")
    nombre = input("Dime el nombre del auto: ")
    
    try:
        while True:
            cantidad = int(input("Dime la cantidad a vender: "))
            vendedor = input("Dime el ID del vendedor: ")
            if cantidad <= 0:
                print("ERROR: La cantidad debe ser un número positivo mayor que cero.")
                raise ValueError
            break
    except ValueError:
        print("ERROR: ingresa un número entero válido.")
        return
    
    try:    
        while True:
            for sellers in vendedores:
                if sellers["ID"] == vendedor:
                    pass
            raise ValueError
    except ValueError:
        print("ERROR: ese empleado no esta registrado")


    
    venta = {
        "vendedor": vendedor,
        "modelo": modelo, 
        "nombre": nombre, 
        "cantidad": cantidad
        }
    
    
    try:
        while True:
            for item in inventario:
                if venta["modelo"] == item["modelo"] and venta["nombre"] == item["nombre"]:
               

                    if venta["cantidad"] <= item["cantidad"]:
                     
                        item["cantidad"] -= cantidad

                        if item["cantidad"] == 0:
                            inventario.remove(item)

                        for j in ventas:
                            if venta["vendedor"] == j["vendedor"] and venta["modelo"] == j["modelo"]: 
                                    j["cantidad"] += cantidad
                                    raise NotError_SalirDeBucle
                        ventas.append(venta)
                        raise NotError_SalirDeBucle
                        
                    
                    else:
                        print(f"No hay suficientes '{modelo}', se requieren: {venta["cantidad"]-item["cantidad"]}")
                        raise NotError_SalirDeBucle
                        
            print(f"Verifica el nombre y modelo. No se encuentra en el inventario")
            break
    except NotError_SalirDeBucle:
       
        pass


def agregar_producto():
    modelo = input("Dime el modelo del auto: ")
    nombre = input("Dime el nombre del auto: ")

    try: 
        while True:
            cantidad = int(input("Dime la cantidad a vender: "))
            if cantidad <= 0:
                print("ERROR: La cantidad debe ser un número positivo mayor que cero.")
                continue
            break
    except ValueError:
        print("ERROR: ingresa un número entero válido.")


    producto = {
        "modelo": modelo,
        "nombre": nombre,
        "cantidad": cantidad
    }

    try:
        for item in inventario:
            if producto["modelo"] == item["modelo"] and producto["nombre"] == item["nombre"]:
                item["cantidad"] += cantidad
                raise NotError_SalirDeBucle
            
        inventario.append(producto)
        raise NotError_SalirDeBucle
    
    except NotError_SalirDeBucle:
        pass

  

def consultar_inventario():
    
    header = ["Modelo","Nombre","Cantidad"]
    table = []
    row = []

    for item in inventario:
        modelo = item["modelo"]
        nombre = item["nombre"]
        cantidad = item["cantidad"]
        row = [ modelo, nombre, cantidad]
        table.append(row)

    return tabulate(table,header,tablefmt="pretty")

def consultar_ventas_general():
    
    header = ["Vendedor","Modelo","Nombre","Cantidad"]
    table = []

    for item in ventas:
        row = []    
        row = [item["vendedor"], item["modelo"], item["nombre"], item["cantidad"]]
        table.append(row)

    print(tabulate(table,header,tablefmt="pretty"))

def reporte_ventas_por_vendedor():
    try:
        while True:
            id = input("Dime el ID del vendedor: ")

            for item in vendedores:
                if id == item["ID"]:
                    raise NotError_SalirDeBucle
            
            print("ERROR: ese vendedor no existe")
            return
    
    except NotError_SalirDeBucle:
        pass

    headers = ["ID", "Vendedor", "Modelo", "Cantidad"]
    table = []

    for item in vendedores:
        if id == item["ID"]:
            vendedor = item["Nombre"]

    for item in ventas:
        if item["vendedor"] == id:
            id = id
            vendedor = vendedor
            modelo = item["modelo"]
            cantidad = item["cantidad"]

            row = [id,vendedor,modelo,cantidad]

            table.append(row)

    for row in table:
        cantidad = int(row[3])

        if cantidad >0 or cantidad != None:
            print(tabulate(table,headers,tablefmt="pretty"))

                    


def reporte_ventas_por_articulo():
    try:
      while True:
          modelo = input("Dime el modelo: ")

          for item in ventas:
              if modelo == item["modelo"]:
                  raise NotError_SalirDeBucle
        
          print("ERROR: ese modelo no se ha vendido")
          return
    except NotError_SalirDeBucle:
        pass
    
    headers = ["Modelo","Vendedor", "Cantidad"]
    table = []

 

    for item in ventas:
        if item["modelo"] == modelo:
            modelo = modelo
            vendedor = item["vendedor"]
            cantidad = item["cantidad"]

            row = [modelo,vendedor,cantidad]

            table.append(row)

    
    print(tabulate(table,headers,tablefmt="pretty"))

                    


def registrar_vendedor():
    id = (input("Dame el ID: "))
    nombre = input("Dime el nombre del vendedor: ")
    producto = {
        "ID": id,
        "Nombre": nombre
        }


    try:  
        for item in vendedores:
            if producto["ID"] == item["ID"] and producto["Nombre"] == item["Nombre"]:
                print("Ese vendedor ya existe")
                raise NotError_SalirDeBucle
            
        vendedores.append(producto)
    except NotError_SalirDeBucle:
        pass

def mostrar_vendedores():
    headers = ["ID", "Nombre"]
    table = []
    for vendedor in vendedores:
        row = [vendedor["ID"], vendedor["Nombre"]]
        table.append(row)
    print(tabulate(table, headers, tablefmt="pretty"))


def modelo_mas_vendido():
    contador_modelos = []
    

    for venta in ventas:
        cantidad = venta["cantidad"]
        modelo = venta["modelo"]
        nombre = venta["nombre"]
        break

    for venta in ventas:
        if venta["cantidad"] > cantidad:
            cantidad = venta["cantidad"]
            modelo = venta["modelo"]
            nombre = venta["nombre"]

    mayor_producto = {"modelo":modelo, "nombre":nombre, "cantidad": cantidad}
    contador_modelos.append(mayor_producto)

    for venta in ventas:
        if venta["cantidad"] == cantidad and venta["modelo"] != modelo:
            cantidad = venta["cantidad"]
            modelo = venta["modelo"]
            nombre = venta["nombre"]
            mayor_producto = {"modelo":modelo, "nombre":nombre, "cantidad": cantidad}
            contador_modelos.append(mayor_producto)


    for item in contador_modelos:
        print(f"El modelo más vendido es '{item["modelo"]}' ({item["nombre"]}) con {item["cantidad"]} unidades vendidas.")


def vendedor_estrella():
    contador_ventas = []

    for empleado in vendedores:
        cantidad = 0

        for sell in ventas:
            if empleado["ID"] == sell["vendedor"]:
                vendedor = empleado["ID"]
                cantidad += int(sell["cantidad"])
        persona = {"vendedor":vendedor, "cantidad": cantidad}
        contador_ventas.append(persona)

    mayor_cantidad = 0
    mayor_vendedor = 0

    for item in contador_ventas:
        if item["cantidad"] > mayor_cantidad:
            mayor_cantidad = item["cantidad"]
            mayor_vendedor = item["vendedor"]
    
    print(f"El mayor vendedor es {mayor_vendedor} con {mayor_cantidad} ventas")



       


def menu():

    while True:
        print("\n=== SISTEMA DE INVENTARIO Y VENTAS ===\n")
        print("1) Registrar venta")
        print("2) Agregar producto al inventario")
        print("3) Mostrar inventario")
        print("4) Consultar datos de ventas")
        print("5) Mostrar reportes de ventas por vendedor o por artículo")
        print("6) Registrar vendedor")
        print("7) Mostrar vendedores")
        print("8) Mostrar modelo más vendido")
        print("9) Mostrar vendedor estrella")
        print("10) Salir\n")

        respuesta = input("Ingrese la opción deseada: ")

        if (respuesta == "1" or respuesta == "2" or respuesta == "3" or respuesta == "4"
            or respuesta == "5" or respuesta == "6" or respuesta == "7" or respuesta == "8"
            or respuesta == "9" or respuesta == "10"):
            break

        print("ERROR: ingresa una respuesta adecuada")


    return respuesta


def main():
    importar_ventas()
    importar_vendedores()
    importar_inventario()

    respuesta = menu()

    while True:
        if respuesta == "1": 
            agregar_venta()

        elif respuesta == "2":
            agregar_producto()

        elif respuesta == "3":
            print(consultar_inventario())

        elif respuesta == "4":
            consultar_ventas_general()

        elif respuesta == "5":

            try:
                while True:
                    print("Opciones para mostrar reporte:")
                    print()
                    print("1) Reporte por vendedor")
                    print("2) Reporte por artículo")

                    respuesta = input("Ingrese respuesta: ")

                    if respuesta == "1":
                        reporte_ventas_por_vendedor()
                        raise NotError_SalirDeBucle

                    if respuesta == "2":
                        reporte_ventas_por_articulo()
                        raise NotError_SalirDeBucle
                    print("ERROR: ingresa una opcion adecuada")

            except NotError_SalirDeBucle:
                pass

        elif respuesta == "6":
            registrar_vendedor()

        elif respuesta == "7":
            mostrar_vendedores()

        elif respuesta == "8":
            modelo_mas_vendido()

        elif respuesta == "9":
            vendedor_estrella()
            
        elif respuesta == "10":
            sys.exit()

        respuesta = menu()
        
        


if __name__ == "__main__":
    main()