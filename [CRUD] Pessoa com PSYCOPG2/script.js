var url = "http://127.0.0.1:5000/";
var pessoasList = [];
var nomeoriginal = "";

function getPessoas() {
    var tabbody = "";
    $.getJSON(url + "pessoas", function (data) {
        pessoasList = data;
        
        for (var i = 0; i < data.pessoas.length; i++) {
            pess = JSON.stringify(data.pessoas[i]) ;
            tabbody += "<tr><td>"+ data.pessoas[i].id + "</td>" + 
                "<td>"+ data.pessoas[i].nome + "</td>" + 
                "<td>"+ data.pessoas[i].telefone + "</td>" + 
                "<td>"+ data.pessoas[i].idade + "</td>" + 
                "<td><button onclick='callEdit("+ pess +")' class='btn'>Editar</button> "+
            "<button onclick='removePessoa("+ pess + ")' class='btn btn-danger'>Excluir</button></td>"
        }
        $(tabbody).appendTo('#tab tbody');
    });
} 

//-------------------Add Pessoa ---------------------------
function addPessoa() {
    var self = this;
    self.nome = $("#inputNome");
    self.telefone = $("#inputTelefone");
    self.idade = $("#inputIdade");
    
    var pessoa = {nome: self.nome.val(),
                  telefone: self.telefone.val(),
                  idade: self.idade.val()
                  }
    
    autoAjax('addpessoa', pessoa, "POST");
    
    $('#modal').modal('hide');
}

//-------------------Edit Pessoa ---------------------------
function callEdit(pessoa) {
    $("#inputID").val(pessoa.id);
    $("#inputNome").val(pessoa.nome);
    $("#inputTelefone").val(pessoa.telefone);
    $("#inputIdade").val(pessoa.idade);
    //nomeoriginal = pessoa.nome;
    
    showModal('#edit');
}

function editarPessoa(){
    pessoa = {
        //nomeoriginal: nomeoriginal,
        id: $("#inputID").val(),
        nome: $("#inputNome").val(),
        telefone: $("#inputTelefone").val(),
        idade: $("#inputIdade").val()
    };
    
    autoAjax('editpessoa', pessoa, "PUT");
    
    $('#modal').modal('hide');
}

//------------------- Delete ---------------------------
function removePessoa(pessoa) {
    autoAjax('delpessoa', pessoa, "DELETE");
}

//------------------- Utils ---------------------------
function autoAjax(uri, data, method){
    $.ajax({
        url: url + uri,
        type: method,
        contentType: "application/json; charset=utf-8",
        dataType: 'json',
        data: JSON.stringify(data),
        success: function(data){
            alert(data.result);
            window.location.reload(true);
        },
        error: function(xhr, request, error) {
            console.log(xhr.responseText)
        }
    });
}

function showModal(idModal){
    if (idModal == '#add'){
        $('#modal #addDialogLabel').html('Nova Pessoa')
        $('#modal #btnSalvar' ).attr('onclick', 'addPessoa()');
    }
    else if(idModal == '#edit'){
        $('#modal #addDialogLabel').html('Editar Pessoa');
        $('#modal #btnSalvar' ).attr('onclick', 'editarPessoa()');
    }
    
    $("#modal").modal('show');
}

//------------------- Inicialização ---------------------------
getPessoas();
