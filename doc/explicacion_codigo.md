### Explicación del código:

Este programa es un sistema de inventario y ventas desarrollado en Python que permite gestionar los productos disponibles, las ventas realizadas y los vendedores registrados. A continuación se mostrara una breve explicación del código:

---

### 1. **Importación de Librerías**

```python
from tabulate import tabulate
import csv
import sys
```

- **`tabulate`**: Se usa para mostrar tablas de datos de manera más legible en la consola.
- **`csv`**: Permite leer y escribir en archivos CSV (Comma Separated Values) que son archivos de texto con valores separados por comas.
- **`sys`**: Proporciona acceso a funcionalidades del sistema, como la salida del programa con `sys.exit()`.

---

### 2. **Variables Globales**

```python
VENDEDORES_FILE = "vendedores.txt"
VENTAS_FILE = "ventas.txt"
INVENTARIO_FILE = "inventario.txt"
```

Estas son variables que almacenan los nombres de los archivos donde se guardan los datos de vendedores, ventas e inventario.

---

### 3. **Clase Personalizada de Excepción**

```python
class NotError_SalirDeBucle(Exception):
    pass
```

Aquí se define una **excepción personalizada** que se usa más adelante para salir de bucles de forma controlada.

---

### 4. **Listas Globales**

```python
inventario = []
ventas = []
vendedores = []
```

- **`inventario`**: Lista donde se guarda la información de los productos en inventario.
- **`ventas`**: Lista donde se guardan las ventas realizadas.
- **`vendedores`**: Lista donde se guardan los vendedores registrados.

---

### 5. **Funciones para Cargar los Datos de los Archivos**

#### a) `importar_ventas()`

Esta función abre el archivo `ventas.txt`, lee su contenido y lo guarda en la lista `ventas`.

```python
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
```

#### b) `importar_vendedores()`

Funciona de manera similar a `importar_ventas()`, pero para el archivo `vendedores.txt`. Guarda la información en la lista `vendedores`.

#### c) `importar_inventario()`

Carga los datos del archivo `inventario.txt` y los guarda en la lista `inventario`.

---

### 6. **Funciones Principales del Sistema**

#### a) `agregar_venta()`

Permite registrar una nueva venta. Valida si el modelo del producto está en el inventario y si hay suficiente cantidad disponible. Si es así, se actualiza el inventario y se agrega la venta a la lista `ventas`.

1. El usuario ingresa el modelo, nombre, cantidad y el ID del vendedor.
2. La función valida que la cantidad ingresada sea positiva y que el vendedor esté registrado.
3. Actualiza el inventario restando la cantidad vendida y añade la venta a la lista.

#### b) `agregar_producto()`

Permite añadir un nuevo producto al inventario o actualizar la cantidad si el producto ya existe.

1. El usuario ingresa el modelo, nombre y cantidad del producto.
2. Si el producto ya está en el inventario, actualiza su cantidad. Si no, lo añade como nuevo.

#### c) `consultar_inventario()`

Muestra el inventario actual en formato de tabla.

#### d) `consultar_ventas_general()`

Muestra todas las ventas registradas en formato de tabla.

#### e) `reporte_ventas_por_vendedor()`

Genera un reporte de ventas de un vendedor específico. Pide el ID del vendedor y muestra todas las ventas realizadas por ese vendedor.

#### f) `reporte_ventas_por_articulo()`

Genera un reporte de ventas de un artículo en particular. El usuario ingresa el modelo del artículo, y el sistema muestra todas las ventas de ese modelo.

---

### 7. **Funciones Adicionales**

#### a) `registrar_vendedor()`

Permite registrar un nuevo vendedor. El usuario ingresa el ID y el nombre del vendedor, y se añade a la lista `vendedores`.

#### b) `mostrar_vendedores()`

Muestra una lista de todos los vendedores registrados en formato de tabla.

#### c) `modelo_mas_vendido()`

Calcula cuál es el modelo más vendido y lo muestra al usuario.

#### d) `vendedor_estrella()`

Calcula qué vendedor ha realizado la mayor cantidad de ventas y lo muestra al usuario.

---

### 8. **Menú del Sistema**

```python
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
```

Esta función muestra el menú principal y devuelve la opción seleccionada por el usuario.

---

### 9. **Función Principal `main()`**

```python
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
        
```

Esta es la función que ejecuta el sistema. Carga los datos al inicio y luego, dependiendo de la opción seleccionada por el usuario, ejecuta las funciones correspondientes.

---

### 10. **Cómo funciona todo junto**

- Cuando inicias el programa, se ejecuta `main()`, que primero carga los datos de los archivos de ventas, inventario y vendedores.
- Luego, se muestra un menú con 10 opciones. El usuario selecciona una opción, y el sistema realiza la acción correspondiente (por ejemplo, registrar una venta o consultar el inventario).
- El sistema sigue ejecutándose hasta que el usuario elige la opción "10" para salir.

---
