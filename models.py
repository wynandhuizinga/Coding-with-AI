from flask_sqlalchemy import SQLAlchemy

from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
app.app_context().push()

class Asset(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   manufacturer = db.Column(db.String(50))
   name = db.Column(db.String(255))
   amount = db.Column(db.Integer)
   
   def __getitem__(self, key):
      if key == "manufacturer":
          return self.manufacturer
      elif key == "name":
          return self.name
      else:
          raise AttributeError("Attribute '%s' not found on object of type Asset" % key)
      
   def to_dict(self):
       return {'id': self.id, 'device_type': self.device_type, 'amount': self.amount}

class ReferenceDevice(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   manufacturer = db.Column(db.String(50))
   name = db.Column(db.String(255))
   category = db.Column(db.String(50))
   subcategory = db.Column(db.String(50))
   lifetime = db.Column(db.Float)
   gwp_total = db.Column(db.Float)
   gwp_use_ratio = db.Column(db.Float)
   gwp_manufacturing_ratio = db.Column(db.Float)
   gwp_transport_ratio = db.Column(db.Float)
   gwp_eol_ratio = db.Column(db.Float)
   gwp_electronics_ratio = db.Column(db.Float)
   gwp_battery_ratio = db.Column(db.Float)
   gwp_hdd_ratio = db.Column(db.Float)
   gwp_ssd_ratio = db.Column(db.Float)
   gwp_othercomponents_ratio = db.Column(db.Float)
   