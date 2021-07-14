
from Actividad6 import cargarPreguntas
from flask import Flask, render_template, request, redirect, jsonify
import json



app = Flask(__name__)

PATH_IN = r'static\data\preguntas.json'

@app.route('/')
def index():
    return render_template('matrix.html')

@app.route('/get-json', methods=['GET', 'POST'])
def get_json():
    #Generar JSON
    import Actividad6
    cargarPreguntas()
    # Importar datos
    with open(PATH_IN) as f:
        json_to = json.load(f)
    return jsonify(json_to)   


if __name__ == '__main__':
    app.run(debug=True, port=5000)


