from flask import Flask, request, jsonify
from bson.json_util import dumps
from bson.objectid import ObjectId
import db
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/medicamentos/<code>", methods=['GET'])
def get_medicamento(code):
    con = db.get_connection()
    dbmov = con.dbmovies
    try:
        medicamentos = dbmov.medicamentos
        response = app.response_class(
            response=dumps(medicamentos.find_one({'_id': ObjectId(code)})),
            status=200,
            mimetype='application/json'
        )
        return response
    finally:
        con.close()
        print("Connection closed")

@app.route("/medicamentos", methods=['GET'])
def get_medicamentos():
    con = db.get_connection()
    dbmov = con.dbmovies
    try:
        medicamentos = dbmov.medicamentos
        response = app.response_class(
            response=dumps(
                medicamentos.find()
            ),
            status=200,
            mimetype='application/json'
        )
        return response
    finally:
        con.close()
        print("Connection closed")

@app.route("/medicamentos", methods=['POST'])
def create():
    data = request.get_json()
    con = db.get_connection()
    dbmov = con.dbmovies 
    try:
        medicamentos = dbmov.medicamentos
        medicamentos.insert_one(data)
        return jsonify({"message":"OK"})
    finally:
        con.close()
        print("Connection closed")

@app.route("/medicamentos/<code>", methods=['PUT'])
def update(code):
    data = request.get_json()
    con = db.get_connection()
    dbmov = con.dbmovies
    try:
        medicamentos = dbmov.medicamentos
        medicamentos.replace_one(
            {'_id': ObjectId(code)},
            data, True
        )
        return jsonify({"message":"OK"})
    finally:
        con.close()
        print("Connection closed")

@app.route("/medicamentos/<code>", methods=['DELETE'])
def delete(code):
    con = db.get_connection()
    dbmov = con.dbmovies
    try:
        medicamentos = dbmov.medicamentos
        medicamentos.delete_many({'_id': ObjectId(code)})
        return jsonify({"message":"OK"})
    finally:
        con.close()
        print("Connection closed")

@app.route("/inventario/<code>", methods=['GET'])
def get_inventario(code):
    con = db.get_connection()
    dbmov = con.dbmovies
    try:
        inventario = dbmov.inventario
        response = app.response_class(
            response=dumps(inventario.find_one({'_id': ObjectId(code)})),
            status=200,
            mimetype='application/json'
        )
        return response
    finally:
        con.close()
        print("Connection closed")

@app.route("/inventario", methods=['GET'])
def get_inventarios():
    con = db.get_connection()
    dbmov = con.dbmovies
    try:
        inventario = dbmov.inventario
        response = app.response_class(
            response=dumps(
                inventario.find()
            ),
            status=200,
            mimetype='application/json'
        )
        return response
    finally:
        con.close()
        print("Connection closed")

@app.route("/inventario", methods=['POST'])
def create_inventario():
    data = request.get_json()
    con = db.get_connection()
    dbmov = con.dbmovies 
    try:
        inventario = dbmov.inventario
        inventario.insert_one(data)
        return jsonify({"message":"OK"})
    finally:
        con.close()
        print("Connection closed")

@app.route("/inventario/<code>", methods=['PUT'])
def update_inventario(code):
    data = request.get_json()
    con = db.get_connection()
    dbmov = con.dbmovies
    try:
        inventario = dbmov.inventario
        inventario.replace_one(
            {'_id': ObjectId(code)},
            data, True
        )
        return jsonify({"message":"OK"})
    finally:
        con.close()
        print("Connection closed")

@app.route("/inventario/<code>", methods=['DELETE'])
def delete_inventario(code):
    con = db.get_connection()
    dbmov = con.dbmovies
    try:
        inventario = dbmov.inventario
        inventario.delete_many({'_id': ObjectId(code)})
        return jsonify({"message":"OK"})
    finally:
        con.close()
        print("Connection closed")

