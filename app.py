from flask import Flask, render_template, request, jsonify
from gtts import gTTS
import os
from io import BytesIO

app = Flask(__name__)
queue = []

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
        name = queue.pop(0)
        return jsonify({"name": name})
    return jsonify({"name": None})

@app.route('/speak', methods=['POST'])
def speak():
    name = request.json.get("name")
    if name:
        tts = gTTS(f"Turno del cliente: {name}", lang='es')
        tts.save("static/audio.mp3")
        return jsonify({"audio_url": "/static/audio.mp3"})
    return jsonify({"error": "No name provided"}), 400

if __name__ == '__main__':
    app.run(debug=True)