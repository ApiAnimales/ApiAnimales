# API ANIMALES

Este programa es una API que permite realizar operaciones básicas sobre una lista de animales. Permite obtener información de todos los animales, buscar un animal por su nombre, agregar un nuevo animal, actualizar la información de un animal existente y eliminar un animal de la lista.

## Autores

- Abella Betancourt Jorge Andres - 160004300
- Alferez Garcia Daniel Camilo - 160004302
- Torres Barreto Juan David - 160004330

## Instalación

1. Clona el repositorio o descarga el código fuente del programa.
2. Asegúrate de tener Python 3 instalado en tu sistema.
3. Instala las dependencias del programa ejecutando el siguiente comando en tu terminal:

pip install -r requirements.txt


## Uso

1. Ejecuta el programa utilizando el siguiente comando:

python app.py

2. La API estará disponible en `http://localhost:5000`.

## Endpoints

- `GET /animales`: Obtiene información de todos los animales.
- `GET /animales/{nombre}`: Obtiene información de un animal por su nombre.
- `POST /animales`: Agrega un nuevo animal.
- `PUT /animales/{nombre}`: Actualiza la información de un animal existente.
- `DELETE /animales/{nombre}`: Elimina un animal de la lista.

## Formato de los datos

Los datos de un animal están representados en formato JSON y contienen los siguientes campos:

- `nombre`: El nombre del animal.
- `especie`: La especie del animal.
- `alimentacion`: El tipo de alimentación del animal.
- `locomocion`: El tipo de locomoción del animal.
- `reproduccion`: El tipo de reproducción del animal.

## Ejemplos

- Obtener todos los animales:

```http
GET /animales
```

- Obtener un animal por su nombre (ejemplo: Leon):

```http
GET /animales/Leon
```

- Agregar un nuevo animal:

```http
POST /animales
Content-Type: application/json
```

```json
{
"nombre": "Gorila",
"especie": "Gorilla gorilla",
"alimentacion": "herbivoro",
"locomocion": "terrestre",
"reproduccion": "viviparo"
}
```

- Actualizar un animal por su nombre (ejemplo: León):

```http
PUT /animales/León
Content-Type: application/json
```

```json
{
"nombre": "León",
"especie": "Panthera leo",
"alimentacion": "carnívoro",
"locomocion": "terrestre",
"reproduccion": "vivíparo"
}
```

- Eliminar un animal por su nombre (ejemplo: León):

```http
DELETE /animales/León
```
