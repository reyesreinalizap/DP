import os
from datetime import datetime
from flask import Flask,render_template,url_for,flash,redirect,abort,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.secret_key="Secret Key"

app.config['SQLALCHEMY_DATABASE_URI']='mysql://db_admin:db_admin@localhost/lifevest'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

db=SQLAlchemy(app)

class Passenger(db.Model):
    __tablename__='passenger'
    id = db.Column(db.Integer, primary_key=True)
    rfid = db.Column(db.String(20), unique =True, nullable = False)
    name = db.Column(db.String(35), unique = True, nullable = False)
    age = db.Column(db.Integer, unique = False, nullable=True)
    gender = db.Column(db.String(8), unique = False, nullable=True)
    contact = db.Column(db.String(18), unique = False, nullable=True)
    address = db.Column(db.String(50), unique = False, nullable=True)
    lat = db.Column(db.Float, unique = False, nullable=True )
    longi = db.Column(db.Float, unique = False, nullable=True)
    pulse = db.Column(db.Float, unique = False, nullable=True)
    status = db.Column(db.Boolean, unique = False, nullable=True)
    destination = db.Column(db.String(18), unique = False, nullable=False)
    dept_time = db.Column(db.DateTime, nullable=True, default=datetime.now, unique=False)
    post_time = db.Column(db.DateTime, nullable=True, default=datetime, unique=True)
    arrival_time = db.Column(db.DateTime, nullable=True, default=datetime, unique=True)

def __repr__(self):
        return f"Passenger('{self.rfid}', '{self.name}', '{self.age}', '{self.gender}','{self.contact}', '{self.address}', '{self.lat}', '{self.longi}', '{self.pulse}', '{self.status}', '{self.destination}', '{self.dept_time}', '{self.post_time}', '{self.arrival_time}')"
    
@app.route('/')
def index():
    passengers= Passenger.query.all()
    return render_template('index.html', title='Home',passengers=passengers)

@app.route('/insert', methods = ['GET','POST'])
def insert():
    if request.form:
        rfid = request.form['rfid']
        name = request.form['name']
        age = request.form['age']
        gender = request.form['gender']
        contact = request.form['contact']
        address = request.form['address']

        passenger = Passenger(rfid=request.form.get('rfid'),name=request.form.get('name'),age=request.form.get('age'),gender=request.form.get('gender'),contact=request.form.get('contact'),address=request.form.get('address'))
        db.session.add(passenger)
        db.session.commit()

        return redirect(url_for('index')) 
    return render_template("index.html")


@app.route('/delete/<rfid>/', methods = ['GET', 'POST'])
def delete(rfid):
    passenger = Passenger.query.filter_by(rfid=rfid).first_or_404()
    db.session.delete(passenger)
    db.session.commit()
    return redirect(url_for('index')) 


if __name__ == "__main__":
    app.run(debug=True)
