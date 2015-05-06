from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap


app = Flask(__name__)

def create_app():
    Bootstrap(app)
    return app

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8001)
