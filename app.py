from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import json
import requests
import csv
import logging
import pandas as pd
import codecs
import io
from models import Asset
from models import db
from models import app
from models import ReferenceDevice

db.create_all()
# logging.basicConfig(filename='error.log', level=logging.ERROR)


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
   try:
       # Read the CSV file from local disk
       df = pd.read_csv('H:/AI generated programs/EIT-v10/referencedevices.csv', encoding='Latin-1')
       # df.str.replace(old='0xa0', new='') # bad fix

       # Check if there are any errors in the CSV file
       if len(df.dropna()) > 0:
           raise ValueError("Could not parse CSV file: {0}".format(len(df.dropna())))

       # Insert each row into the database
       for index, row in df.iterrows():
           new_device = ReferenceDevice(
               manufacturer=row['manufacturer'],
               name=row['name'],
               category=row['category'],
               subcategory=row['subcategory'],
               lifetime=float(row['lifetime']),
               gwp_total=float(row['gwp_total']),
               gwp_use_ratio=float(row['gwp_use_ratio']),
               gwp_manufacturing_ratio=float(row['gwp_manufacturing_ratio']),
               gwp_transport_ratio=float(row['gwp_transport_ratio']),
               gwp_eol_ratio=float(row['gwp_eol_ratio']),
               gwp_electronics_ratio=float(row['gwp_electronics_ratio']),
               gwp_battery_ratio=float(row['gwp_battery_ratio']),
               gwp_hdd_ratio=float(row['gwp_hdd_ratio']),
               gwp_ssd_ratio=float(row['gwp_ssd_ratio']),
               gwp_othercomponents_ratio=float(row['gwp_othercomponents_ratio']))
           db.session.add(new_device)
           db.session.commit()
       return jsonify({"status": "OK"}), 201
   except Exception as e:
       print("An error occurred: ", str(e))
       return jsonify({"status": "FAILED"}), 500

@app.route('/refresh_reference_devices', methods=['GET'])
def get_refresh_reference_devices():
   url = 'https://raw.githubusercontent.com/Boavizta/environmental-footprint-data/main/boavizta-data-us.csv'
   response = requests.get(url)
   csv_data = response.text
   with codecs.open('referencedevices.csv', 'w') as f:
       f.write(csv_data)
   return jsonify({"status": "OK"}), 201

if __name__ == '__main__':
  app.run(port=6000)
