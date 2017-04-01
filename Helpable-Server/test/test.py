from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    return '', 452

app.run()