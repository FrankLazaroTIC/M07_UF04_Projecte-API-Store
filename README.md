# Projecte Django REST FRAMEWORK: Api_Store

A través de esta API REST se realizarán las acciones más importantes propias de una tienda en línea, como la gestión de productos, su stock, el carrito de la compra, las órdenes y los pagos.

## Diseño del modelo relacional de las tablas de la base de datos:

### Tablas:

- **client**
- **producte**
- **carreto**
- **comanda**
- **pagament**

#### Tabla `client`:
- `id` (pk)
- `nom`
- `cognoms`
- `email`
- `password`

*Todos las tablas deben tener los campos de control `created_at` y `update_at` y deben ser utilizados correctamente.*

### Desarrollo de la API REST a través de Django

Este proyecto tendrá 4 aplicaciones:

### Catàleg (25 punts)
Gestión del catálogo de productos (mínimo 10 registros) (rama catalog).

#### Acciones:
- Añadir nuevos productos.
- Actualizar productos.
- Actualizar stock de productos.
- Eliminar productos mediante borrado lógico.
- Ver todos los productos.
- Ver información detallada de un producto.

#### Condiciones:
- La tabla `producte` debe tener mínimo 6 campos sin contar la `id` y los campos de control.
- CRUD de productos teniendo en cuenta las acciones indicadas.
- El borrado lógico implica "marcar" los productos como borrados.
  
#### Datos de retorno:
Cada acción debe retornar un JSON con al menos:
- Un estado indicando si ha sido exitoso.
- Un mensaje informando sobre la realización de la acción o indicando el error.

### Carretó (3 punts)
Gestión del carrito de productos que se quieren comprar (mínimo un carrito con 4 productos) (rama cart).

#### Acciones:
- Crear un nuevo carrito.
- Agregar productos al carrito.
- Eliminar productos del carrito mediante borrado físico.
- Eliminar todo el carrito mediante borrado físico.
- Modificar cantidad de un producto.
- Consultar el listado de productos del carrito.
- Comprar.

#### Funcionamiento:
- Relacionar el carrito con el cliente al crearlo.
- No se puede crear un carrito si ya existe uno abierto para ese cliente.
- Mientras el carrito esté abierto o no finalizado, se pueden realizar acciones propias del carrito.
- Después de la compra, el carrito pasa a un estado finalizado y no se puede modificar.
- Se crea un nuevo registro en la tabla de comanda con la información necesaria del carrito, que estará en un estado abierto.

#### Funcionalidades extras (5 puntos):
- Si un producto no tiene stock, informar que no se puede agregar al carrito.

#### Datos de retorno:
Cada acción debe retornar un JSON con al menos:
- Un estado indicando si la acción ha sido exitosa.
- Un mensaje informando sobre la realización de la acción o indicando el error.
- Información del carrito: lista de productos con nombre, unidades y precio por producto, y precio total del carrito.

### Comandes (2 punts)
Gestión de órdenes (repartir 10 registros entre cada estado) (rama orders).

#### Acciones:
- Mostrar historial de órdenes.
- Mostrar historial de órdenes por un cliente en concreto.
- Mostrar historial de órdenes que no están finalizadas.

#### Datos de retorno:
Cada acción debe retornar un JSON con al menos:
- Un estado indicando si la acción ha sido exitosa.
- Un mensaje informando sobre la realización de la acción o indicando el error.
- Información de la orden: ID de la orden, total de productos y precio total de la compra.

### Pagament (25 punts)
Gestión de pagos (simulado) (rama payments).

#### Acciones:
- Pagar una orden.
- Consultar estado de orden.

#### Funcionamiento:
- Para realizar el pago, se debe proporcionar el número de tarjeta, fecha de caducidad y CVC.
- El pago solo se puede realizar para órdenes abiertas.
- Primero se debe verificar si la orden que se desea pagar está abierta.
- Después de realizar la compra, la orden se actualiza a finalizada o cerrada.

#### Funcionalidades extras (5 puntos):
- Verificar mediante expresiones regulares que el formato del número de tarjeta proporcionado sea correcto.

#### Datos de retorno:
Cada acción debe retornar un JSON con al menos:
- Un estado indicando si la acción ha sido exitosa.
- Un mensaje informando sobre la realización de la acción o indicando el error.

**A tener en cuenta:** Se debe utilizar `@api_view`, `Response`, queries de base de datos y forms para realizar POSTS. No se requiere frontend, solo crear una API con DRF (Django Rest Framework).
# Projecte Django REST FRAMEWORK: Api_Store

A través de esta API REST se realizarán las acciones más importantes propias de una tienda en línea, como la gestión de productos, su stock, el carrito de la compra, las órdenes y los pagos.

## Diseño del modelo relacional de las tablas de la base de datos:

### Tablas:

- **client**
- **producte**
- **carreto**
- **comanda**
- **pagament**

#### Tabla `client`:
- `id` (pk)
- `nom`
- `cognoms`
- `email`
- `password`

*Todos las tablas deben tener los campos de control `created_at` y `update_at` y deben ser utilizados correctamente.*

### Desarrollo de la API REST a través de Django

Este proyecto tendrá 4 aplicaciones:

### Catàleg (25 punts)
Gestión del catálogo de productos (mínimo 10 registros) (rama catalog).

#### Acciones:
- Añadir nuevos productos.
- Actualizar productos.
- Actualizar stock de productos.
- Eliminar productos mediante borrado lógico.
- Ver todos los productos.
- Ver información detallada de un producto.

#### Condiciones:
- La tabla `producte` debe tener mínimo 6 campos sin contar la `id` y los campos de control.
- CRUD de productos teniendo en cuenta las acciones indicadas.
- El borrado lógico implica "marcar" los productos como borrados.
  
#### Datos de retorno:
Cada acción debe retornar un JSON con al menos:
- Un estado indicando si ha sido exitoso.
- Un mensaje informando sobre la realización de la acción o indicando el error.

### Carretó (3 punts)
Gestión del carrito de productos que se quieren comprar (mínimo un carrito con 4 productos) (rama cart).

#### Acciones:
- Crear un nuevo carrito.
- Agregar productos al carrito.
- Eliminar productos del carrito mediante borrado físico.
- Eliminar todo el carrito mediante borrado físico.
- Modificar cantidad de un producto.
- Consultar el listado de productos del carrito.
- Comprar.

#### Funcionamiento:
- Relacionar el carrito con el cliente al crearlo.
- No se puede crear un carrito si ya existe uno abierto para ese cliente.
- Mientras el carrito esté abierto o no finalizado, se pueden realizar acciones propias del carrito.
- Después de la compra, el carrito pasa a un estado finalizado y no se puede modificar.
- Se crea un nuevo registro en la tabla de comanda con la información necesaria del carrito, que estará en un estado abierto.

#### Funcionalidades extras (5 puntos):
- Si un producto no tiene stock, informar que no se puede agregar al carrito.

#### Datos de retorno:
Cada acción debe retornar un JSON con al menos:
- Un estado indicando si la acción ha sido exitosa.
- Un mensaje informando sobre la realización de la acción o indicando el error.
- Información del carrito: lista de productos con nombre, unidades y precio por producto, y precio total del carrito.

### Comandes (2 punts)
Gestión de órdenes (repartir 10 registros entre cada estado) (rama orders).

#### Acciones:
- Mostrar historial de órdenes.
- Mostrar historial de órdenes por un cliente en concreto.
- Mostrar historial de órdenes que no están finalizadas.

#### Datos de retorno:
Cada acción debe retornar un JSON con al menos:
- Un estado indicando si la acción ha sido exitosa.
- Un mensaje informando sobre la realización de la acción o indicando el error.
- Información de la orden: ID de la orden, total de productos y precio total de la compra.

### Pagament (25 punts)
Gestión de pagos (simulado) (rama payments).

#### Acciones:
- Pagar una orden.
- Consultar estado de orden.

#### Funcionamiento:
- Para realizar el pago, se debe proporcionar el número de tarjeta, fecha de caducidad y CVC.
- El pago solo se puede realizar para órdenes abiertas.
- Primero se debe verificar si la orden que se desea pagar está abierta.
- Después de realizar la compra, la orden se actualiza a finalizada o cerrada.

#### Funcionalidades extras (5 puntos):
- Verificar mediante expresiones regulares que el formato del número de tarjeta proporcionado sea correcto.

#### Datos de retorno:
Cada acción debe retornar un JSON con al menos:
- Un estado indicando si la acción ha sido exitosa.
- Un mensaje informando sobre la realización de la acción o indicando el error.

**A tener en cuenta:** Se debe utilizar `@api_view`, `Response`, queries de base de datos y forms para realizar POSTS. No se requiere frontend, solo crear una API con DRF (Django Rest Framework).
