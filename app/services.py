from flask import Flask, jsonify, render_template
import simpleaudio as sa
import time

app = Flask(__name__)

last_time = time.time()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/doorbell/")
def ring_doorbell():
    if time.time() - last_time() > 1:
        return
    last_time = time.time()
    wave_obj = sa.WaveObject.from_wave_file("app/doorbell-223669.wav")
    play_obj = wave_obj.play()
    return jsonify({'message': 'Ding Dong!', 'status': 200})
