var http = require('http');
var express = require('express');

var bodyParser = require('body-parser');

//vetor lista
var lista =[]

var app = express();

//mecanismo de visualização
app.set('view engine', 'ejs');

//body
app.use(bodyParser.urlencoded({extended: false}));
app.use(bodyParser.json());

//uso do conteudo estatico
app.use(express.static('./public'));

//requisicao das paginas
app.get('/index', function(requisicao, resp){
    resp.render('index');});

app.post('/lista', function(requisicao, resp){
    var usuario = {
        login: requisicao.body.login,
        nome: requisicao.body.nome,
        senha: requisicao.body.senha
    };
    lista.push(usuario); //adiciona um novo elemento ao vetro
    resp.render('lista', {lista});
});

// limpa o vetor
app.get('/limpa', function(requisicao, resp){
    lista = []; //zera o vetor
    resp.render('index'); //chama o cadastra
});

//cria o servidor e a porta
var server = http.createServer(app);
server.listen(8080);

console.log("Servidor rodando...");