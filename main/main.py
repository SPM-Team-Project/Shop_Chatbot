from flask import Flask
from model import Customer


app = Flask(__name__)


@app.route('/')
def index():
    return ""


if __name__ == '__main__':
    app.run()