# Sistema de Inventario y Ventas

## Descripción

El **Sistema de Inventario y Ventas** es una herramienta diseñada para gestionar el inventario y las ventas de un establecimiento comercial. Este sistema permite a los administradores y vendedores:

- Registrar ventas y actualizar el inventario.
- Consultar el inventario y las ventas realizadas.
- Generar reportes de ventas detallados, tanto por vendedor como por artículo.

El programa es fácil de usar y asegura que los datos ingresados sean validados y consistentes.

### Características principales:
- **Registrar ventas**: Asegura que los productos vendidos se resten del inventario.
- **Agregar productos al inventario**: Gestiona nuevas llegadas de productos.
- **Generar reportes**: Reportes detallados por vendedor o artículo vendido.
- **Mostrar el producto más vendido y el vendedor estrella**.

---

## Tabla de Contenidos
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Estructura de Archivos](#estructura-de-archivos)
- [Contribuir](#contribuir)
- [Créditos](#créditos)
- [Licencia](#licencia)

---

## Requisitos

El sistema requiere Python 3.x y la instalación de la biblioteca `tabulate` para generar tablas en consola.

### Dependencias:
- **Python 3.x**
- **tabulate**: Para mostrar los datos en formato de tabla.

Instala las dependencias ejecutando:

```bash
pip3 install tabulate
```

---

## Instalación

1. Clona este repositorio:

   ```bash
   git clone https://github.com/tuusuario/tu-repositorio.git
   cd tu-repositorio
   ```

2. Asegúrate de tener **Python 3** instalado.

3. Instala las dependencias necesarias:
   ```bash
   pip3 install tabulate
   ```

4. Coloca los archivos de datos (`inventario.txt`, `ventas.txt`, `vendedores.txt`) en el directorio `data/`.

---

## Uso

### Ejecución del programa

Para ejecutar el programa, simplemente corre el siguiente comando:

```bash
python3 src/main.py
```

### Menú Principal

Al ejecutar el programa, verás el siguiente menú:

```plaintext
=== SISTEMA DE INVENTARIO Y VENTAS ===
1) Registrar venta
2) Agregar producto al inventario
3) Mostrar inventario
4) Consultar datos de ventas
5) Mostrar reportes de ventas por vendedor o por artículo
6) Registrar vendedor
7) Mostrar vendedores
8) Mostrar modelo más vendido
9) Mostrar vendedor estrella
10) Salir
```

Cada opción del menú te guiará en la acción correspondiente. 

### Ejemplo de uso

- **Registrar una venta**: Selecciona la opción 1, ingresa el modelo, nombre del producto, cantidad vendida y el ID del vendedor.
- **Consultar inventario**: Selecciona la opción 3 para ver el inventario actual.

---

## Estructura de Archivos

```plaintext
├── src/                          # Código fuente
│   └── main.py                   # Archivo principal
├── data/                         # Archivos de datos
│   ├── inventario.txt            # Inventario de productos
│   ├── vendedores.txt            # Información de vendedores
│   └── ventas.txt                # Registro de ventas
├── docs/                         # Documentación adicional
│   └── manual.md                 # Manual de usuario
└── README.md                     # Este archivo
```

---

## Créditos

Este proyecto fue desarrollado por el Equipo 5:
- Pompeyo Alexander Pérez Marín
- Athenea Méndez Cisneros
- Andrea Estefanía De la Peña Contreras
- Fernanda Santillán Dantes
- Erika Esquivel Correa

Agradecimientos especiales a la profesora **Mayra Flores López** por su orientación en el curso de Pensamiento Computacional para la Ingeniería.

---

## Licencia

Este proyecto está bajo la [Licencia MIT](LICENSE).
```
