from flask import Flask



app = Flask(__name__)
app.secret_key = "Ira"


@app.route('/')
def home():
    return "Home page"

if __name__=='__main__':
    app.run(port=1000, debug=True)
