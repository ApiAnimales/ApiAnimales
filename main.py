# Animales: {
# nombre, 
# especie, 
# alimentacion(carnivoro, herbivoro ...), 
# locomocion(aereo, terrestre, acuatico, ...), 
# reproduccion (oviparo, viviparo, ...), 
# }

from flask import Flask, jsonify, json

app = Flask(__name__)

@app.route('/api/', methods=['GET'])
def getAnimals():
    with open('data.json','r') as archivo:
        datos = json.load(archivo)
    return datos

if __name__ == '__main__':
    app.run(debug=True)


