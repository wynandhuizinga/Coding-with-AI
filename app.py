from flask import Flask, jsonify, request
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

@app.route('/assets', methods=['GET'])
def get_all_assets():
  assets = Asset.query.all()
  asset_list = []
  for asset in assets:
   asset_dict = {'id': asset.id, 'manufacturer': asset.manufacturer, 'name': asset.name, 'amount': asset.amount}
   asset_list.append(asset_dict)
  return jsonify(asset_list), 201, {"Access-Control-Allow-Origin": "*"}

@app.route('/total_gwp', methods=['GET'])
def get_gwp_totals():
  asset_ids = Asset.query.all()
  gwp_totals = 0.0
  for asset in asset_ids:
      reference_device = ReferenceDevice.query.filter_by(manufacturer=asset['manufacturer'], name=asset['name']).first()
      if reference_device:
          gwp_totals += reference_device.gwp_total * asset.amount / reference_device.lifetime
  km_driven_comp = gwp_totals * float(4.18429) # source: https://www.epa.gov/energy/greenhouse-gas-equivalencies-calculator --> converted 2.6 miles to km (=4.18...)
  message = str("Total global warming potential of your CMDB: ") + str(round(gwp_totals, 2)) + str(" kgCO2eq over the entire lifetime of all assets combined.") + str("\n This is equivalent to ") + str(round(km_driven_comp, 2)) + str(" km driving with a personnel vehicle")
  return jsonify(message), 201, {"Access-Control-Allow-Origin": "*"}

@app.route('/assets', methods=['POST'])
def create_new_asset():
    data = request.get_json()
    asset = Asset(manufacturer=data['manufacturer'], name=data['name'], amount=data['amount'], )
    db.session.add(asset)
    db.session.commit()
    return jsonify({'message': 'Asset created successfully.'}), 201, {"Access-Control-Allow-Origin": "*"}

@app.route('/reference_devices', methods=['GET'])
def get_reference_devices():
   try:
       df = pd.read_csv('H:/AI generated programs/EIT-v10/referencedevices.csv', encoding='Latin-1')
       if len(df.dropna()) > 0:
           raise ValueError("Could not parse CSV file: {0}".format(len(df.dropna())))
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
       return jsonify({"message": "OK"}), 201, {"Access-Control-Allow-Origin": "*"}
   except Exception as e:
       print("An error occurred: ", str(e))
       return jsonify({"message": "FAILED"}), 500, {"Access-Control-Allow-Origin": "*"}

@app.route('/refresh_reference_devices', methods=['GET'])
def get_refresh_reference_devices():
   url = 'https://raw.githubusercontent.com/Boavizta/environmental-footprint-data/main/boavizta-data-us.csv'
   response = requests.get(url)
   csv_data = response.text
   with codecs.open('referencedevices.csv', 'w') as f:
       f.write(csv_data)
   return jsonify({"message": "OK"}), 201, {"Access-Control-Allow-Origin": "*"}

if __name__ == '__main__':
  app.run(port=80)
