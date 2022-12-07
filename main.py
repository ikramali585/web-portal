
from flask import Flask, render_template ,request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
local_server="TRUE"
if(local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:@localhost/geocoordinates"
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:@localhost/geocoordinates"
db = SQLAlchemy(app)
class Coordinates(db.Model):
    '''
    sr, Latitude,Longitude
    '''
    sr = db.Column(db.Integer, primary_key=True)
    Latitude= db.Column(db.Integer, nullable=False)
    Longitude= db.Column(db.Integer, nullable=False)
    

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/test', methods = ['GET', 'POST'])
def Test():
    if(request.method=='POST'):
        '''Add entry to the database'''
        Latitude= (request.form.get('latitude'))
        Longitude = (request.form.get('longitude'))
        print(Longitude, Latitude)
        entry = Coordinates(Latitude=Latitude,Longitude=Longitude)
        db.session.add(entry)
        db.session.commit() 
    return render_template("test.html")


if __name__ == '__main__':
    app.debug = True
    app.run()

