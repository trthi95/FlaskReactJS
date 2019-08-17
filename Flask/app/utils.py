from .models import WebAPI
from flask import json

def save(query):
    print(query)
    WebAPI.save(query)

def getAll():
    data = WebAPI.getAll()
    return data

def delete_data(id):
    WebAPI.delete_data(id)
    
def edit_data(id_edit, data_edit):
    WebAPI.edit_data(id_edit, data_edit)
