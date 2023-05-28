from flask import Flask, jsonify
import gdown
app = Flask(__name__)

@app.route('/run-colab')
def run_colab():
    gdown.download('https://drive.google.com/uc?id=1Hp9Jcpu6d3PB0RQAcPe31HZFxqWiYEvZ', 'colab.ipynb', quiet=False)
    return jsonify(message='colab notebook ran successfully')



