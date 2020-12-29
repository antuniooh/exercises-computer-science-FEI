var http = require('http');
var express = require('express');
var app = express();
app.use(express.static('./public'));
app.use(express.static('./views'));
var bodyParser = require('body-parser');
var mongoose = require('mongoose');
app.set('view engine', 'ejs');
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

var cadastroUsuario = new mongoose.Schema({
    cadastroLogin: String,
    cadastroSenha: String,
    cadastroNome: String
});

var ModelUsuario = mongoose.model('usuarios', cadastroUsuario);

var cadastroLivro = new mongoose.Schema({
    cadastroLivro: String,
    cadastroAutor: String
});

var ModelLivro = mongoose.model('livros', cadastroLivro);

mongoose.connect('mongodb://localhost/banco', { useMongoClient: true });

app.get(['/', '/login'], function(requisicao, resp){
    resp.render('login'); //alterar de acordo com o nome da página
});

app.get(['/cadastra'], function (requisicao, resp) {
    resp.render('cadastra');
})

app.post('/cadastra',function (requisicao, resp) {

   var Username = requisicao.body.username;//nomes colocados na pagina de cadastro de usuario
   var Senha = requisicao.body.senha;
   var Nome = requisicao.body.nome;

   var novoUsuario = new ModelUsuario({
       cadastroLogin: Username,
       cadastroSenha: Senha,
       cadastroNome: Nome
   });

   novoUsuario.save(function(err){
       if (err){
           var msg = "Algo deu errado...";
           resp.render('cadastraMsg', {mensagem: msg});
       }else{
           var msg = "Produto cadastrado!";
           resp.render('cadastraMsg', {mensagem: msg});
       }
   });

});

app.post('/cadastraLivro',function (requisicao, resp) {

    var Livro = requisicao.body.livro;//nomes colocados na pagina de cadastro de livro
    var Autor = requisicao.body.autor;

    var novoLivro = new ModelLivro({
        cadastroLivro: Livro,
        cadastroAutor: Autor
    });

    novoLivro.save(function(err){
        if (err){
            resp.render('erroLivro') //criar página de erro de cadastro de livro
        }else{
            resp.render('okLivro') //criar página de ok de cadastro de livro
        }
    });

});

ModelUsuario.find({cadastroLogin: Username, cadastroSenha:loginSenha},
    function (err, obj) {
        if(err){
            console.log(err);
        }
        if(obj.length){
            resp.render('home')//nome página home
        }
        else{
            var msg = "Login incorreto";
            resp.render('loginMsg', {mensagem: msg})
        }

    }
)


var server = http.createServer(app);
server.listen(8080);
console.log("Servidor rodando...");
