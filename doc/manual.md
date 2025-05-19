# Manual de Usuario - Sistema de Inventario y Ventas

## Introducción
Este manual explica cómo usar el Sistema de Inventario y Ventas para gestionar productos y registrar ventas.

## Requisitos
- Python 3.x
- Biblioteca `tabulate`: Instalar con `pip3 install tabulate`
- Archivos en el mismo directorio: `inventario.txt`, `ventas.txt`, `vendedores.txt`

## Inicio
Para iniciar el sistema, ejecute: `python3 main.py`

## Menú Principal
```
=== SISTEMA DE INVENTARIO Y VENTAS ===
1) Registrar venta
2) Agregar producto al inventario
3) Mostrar inventario
4) Consultar datos de ventas
5) Mostrar reportes de ventas
6) Registrar vendedor
7) Mostrar vendedores
8) Mostrar modelo más vendido
9) Mostrar vendedor estrella
10) Salir
```

## Opciones del Menú

### 1) Registrar Venta
- Ingrese modelo, nombre, cantidad y ID del vendedor
- El sistema verifica existencia y disponibilidad

### 2) Agregar Producto
- Ingrese modelo, nombre y cantidad
- Actualiza productos existentes o agrega nuevos

### 3) Mostrar Inventario
- Muestra tabla con modelos, nombres y cantidades

### 4) Consultar Ventas
- Muestra todas las ventas realizadas

### 5) Reportes de Ventas
- **Por vendedor**: Ventas de un vendedor específico
- **Por artículo**: Ventas de un modelo específico

### 6) Registrar Vendedor
- Ingrese ID y nombre del nuevo vendedor

### 7) Mostrar Vendedores
- Lista todos los vendedores registrados

### 8) Modelo Más Vendido
- Muestra el modelo con mayor cantidad vendida

### 9) Vendedor Estrella
- Muestra el vendedor con más ventas realizadas

### 10) Salir
- Termina la ejecución del programa

## Solución de Problemas

- **"No hay suficientes productos"**: Verifique el inventario disponible
- **"Archivo no encontrado"**: Verifique que los archivos estén en el directorio correcto
- **"ID de vendedor no registrado"**: Registre al vendedor con la opción 6

## Créditos
Equipo 5:
- Pompeyo Alexander
- Athenea Méndez
- Andrea De la Peña
- Fernanda Dantes
- Erika Correa
