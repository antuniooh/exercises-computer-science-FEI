//inclui modulo http
var http = require('http');

//inclui modulo express
var express = require('express');

///Para Trabalhar com o caminho absoluto ao invés do caminho relativo:
const path = require('path');

//cria variavel app
var app = express();

//metodo use para saber onde esta o conteudo estatico
app.use(express.static('./public'));

//cria o servidor
var server = http.createServer(app);

//define o número de porta
server.listen(8080);

// mensagem
console.log("Servidor rodando");

//send file
app.get('/pagina1', function(requisicao, resp){
    resp.sendFile(path.join(__dirname+'/views/pagina1.html'));
});

app.get('/pagina2', function(requisicao, resp){
    resp.sendFile(path.join(__dirname+'/views/pagina2.html'));
});

app.get('/pagina3', function(requisicao, resp){
    resp.sendFile(path.join(__dirname+'/views/pagina3.html'));
});

app.get('/pagina4', function(requisicao, resp){
    resp.sendFile(path.join(__dirname+'/views/pagina4.html'));
});