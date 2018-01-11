from flask import Flask, render_template, request, redirect, url_for
import os

UPLOAD_FOLDER='C:\\Users\\Ira\\Desktop' # Do i need this ??
ALLOWED_EXTENSIONS = set(['txt','json','csv', 'py']) # Do i need this ??

app=Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")

@app.route("/templates/succcess", methods=['POST'])
def  upload():
    print("==== upload()")
    if request.method=='POST':
        print("==== POST")
        data = request.files['data']
        print(data)

        if '.' in data.filename and data.filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS:
            print("==== data.save()")
            data.save(os.path.join(app.config['UPLOAD_FOLDER'], data.filename))
            #return render_tempalte("success.html")
            print("==== redirect()")
            return redirect(url_for("index"))
        else:
            print("==== if did not work")


if __name__=='__main__':
    app.debug=True
    app.run()
