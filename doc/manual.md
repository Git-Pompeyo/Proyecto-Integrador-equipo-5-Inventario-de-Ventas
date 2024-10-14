# Manual de Usuario - Sistema de Inventario y Ventas

## Introducción
Este sistema permite a los administradores y vendedores gestionar el inventario de productos y registrar las ventas de manera eficiente. El sistema también genera reportes detallados sobre las ventas y el inventario.

## Requisitos

Antes de usar el sistema, asegúrate de contar con:
- **Python 3.x**
- La biblioteca `tabulate` instalada. Puedes instalarla ejecutando:
  ```bash
  pip3 install tabulate
  ```

## Archivos Requeridos

Los siguientes archivos `.txt` deben estar en el mismo directorio que el archivo `main.py`:
- **`inventario.txt`**: Contiene información de los productos en inventario (modelo, nombre, cantidad).
- **`ventas.txt`**: Registra todas las ventas realizadas (vendedor, modelo, nombre, cantidad).
- **`vendedores.txt`**: Lista los vendedores registrados (ID, nombre).

## Instrucciones de Uso

### Ejecución del Programa

Para iniciar el sistema, ejecuta el siguiente comando en la terminal:
```bash
python3 main.py
```

### Menú Principal

Al ejecutar el programa, verás el siguiente menú en la consola:

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

Cada opción del menú te permite realizar diferentes acciones. A continuación se explican todas las opciones en detalle.

### 1) Registrar Venta

Este módulo permite registrar una venta. Sigue estos pasos:

1. Selecciona la opción **1** del menú principal.
2. Ingresa el **modelo del auto**.
3. Ingresa el **nombre del auto**.
4. Ingresa la **cantidad a vender** (solo números positivos).
5. Ingresa el **ID del vendedor** que realizó la venta.

El sistema validará que el producto exista en el inventario y que haya suficiente cantidad disponible. Si todo es correcto, la venta se registrará y el inventario se actualizará.

### 2) Agregar Producto al Inventario

Esta opción permite agregar nuevos productos o actualizar la cantidad de productos existentes en el inventario.

1. Selecciona la opción **2** del menú.
2. Ingresa el **modelo del auto**.
3. Ingresa el **nombre del auto**.
4. Ingresa la **cantidad** de productos a agregar (solo números positivos).

Si el producto ya existe en el inventario, se actualizará la cantidad. De lo contrario, el producto se agregará como un nuevo registro en el inventario.

### 3) Mostrar Inventario

Esta opción permite visualizar el inventario completo, mostrando los productos disponibles y la cantidad restante en formato de tabla.

1. Selecciona la opción **3** del menú.
2. Se mostrará una tabla con los **modelos**, **nombres**, y **cantidades** de todos los productos en inventario.

### 4) Consultar Datos de Ventas

Permite ver todas las ventas realizadas hasta el momento.

1. Selecciona la opción **4** del menú.
2. Se mostrará una tabla con las ventas, incluyendo el **vendedor**, **modelo**, **nombre**, y **cantidad** vendida.

### 5) Mostrar Reportes de Ventas por Vendedor o Artículo

Este módulo genera reportes específicos de ventas. Puedes elegir entre un reporte por vendedor o un reporte por artículo.

1. Selecciona la opción **5** del menú.
2. Elige una de las siguientes opciones:
   - **1**: Reporte por vendedor.
     - Ingresa el **ID del vendedor** para ver todas las ventas realizadas por ese vendedor.
   - **2**: Reporte por artículo.
     - Ingresa el **modelo del artículo** para ver cuántas ventas se han hecho de ese modelo.

### 6) Registrar Vendedor

Si necesitas agregar un nuevo vendedor, usa esta opción:

1. Selecciona la opción **6** del menú.
2. Ingresa el **ID del vendedor**.
3. Ingresa el **nombre del vendedor**.

El nuevo vendedor será registrado en el sistema y aparecerá en futuros reportes de ventas.

### 7) Mostrar Vendedores

Esta opción muestra una lista de todos los vendedores registrados en el sistema.

1. Selecciona la opción **7** del menú.
2. Verás una tabla con los **IDs** y **nombres** de los vendedores.

### 8) Mostrar Modelo Más Vendido

El sistema mostrará cuál ha sido el modelo más vendido hasta el momento.

1. Selecciona la opción **8** del menú.
2. Se mostrará el **modelo** y **nombre del auto** más vendido, junto con la **cantidad** de unidades vendidas.

### 9) Mostrar Vendedor Estrella

Este módulo muestra al vendedor que ha realizado la mayor cantidad de ventas.

1. Selecciona la opción **9** del menú.
2. El sistema mostrará el **ID** del vendedor estrella y la **cantidad** de ventas que ha realizado.

### 10) Salir

Para finalizar la ejecución del programa, selecciona la opción **10**.

---
### Ejemplos de Casos de Uso para las 10 Opciones del Menú
---

### **Opción 1: Registrar Venta**

#### Ejemplo:
Un cliente compra **2 unidades** del modelo **"Civic, Type R"** de **Honda**, y la venta es realizada por **Erika** (ID: A00841206).

1. Selecciona la opción **1** del menú.
2. Ingresa los siguientes valores cuando se te solicite:
   - Modelo: `Civic, Type R`
   - Nombre: **Honda**
   - Cantidad: **2**
   - ID del vendedor: **A00841206**

**Resultado esperado**: 
- El inventario se actualizará y la cantidad de **"Civic, Type R"** de **Honda** pasará de **25** a **23**.
- La venta se registrará en el archivo `ventas.txt`.

---

### **Opción 2: Agregar Producto al Inventario**

#### Ejemplo:
Llega un nuevo lote de **5 unidades** del modelo **"Corvette, Stingray"** de **Chevrolet**.

1. Selecciona la opción **2** del menú.
2. Ingresa los siguientes valores cuando se te solicite:
   - Modelo: `Corvette, Stingray`
   - Nombre: **Chevrolet**
   - Cantidad: **5**

**Resultado esperado**: 
- La cantidad de **Corvette, Stingray** en el inventario se actualizará, pasando de **6** a **11**.
- El archivo `inventario.txt` reflejará este cambio.

---

### **Opción 3: Mostrar Inventario**

#### Ejemplo:
1. Selecciona la opción **3** del menú.

**Resultado esperado**:
- El sistema mostrará una tabla con el inventario completo. Por ejemplo:
  ```plaintext
  Modelo                | Nombre         | Cantidad
  ------------------------------------------------
  Stradale, SF90        | Ferrari        | 12
  Spider, SF90          | Ferrari        | 12
  Mustang               | Ford           | 12
  Centodieci            | Bugatti        | 1
  Chiron Super Sport    | Bugatti        | 2
  Wrangler              | Jeep           | 14
  ...                   | ...            | ...
  ```

---

### **Opción 4: Consultar Datos de Ventas**

#### Ejemplo:
1. Selecciona la opción **4** del menú.

**Resultado esperado**:
- El sistema mostrará una tabla con todas las ventas registradas. Por ejemplo:
  ```plaintext
  Vendedor     | Modelo           | Nombre         | Cantidad
  ----------------------------------------------------------
  A01068085    | Centodieci       | Bugatti        | 2
  A00841206    | Wrangler         | Jeep           | 1
  A00840973    | Mustang          | Ford           | 1
  A00841748    | Challenger       | Dodge          | 1
  A00842194    | GT, AMG          | Mercedes-Benz  | 1
  ```

---

### **Opción 5: Mostrar Reportes de Ventas por Vendedor o por Artículo**

#### Reporte por Vendedor:
Supongamos que quieres ver las ventas realizadas por **Pompeyo** (ID: A01068085).

1. Selecciona la opción **5** del menú.
2. Elige **1** para el reporte por vendedor.
3. Ingresa el ID del vendedor: **A01068085**.

**Resultado esperado**:
- El sistema mostrará todas las ventas realizadas por Pompeyo:
  ```plaintext
  ID         | Vendedor   | Modelo     | Cantidad
  ----------------------------------------------
  A01068085  | Pompeyo    | Centodieci | 2
  ```

#### Reporte por Artículo:
Supongamos que quieres ver las ventas del modelo **"Wrangler"** de **Jeep**.

1. Selecciona la opción **5** del menú.
2. Elige **2** para el reporte por artículo.
3. Ingresa el modelo: **Wrangler**.

**Resultado esperado**:
- El sistema mostrará todas las ventas del modelo **Wrangler**:
  ```plaintext
  Modelo     | Vendedor     | Cantidad
  -------------------------------------
  Wrangler   | A00841206    | 1
  ```

---

### **Opción 6: Registrar Vendedor**

#### Ejemplo:
Se quiere registrar un nuevo vendedor llamado **Jorge** con el ID **A01012345**.

1. Selecciona la opción **6** del menú.
2. Ingresa los siguientes valores cuando se te solicite:
   - ID: **A01012345**
   - Nombre: **Jorge**

**Resultado esperado**:
- El nuevo vendedor **Jorge** será registrado en el archivo `vendedores.txt` y estará disponible para futuras ventas.

---

### **Opción 7: Mostrar Vendedores**

#### Ejemplo:
1. Selecciona la opción **7** del menú.

**Resultado esperado**:
- El sistema mostrará una tabla con todos los vendedores registrados:
  ```plaintext
  ID          | Nombre
  --------------------------
  A01068085   | Pompeyo
  A00841206   | Erika
  A00840973   | Andrea
  A00841748   | Fernanda
  A00842194   | Athenea
  ```

---

### **Opción 8: Mostrar Modelo Más Vendido**

#### Ejemplo:
1. Selecciona la opción **8** del menú.

**Resultado esperado**:
- El sistema calculará y mostrará el modelo más vendido. Por ejemplo:
  ```plaintext
  El modelo más vendido es "Centodieci" (Bugatti) con 2 unidades vendidas.
  ```

---

### **Opción 9: Mostrar Vendedor Estrella**

#### Ejemplo:
1. Selecciona la opción **9** del menú.

**Resultado esperado**:
- El sistema calculará y mostrará al vendedor con más ventas. Por ejemplo:
  ```plaintext
  El mayor vendedor es A01068085 (Pompeyo) con 2 ventas.
  ```

---

### **Opción 10: Salir**

#### Ejemplo:
1. Selecciona la opción **10** del menú.

**Resultado esperado**:
- El programa finalizará y se cerrará correctamente.
---

## Solución de Problemas

### Error: "No hay suficientes productos en el inventario"

Este error se produce cuando intentas vender más productos de los que hay en el inventario. Asegúrate de que la cantidad que deseas vender no exceda el inventario disponible.

### Error: "El archivo no se encontró"

Si ves este mensaje, verifica que los archivos `inventario.txt`, `ventas.txt`, y `vendedores.txt` estén en el mismo directorio que el archivo `main.py`.

### Error: "ID de vendedor no registrado"

Este error aparece si intentas registrar una venta con un ID de vendedor que no está registrado en el sistema. Asegúrate de registrar al vendedor primero usando la opción **6** del menú.

---

## Créditos

Este manual fue creado por el **Equipo 5** para el curso de Pensamiento Computacional para la Ingeniería, guiado por la profesora **Mayra Flores López**.

Los miembros del equipo son:
- Pompeyo Alexander Pérez Marín
- Athenea Méndez Cisneros
- Andrea Estefanía De la Peña Contreras
- Fernanda Santillán Dantes
- Erika Esquivel Correa
