from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sendEmail import send_email
from sqlalchemy.sql import func

#SDFGHJKL;'GHJKLDFGHJKFGH'

app=Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:post@localhost/Height_collector'
app.config['SQLALCHEMY_DATABASE_URI']='postgres://cyahkqwmpjuqit:2fd19ea3e526ac35c15d56173a8c4af7067c2b7297dcdb6503596d6e6785cd47@ec2-107-21-224-61.compute-1.amazonaws.com:5432/d9s3k44g07tvpn?sslmode=require'
db=SQLAlchemy(app)   # Creates database for my webapp

class Data(db.Model):
    __tablename__="data"
    id=db.Column(db.Integer, primary_key=True)
    email_=db.Column(db.String(120), unique=True)    # This class creates the database, gives it name and properties.
    height_=db.Column(db.Integer)

    def __init__(self, email_, height_):
        self.email_=email_
        self.height_=height_

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/templates/success", methods=['POST'])
def success():
    if request.method=='POST':
        email=request.form["email_name"]
        height=request.form["height_name"]
        if db.session.query(Data).filter(Data.email_==email).count() == 0:  # Points to Data base class to fileter and stops duplication
            data=Data(email,height)
            db.session.add(data)
            db.session.commit()
            avg=db.session.query(func.avg(Data.height_)).scalar()
            avg=round(avg,2)
            count=db.session.query(Data.height_).count()
            send_email(email, height, avg, count)
            print(avg)
            return render_template("success.html")
    return render_template("index.html", text="We already have that email in our database")

if __name__=='__main__':
    app.debug=True
    app.run()
