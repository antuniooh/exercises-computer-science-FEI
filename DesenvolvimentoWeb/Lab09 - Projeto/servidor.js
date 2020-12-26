var http = require('http');
var express = require('express');
var bodyParser = require('body-parser');
var mongoose = require('mongoose');//pacote mongoose

var app = express();

//conexão com banco de dados
mongoose.connect("mongodb://localhost/usuarios"); //nome do db

//schemmas
var modelUsuarioSchema = new mongoose.Schema({
    nome: "String",
    login: "String",
    senha: "String"  });
var modelUsuario = mongoose.model('Usuarios', modelUsuarioSchema);

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


//cadatsro
app.get('/cadastro', function(requisicao, resp){
    resp.render('cadastro');});

app.post('/cadastro', function(requisicao, resp){
    var login = requisicao.body.login;
    var nome = requisicao.body.nome;
    var senha = requisicao.body.senha;

    var usuario = new modelUsuario({
        login: login,
        nome: nome,
        senha: senha
    });

    usuario.save(function (err, obj) {
        if(err) {
            console.log('erro');}
    });
    var msg = "Usuário cadastrado"
    resp.render("cadastro", {mensagem:msg});
});

//login
app.get('/login', function(requisicao, resp){
    resp.render('login');});

app.post('/login', function(requisicao, resp) {
    var login = requisicao.body.login;
    var senha = requisicao.body.senha;

    modelUsuario.find({modelUsuarioSchema: login, modelUsuarioSchema: senha},
        function (err, obj) {
            if (err) {
                console.log(err);
            }
            if (obj.length) {
                message = "Acertou!";
                resp.render('login', {message})
            }
            else {
                message = "Errou!";
                console.log("Acertou");
                resp.render('login', {message})
            }
        });
} );



app.get('/lista', function(requisicao, resp){
    modelUsuario.find(function (err, objs) {
        resp.render('lista', {usuarios: objs});
});



//cria o servidor e a porta
var server = http.createServer(app);
server.listen(8080);

console.log("Servidor rodando...");