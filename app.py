from flask import Flask, render_template, request, jsonify
from gtts import gTTS
import os

app = Flask(__name__)
queue = []  # Se mantiene global y persistente durante ejecución del servidor

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/attend')
def attend():
    return render_template('attend.html')

@app.route('/add_name', methods=['POST'])
def add_name():
    name = request.json.get('name')
    if name:
        queue.append(name)
        return jsonify({"status": "ok", "queue": queue})
    return jsonify({"status": "error"}), 400

@app.route('/next', methods=['GET'])
def next_client():
    if queue:
        name = queue.pop(0)  # Quita al primer cliente de la cola
        return jsonify({"name": name})
    return jsonify({"name": None})

@app.route('/speak', methods=['POST'])
def speak():
    name = request.json.get("name")
    if name:
        tts = gTTS(f"Turno del cliente: {name}", lang='es')
        audio_path = "static/audio.mp3"
        tts.save(audio_path)
        return jsonify({"audio_url": "/" + audio_path})
    return jsonify({"error": "No name provided"}), 400

@app.route('/get_queue', methods=['GET'])
def get_queue():
    return jsonify({"queue": queue})


if __name__ == '__main__':
    app.run(debug=True)
