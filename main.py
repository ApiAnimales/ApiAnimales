# Animales: {
# nombre, 
# especie, 
# alimentacion(carnivoro, herbivoro ...), 
# locomocion(aereo, terrestre, acuatico, ...), 
# reproduccion (oviparo, viviparo, ...), 
# }

from flask import Flask, jsonify, request

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

# Obtener todos los animales
@app.route('/animales', methods=['GET'])
def obtener_animales():
    return jsonify(animales)

# Obtener un animal por su índice
@app.route('/animales/<int:indice>', methods=['GET'])
def obtener_animal(indice):
    if indice >= 0 and indice < len(animales):
        return jsonify(animales[indice])
    else:
        return jsonify({'mensaje': 'Índice de animal no válido'})

# Agregar un nuevo animal
@app.route('/animales', methods=['POST'])
def agregar_animal():
    nuevo_animal = request.get_json()
    animales.append(nuevo_animal)
    return jsonify({'mensaje': 'Animal agregado exitosamente'})

# Actualizar un animal por su índice
@app.route('/animales/<int:indice>', methods=['PUT'])
def actualizar_animal(indice):
    if indice >= 0 and indice < len(animales):
        animal_actualizado = request.get_json()
        animales[indice] = animal_actualizado
        return jsonify({'mensaje': 'Animal actualizado exitosamente'})
    else:
        return jsonify({'mensaje': 'Índice de animal no válido'})

# Eliminar un animal por su índice
@app.route('/animales/<int:indice>', methods=['DELETE'])
def eliminar_animal(indice):
    if indice >= 0 and indice < len(animales):
        animales.pop(indice)
        return jsonify({'mensaje': 'Animal eliminado exitosamente'})
    else:
        return jsonify({'mensaje': 'Índice de animal no válido'})

if __name__ == '__main__':
    app.run(debug=True)