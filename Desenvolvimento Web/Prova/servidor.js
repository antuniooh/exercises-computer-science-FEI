//importação dos elementos necessários
var http = require("http");
var express = require("express");
var bodyParser = require("body-parser");

var app = express();

//criar o db
var mongoose = require("mongoose");
mongoose.connect("mongodb://localhost/exe1");

//cria o schema
var idosoSchema = new mongoose.Schema({
    dbnome:"string",
    dbendereco: "string",
    dbidade: "string"});
var idosoModel = mongoose.model("idosos", idosoSchema);

//visualizador ejs
app.set("view engine","ejs");

//bodyparser
app.use(bodyParser.urlencoded());
app.use(bodyParser.json());
app.use(express.static("./public"));

//criar metodos get
app.get(["/","/index"],function(req, resp) {
    resp.render("index")
});

app.get("/lista", function (req, resp) {
    idosoModel.find(function (err, objs) {
        resp.render("lista", {idosos:objs});
    });
});

//criar metodos post
app.post("/index", function (req, resp) {
    var nome = req.body.Nome;
    var endereco = req.body.Endereco;
    var idade = req.body.Idade;

    var novo = new idosoModel({
        dbnome: nome,
        dbendereco: endereco,
        dbidade: idade
    });
    novo.save();
    resp.render("cadastra", {mensagem: "usuário cadastrado", nome: nome, endereco: endereco, idade: idade});

    //novo.save(function (err) {
        //if (err) {
           // resp.render("cadastra", {mensagem: "usuário não cadastrado", nome: nome, endereco: endereco, idade: idade});
        //}
        //else {
        //    resp.render("cadastra", {mensagem: "usuário cadastrado", nome: nome, endereco: endereco, idade: idade});
        //}
    //});
});

//servidor
console.log("servidor rodando");
var servidor = http.createServer(app);
servidor.listen(8080);