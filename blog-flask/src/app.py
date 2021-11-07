from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello my creation!"







if __name__ == '__main__':
    app.run(port=1000)
