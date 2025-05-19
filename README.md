# Sistema de Inventario y Ventas

## Descripción
El **Sistema de Inventario y Ventas** es una herramienta diseñada para gestionar el inventario y las ventas de un establecimiento comercial. Este sistema permite a los administradores y vendedores:
- Registrar ventas y actualizar el inventario automáticamente
- Consultar el inventario y las ventas realizadas
- Generar reportes detallados, tanto por vendedor como por artículo

### Características principales:
- **Registrar ventas**: Asegura que los productos vendidos se resten del inventario
- **Agregar productos al inventario**: Gestiona nuevas llegadas de productos
- **Generar reportes**: Reportes detallados por vendedor o artículo vendido
- **Estadísticas**: Muestra el producto más vendido y el vendedor estrella

## Inicio Rápido

### Requisitos
- Python 3.x
- Biblioteca `tabulate`: `pip3 install tabulate`

### Ejecución
1. Asegura que los archivos (`inventario.txt`, `ventas.txt`, `vendedores.txt`) estén en el mismo directorio que `main.py`
2. Ejecuta: `python3 main.py`

## Documentación

Este repositorio incluye documentación detallada para diferentes audiencias:

- [**Manual de Usuario**](./Manual.md): Guía completa con instrucciones paso a paso y ejemplos de uso para usuarios finales
- [**Explicación del Código**](./Explicacioncodigo.md): Documentación técnica que explica la implementación para desarrolladores

## Estructura de Archivos
```
├── main.py              # Archivo principal del sistema
├── inventario.txt       # Datos de inventario
├── vendedores.txt       # Registro de vendedores
├── ventas.txt           # Historial de ventas
├── README.md            # Este archivo
├── Manual.md            # Manual de usuario detallado
└── Explicacioncodigo.md # Explicación técnica del código
```

## Créditos
Desarrollado por el Equipo 5:
- Pompeyo Alexander Pérez Marín
- Athenea Méndez Cisneros
- Andrea Estefanía De la Peña Contreras
- Fernanda Santillán Dantes
- Erika Esquivel Correa

Agradecimientos especiales a la profesora **Mayra Flores López** por su orientación en el curso de Pensamiento Computacional para la Ingeniería.
