# Explicación del Código - Sistema de Inventario y Ventas

## Estructura General

Este programa gestiona inventario y ventas usando Python. Su organización incluye:

## 1. Librerías y Archivos

```python
from tabulate import tabulate
import csv
import sys

# Archivos de datos
VENDEDORES_FILE = "vendedores.txt"
VENTAS_FILE = "ventas.txt"
INVENTARIO_FILE = "inventario.txt"
```

## 2. Componentes Principales

### Estructuras de Datos
- **`inventario[]`**: Lista de productos disponibles
- **`ventas[]`**: Registro de transacciones
- **`vendedores[]`**: Registro de vendedores

### Funciones de Importación
- **`importar_ventas()`**: Carga datos de ventas desde archivo
- **`importar_vendedores()`**: Carga datos de vendedores
- **`importar_inventario()`**: Carga datos de inventario

### Funciones Operativas
- **`agregar_venta()`**: Registra venta y actualiza inventario
- **`agregar_producto()`**: Añade o actualiza productos
- **`consultar_inventario()`**: Muestra productos disponibles
- **`consultar_ventas_general()`**: Muestra todas las ventas
- **`reporte_ventas_por_vendedor()`**: Filtra ventas por vendedor
- **`reporte_ventas_por_articulo()`**: Filtra ventas por modelo
- **`registrar_vendedor()`**: Añade nuevo vendedor
- **`mostrar_vendedores()`**: Lista vendedores registrados
- **`modelo_mas_vendido()`**: Calcula producto más popular
- **`vendedor_estrella()`**: Identifica vendedor con más ventas

### Menú y Control
- **`menu()`**: Muestra opciones y captura selección
- **`main()`**: Función principal que coordina el flujo del programa

## 3. Flujo de Ejecución

1. El programa inicia en `main()`, cargando datos desde archivos
2. Muestra menú de opciones (1-10)
3. Ejecuta la función correspondiente a la opción elegida
4. Regresa al menú después de cada operación
5. Termina cuando el usuario selecciona "Salir" (opción 10)

## 4. Validaciones Implementadas

- Verifica cantidades positivas para ventas e inventario
- Confirma existencia de productos antes de vender
- Valida que haya suficiente inventario
- Verifica que el vendedor esté registrado

## 5. Persistencia de Datos

- Los datos se almacenan en archivos externos (txt)
- Los cambios se guardan automáticamente después de operaciones
