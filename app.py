from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class Asset(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   device_type = db.Column(db.String(50))
   amount = db.Column(db.Float)

@app.route('/assets', methods=['GET'])
def get_all_assets():
   assets = Asset.query.all()
   return jsonify(assets)

@app.route('/assets', methods=['POST'])
def create_new_asset():
   data = request.get_json()
   asset = Asset(device_type=data.get('device_type'), amount=data.get('amount'))
   db.session.add(asset)
   db.session.commit()
   return jsonify(asset), 201

if __name__ == '__main__':
   app.run(port=6000)