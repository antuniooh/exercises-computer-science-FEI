function Cadastrar(){
    var aluno = {
        nome: document.getElementById("nome").value,
        lab: parseFloat(document.getElementById("lab").value),
        projeto: parseFloat(document.getElementById("projeto").value),
        prova: parseFloat(document.getElementById("prova").value),
        calculaNota: function () {
            nota = (this.lab + 2 * this.projeto + 3 * this.prova) / 6;
            return nota;
        },
        imprime: function () {
            var col1 = "<td>" + this.nome + "</td>";
            var col2 = "<td>" + this.projeto + "</td>";
            var col3 = "<td>" + this.prova + "</td>";
            var col4 = "<td>" + this.lab + "</td>";
            var col5 = "<td>" + this.calculaNota().toFixed(2) + "</td>"; // numero de casas decimais
            var linha = "<tr>" + col1 + col2 + col3 + col4 + col5 + "</tr>";
            var tabela = document.getElementById("Table");
            tabela.innerHTML += linha;
        }
    };

    aluno.imprime();

}


