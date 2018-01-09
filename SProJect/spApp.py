from flask import Flask, render_template, request, redirect, url_for
import os

UPLOAD_FOLDER='/' # Do i need this ??
ALLOWED_EXTENSIONS = set(['txt','json','csv']) # Do i need this ??

app=Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")

@app.route("/templates/succcess", methods=['POST', 'GET'])
def  upload():
    if request.method=='POST':
        data=request.form['data']
        if data.rsplit('.',1)[1] in ALLOWED_EXTENSIONS:
            data.save(os.path.join(app.config['UPLOAD_FOLDER'], data))
            return render_tempalte("success.html")


if __name__=='__main__':
    app.debug=True
    app.run()
