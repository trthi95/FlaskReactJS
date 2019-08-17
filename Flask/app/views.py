from flask import Blueprint, jsonify, request
from .utils import save, getAll, delete_data, edit_data
from .models import WebAPI
main = Blueprint('main', __name__)

@main.route('/add', methods = ['GET','POST','DELETE', 'PUT'])
def add():
    if request.method == 'GET':
        data_test =  getAll()
        print(data_test)
        datas = []
        for data in data_test:
            print(data.id," - ",data.data)
            data = {
                'id' : data.id,
                'data' : data.data 
            }
            datas.append(data)
        print(datas)
        print(type(data_test))
        return jsonify(datas)
        
    elif request.method == 'POST':
        data = request.get_json()
        query = data.get("data")
        save(query)
        return jsonify(data)

    elif request.method == 'DELETE':
        id_delete = request.get_json()
        id = id_delete.get('id')
        delete_data(id)
        return 'success'
    elif request.method == 'PUT':
        data_edit_json = request.get_json()
        id_edit = data_edit_json.get('id')
        data_edit = data_edit_json.get('data')
        edit_data(id_edit, data_edit)
        return jsonify(success=True)
# @main.route('/add', methods = ['GET'])
# def get():
#     query = 'test'
#     save(query)
#     return jsonify(query)