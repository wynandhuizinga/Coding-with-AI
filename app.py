from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import requests

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
app.app_context().push()

class Asset(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   device_type = db.Column(db.String(50))
   amount = db.Column(db.Float)

# Create the assets table
db.create_all()

@app.route('/assets', methods=['GET'])
def get_all_assets():
   assets = Asset.query.all()
   return jsonify(assets)

@app.route('/assets', methods=['POST'])
def create_new_asset():
   with open('asset.json') as f:
    data = json.load(f)
   asset = Asset(**data)
   db.session.add(asset)
   db.session.commit()
   return jsonify(data), 201

if __name__ == '__main__':
  app.run(port=6000)