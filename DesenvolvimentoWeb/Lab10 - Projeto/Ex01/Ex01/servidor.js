var http = require("http");
var express = require("express");
var bodyParser = require("body-parser");
var mongoose = require("mongoose");
var app = express();

mongoose.connect("mongodb://localhost/Ex01");

var livroSchema = new mongoose.Schema({
    titulo: "String",
    autor: "String",});

var livroModel = mongoose.model("livros", livroSchema);


app.set("view engine", "ejs");
app.use(bodyParser.urlencoded());
app.use(bodyParser.json());

app.use(express.static('./public'));

app.get(["/", "/principal"], function(req, resp){
    resp.render("principal");
});

app.get("/cadastra", function(req, resp){
	resp.render("Cadastra");
});

app.post("/cadastra", function(req, resp){
    var Titulo = req.body.titulo1;
    var Autor = req.body.autor1;

    var novo = new livroModel({
        titulo: Titulo,
        autor: Autor,
    });

    novo.save();
    var msg = "Livro cadastrado!";
    resp.render("mensagem", {mensagem: msg});
});

app.get("/buscar", function(req, resp){

	livroModel.collection.distinct("autor", function(error, results){
		if(results.length == 0 )
			resp.render("mensagem", {mensagem: "Nenhum livro encontrado!"})
		else
			resp.render("Busca", {livros: results});
	});
});	

app.post("/buscar", function(req, resp){
    var autor_busca = req.body.autorB;
    livroModel.find({autor: autor_busca}, function(err, objs){
        console.log(objs.length)
        if(objs.length == 0){
            resp.render("mensagem", {mensagem: "Nenhum livro encontrado!"})
        }
        else
        {
            resp.render("listagem", {livros: objs});
        }
    });
});

app.get("/deleta", function(req, resp){

    livroModel.collection.distinct("autor", function(error, results){
        if(results.length == 0 )
            resp.render("mensagem", {mensagem: "Nenhum livro encontrado!"})
        else
            resp.render("Busca", {livros: results});
    });
});

app.post("/deletar", function(req, resp){
    var autor_busca = req.body.autorB;
    livroModel.remove({autor: autor_busca}, function(err, objs){
        if(objs.length == 0){
            resp.render("mensagem", {mensagem: "Nenhum livro encontrado!"})
        }
        else
        {
            resp.render("mensagem", {mensagem: "livro deletado!"});
        }
    });
});
var servidor = http.createServer(app);
servidor.listen(8080);
console.log("Servidor rodando...");

