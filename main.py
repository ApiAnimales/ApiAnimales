# API ANIMALES
# Abella Betancourt Jorge Andres 160004300
# Alferez Garcia Daniel Camilo   160004302
# Torres Barreto Juan David      160004330

from flask import Flask, jsonify, request
from typing import Union
from unidecode import unidecode 
app = Flask(__name__)

animales = [
    {
        "nombre": "León",
        "especie": "Panthera leo",
        "alimentacion": "carnívoro",
        "locomocion": "terrestre",
        "reproduccion": "vivíparo"
    },
    {
        "nombre": "Elefante",
        "especie": "Loxodonta africana",
        "alimentacion": "herbívoro",
        "locomocion": "terrestre",
        "reproduccion": "vivíparo"
    },
    {
        "nombre": "Tigre",
        "especie": "Panthera tigris",
        "alimentacion": "carnívoro",
        "locomocion": "terrestre",
        "reproduccion": "vivíparo"
    }
]
# Metodos para el manejo de datos
def buscar_animal_por_nombre(nombre) -> Union[int, dict]:
    """
        Busca animal por nombre sin importar mayusculas, minusculas, o acentos.
    """
    global animales
    indice, datos = None, dict()
    i = 0
    for animal in animales:
        if unidecode(animal["nombre"].lower()) == unidecode(nombre.lower()):
            indice = i
            datos = animal
            break
        i+=1
    return indice, datos

def validar_datos_animales(datos):
    campos = ["nombre", "especie", "alimentacion", "locomocion", "reproduccion"]
    if len(datos) != len(campos):
        return False 
    for campo in campos:
        if campo not in datos:
            return False
    return True
# End Points 
# Obtener todos los animales
@app.route('/animales', methods=['GET'])
def obtener_animales():
    return jsonify(animales), 200

# Obtener un animal por su nombre
@app.route('/animales/<string:nombre>', methods=['GET'])
def obtener_animal(nombre):
    indice, datos = buscar_animal_por_nombre(nombre)
    if indice!=None:
        return jsonify(datos), 200
    else:
        return jsonify({'mensaje': 'El animal no esta registrado'}), 404

# Agregar un nuevo animal
@app.route('/animales', methods=['POST'])
def agregar_animal():
    nuevo_animal = request.get_json()
    resultado = validar_datos_animales(nuevo_animal)
    if resultado == False:
        return jsonify({'mensaje': 'Animal requiere los campos: nombre, especie, alimentacion, locomocion, reproduccion'}), 400
    resultado, _ = buscar_animal_por_nombre(nuevo_animal["nombre"])
    if resultado != None:
        return jsonify({'mensaje': 'El Animal ya se encuentra registrado'}), 409
    animales.append(nuevo_animal)
    return jsonify({'mensaje': 'Animal agregado exitosamente'}), 201

# Actualizar un animal por su índice
@app.route('/animales/<string:nombre>', methods=['PUT'])
def actualizar_animal(nombre):
    animal_actualizado = request.get_json()
    resultado = validar_datos_animales(animal_actualizado)
    if resultado==False:
        return jsonify({'mensaje': 'Animal requiere los campos: nombre, especie, alimentacion, locomocion, reproduccion'}), 400
    indice, _ = buscar_animal_por_nombre(nombre)
    if indice!=None:
        animales[indice] = animal_actualizado
        return jsonify({'mensaje': 'Animal actualizado exitosamente'}), 200
    else:
        return jsonify({'mensaje': 'El Animal no se encuentra registrado'}), 404

# Eliminar un animal por su índice
@app.route('/animales/<string:nombre>', methods=['DELETE'])
def eliminar_animal(nombre):
    indice, _ = buscar_animal_por_nombre(nombre)
    if indice != None:
        animales.pop(indice)
        return jsonify({'mensaje': 'Animal eliminado exitosamente'}), 200
    else:
        return jsonify({'mensaje': 'Índice de animal no válido'}), 404

if __name__ == '__main__':
    app.run(debug=True)