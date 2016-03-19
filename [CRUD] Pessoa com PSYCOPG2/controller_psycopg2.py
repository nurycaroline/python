from flask import render_template, request,flash, redirect, url_for, jsonify,abort, request, make_response, json
from model_psycopg2 import Pessoa, app
import psycopg2
import sys

#---------------------------------------------------
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

#---------------------------------------------------
db = None
db = psycopg2.connect(database='teste', user='postgres', password='postgres', port='5470')
cursor = db.cursor()


#READ
@app.route('/pessoas', methods=['GET'])
def pessoa_index():
    cursor.execute("SELECT * FROM pessoa ")
    pessoas = cursor.fetchall()
    
    rowarray_list = []
    for p in pessoas:
        rowarray_list.append({'id':p[0], 'nome':p[1], 'telefone': p[2], 'idade': [3]})

    return jsonify({'pessoas': rowarray_list}) # json.dumps(rowarray_list)

#CREATE
@app.route('/addpessoa', methods=['POST'])
def pessoa_add():
    if request.method == 'POST':
        pessoa=Pessoa(None, request.json['nome'],request.json['telefone'], request.json['idade'])
        pessoa_add = pessoa.add(pessoa)

    if not pessoa_add:
        return jsonify({'result': "Adicionado com Sucesso"})
    return jsonify({'result': "Ihh, não adicionou!"})
 
#UPDATE
@app.route('/editpessoa', methods=['PUT'])
def pessoa_update():
    pessoa = Pessoa(request.json['id'],request.json['nome'],request.json['telefone'], request.json['idade'])
    if pessoa == None or pessoa == "":
        return jsonify({'result': 'nao existe na base de dados'})
   
    pessoa_update = pessoa.update(pessoa)
    #If post.update does not return an error
    if not pessoa_update:
        return jsonify({'result': "Atualizado com Sucesso"})
    return jsonify({'result': "Ihh, não salvou!"})

#DELETE
@app.route('/delpessoa' , methods=['DELETE'])
def pessoa_delete ():
    pessoa = pessoa=Pessoa(request.json['id'],request.json['nome'],request.json['telefone'], request.json['idade'])
    if pessoa == None or pessoa == "":
        return jsonify({'result': 'nao existe na base de dados'})
    
    pessoa_delete = pessoa.delete(pessoa.id)
    if not pessoa_delete:
        return jsonify({'result': "Detelado com Sucesso"})
    return  jsonify({'result': "Ihh, não excluiu!"})

if __name__ == '__main__':
    app.debug=True
    app.run()