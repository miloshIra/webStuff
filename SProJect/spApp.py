from flask import Flask, render_template, request, redirect, url_for
import os, csv

UPLOAD_FOLDER='C:\\Users\\Ira\\Desktop\\Snaik\\10 Apps Tutorial\\SproJect'
ALLOWED_EXTENSIONS = set(['txt','pdf','csv', 'py', 'jpg'])

app=Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

address=[]

@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")

@app.route("/templates/succcess", methods=['POST'])
def  upload():
    if request.method=='POST':
        data = request.files['data']
        if '.' in data.filename and data.filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS:
            data.save(os.path.join(app.config['UPLOAD_FOLDER'], data.filename))
            #return render_template("success.html")
            #return redirect(url_for("index"))
        #else:
            #return render_template("faliure.html")
        with open (data) as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                if row == 'address' or 'Address':
                    print(row)


if __name__=='__main__':
    app.debug=True
    app.run()
