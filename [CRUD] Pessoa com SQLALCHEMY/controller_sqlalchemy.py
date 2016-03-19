from flask import render_template, request,flash, redirect, url_for, jsonify,abort, request, make_response, json
from model_sqlalchemy import Pessoa, app

#---------------------------------------------------
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

#---------------------------------------------------

#READ
@app.route('/pessoas', methods=['GET'])
def pessoa_index():
    pessoas = Pessoa.query.all()
    
    rowarray_list = []
    for p in pessoas:
        ps = ({'id':p.id, 'nome':p.nome, 'telefone': p.telefone, 'idade': p.idade})
        rowarray_list.append(ps)
    
    return jsonify({'pessoas': rowarray_list}) # json.dumps(rowarray_list)

#CREATE
@app.route('/addpessoa', methods=['POST'])
def pessoa_add():
    if request.method == 'POST':
        pessoa=Pessoa(request.json['nome'],request.json['telefone'], request.json['idade'])
        pessoa_add = pessoa.add(pessoa)

    if not pessoa_add:
        return jsonify({'result': "Adicionado com Sucesso"})
    return jsonify({'result': "Ihh, não adicionou!"})
 
#UPDATE
@app.route('/editpessoa', methods=['PUT'])
def pessoa_update():
    pessoa = Pessoa.query.get(request.json['id'])
    if pessoa == None or pessoa == "":
        return jsonify({'result': 'nao existe na base de dados'})
    
    pessoa.nome    =request.json['nome'],
    pessoa.telefone=request.json['telefone'],
    pessoa.idade   =request.json['idade']
                
    pessoa_update = pessoa.update()
    #If post.update does not return an error
    if not pessoa_update:
        return jsonify({'result': "Atualizado com Sucesso"})
    return jsonify({'result': "Ihh, não salvou!"})

#DELETE
@app.route('/delpessoa' , methods=['DELETE'])
def pessoa_delete ():
    pessoa = Pessoa.query.get(request.json['id'])
    #Check if the post exists:
    if pessoa == None:
        return jsonify({'result': 'nao existe na base de dados'})
    
    pessoa_delete=pessoa.delete(pessoa)
    if not pessoa_delete:
        return jsonify({'result': "Detelado com Sucesso"})
    return jsonify({'result': "Ihh, não exclui!"})

if __name__ == '__main__':
    app.debug=True
    app.run()