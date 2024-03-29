from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import json
import requests
import csv
from models import Asset
from models import db
from models import app
from models import ReferenceDevice

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

@app.route('/reference_devices', methods=['GET'])
def get_reference_devices():
  # Read the CSV file from local disk
  with open('H:/AI generated programs/EIT-v10/referencedevices.csv', 'r') as f:
   reader = csv.DictReader(f.readlines())
   for row in reader:
       new_device = ReferenceDevice(
           brand=row['Brand'],
           device_make=row['Device Make'],
           emission_impact=float(row['Emission Impact']))
       db.session.add(new_device)
   db.session.commit()
   return jsonify({"status": "OK"}), 201

@app.route('/refresh_reference_devices', methods=['GET'])
def get_refresh_reference_devices():
    url = 'https://raw.githubusercontent.com/Boavizta/environmental-footprint-data/main/boavizta-data-us.csv'
    response = requests.get(url)
    csv_data = response.text
    with open('referencedevices.csv', 'w') as f:
        f.write(csv_data) # Works, but does not enjoy fancy characters
    return jsonify({"status": "OK"}), 201

if __name__ == '__main__':
  app.run(port=6000)