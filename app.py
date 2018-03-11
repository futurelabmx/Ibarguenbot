from flask import Flask
from flask import render_template
from generator import *


# Simple Flask app:
app = Flask(__name__)


# Index:
@app.route("/")
def index():
    return render_template('index.html')


# Generate text:
@app.route("/generate", methods=['GET', 'POST'])
def generate():
    model = generate_model("../docs/lasmuertas.txt")
    text = model.make_short_sentence(250)
    print(text)
    return render_template('index.html', text=text)


# Main:
if __name__ == '__main__':
    app.run(debug=True)
