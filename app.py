from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import json
import requests
from models import Asset
from models import db
from models import app

db.create_all()

@app.route('/assets', methods=['GET'])
def get_all_assets():
  assets = Asset.query.all()
  asset_list = []
  for asset in assets:
   asset_dict = {'id': asset.id, 'device_type': asset.device_type, 'amount': asset.amount}
   asset_list.append(asset_dict)
  return jsonify(asset_list)

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