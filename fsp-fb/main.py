from flask import Flask

app = Flask(__name__)
app.secret_key = "key"


@app.route('/')
@app.route('/index')
def index():
    return "Hello World"


if __name__ == '__main__':
    app.run(port=1001, debug=True)
