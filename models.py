from flask_sqlalchemy import SQLAlchemy

from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
app.app_context().push()

class Asset(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   device_type = db.Column(db.String(50))
   amount = db.Column(db.Float)

   def to_dict(self):
       return {'id': self.id, 'device_type': self.device_type, 'amount': self.amount}

class ReferenceDevice(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   brand = db.Column(db.String(50))
   device_make = db.Column(db.String(50))
   emission_impact = db.Column(db.Float)