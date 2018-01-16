from flask import Flask, render_template, request, redirect, url_for
from geopy.geocoders import Nominatim
import pandas
import datetime

app=Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")

@app.route("/templates/success", methods=['POST'])
def  success():
    global filename
    if request.method=='POST':
        data=request.files['data']
        try:
            df=pandas.read_csv(data)
            df['coordinates']=df["Address"].apply(gc.geocode)
            df['Latitude'] = df['coordinates'].apply(lambda x:x.latitude if x !None else None)
            df['Longitude'] = df['coordinates'].apply(lambda x:x.latitude if x !None else None)
            df=df.drop("coordinates")
            filename=datetime.datetime.now().strftime("uploads/+%Y-%m-%d-%H-%M-%S-%f"+".csv")
            df.to_csv(filename, index=None)
            return render_template('index.html', text=df.to_html(), btn='download.html')
        except:
            return render_template('index.html', text="Please enter file with address column")

@app.route("/download-file/")
def download():
    return send_file(filename, attachment_filename='your.csv', as_attachment=True)

if __name__=='__main__':
    app.debug=True
    app.run()
