from flask import Flask, jsonify
import simpleaudio as sa

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/doorbell/")
def ring_doorbell():
    wave_obj = sa.WaveObject.from_wave_file("app/doorbell-223669.wav")
    play_obj = wave_obj.play()
    data = {'message': 'Success', 'status':200}
    return jsonify(data)