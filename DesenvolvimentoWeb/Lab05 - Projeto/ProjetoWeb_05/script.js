var canvas = document.getElementById("Canvas");
var ctx = canvas.getContext("2d");

function desenharQuadrados(){
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    //desenha o quadrado vermeelho
    ctx.fillStyle = "red";
    ctx.fillRect(0, 0, 30, 30);

    //desenha o quadrado azul
    ctx.fillStyle = "blue";
    ctx.fillRect(270, 0, 30, 30);

    //desenha o quadrado amarelo
    ctx.fillStyle = "yellow";
    ctx.fillRect(0, 270, 30, 30);

    //desenha o quadrado verde
    ctx.fillStyle = "green";
    ctx.fillRect(270, 270, 30, 30);}

function desenharLinha(){

    //desenha a linha vermelha
    ctx.strokeStyle = "red";
    ctx.moveTo(0, 0);
    ctx.lineTo(300, 300);
    ctx.stroke();

    //desenha a linha azul
    ctx.beginPath();
    ctx.strokeStyle = "blue";
    ctx.moveTo(0, 300);
    ctx.lineTo(300, 0);
    ctx.stroke();

    //desenha a linha verde
    ctx.beginPath();
    ctx.strokeStyle = "green";
    ctx.moveTo(0, 150);
    ctx.lineTo(300, 150);
    ctx.stroke();

    //borda
    ctx.beginPath();
    ctx.strokeStyle = "black";
    ctx.moveTo(0, 0);
    ctx.lineTo(300, 0);
    ctx.stroke();

    ctx.moveTo(300, 0);
    ctx.lineTo(300, 300);
    ctx.stroke();

    ctx.moveTo(300, 300);
    ctx.lineTo(0, 300);
    ctx.stroke();

    ctx.moveTo(0, 300);
    ctx.lineTo(0, 0);
    ctx.stroke();


}

function desenharArcos(){
    //desenha criculo central
    ctx.beginPath();
    ctx.strokeStyle = 'green';
    ctx.arc(150, 150, 50, 0, 2 * Math.PI /2);
    ctx.stroke();

    //desenha criculo esquerda
    ctx.beginPath();
    ctx.strokeStyle = 'green';
    ctx.arc(40, 100, 15, 0, 2 * Math.PI);
    ctx.stroke();
    ctx.fillStyle = "yellow"
    ctx.fill()

    //desenha criculo direita
    ctx.beginPath();
    ctx.strokeStyle = 'green';
    ctx.arc(260, 100, 15, 0, 2 * Math.PI);
    ctx.stroke();
    ctx.fillStyle = "yellow"
    ctx.fill()


}
function escrever(){
    ctx.fillStyle = "black";
    ctx.font = "22px Arial";
    ctx.fillText("Desenvolvimento Web", 40, 45);

}

function main(){
    desenharQuadrados();
    desenharLinha();
    desenharArcos();
    escrever();
}
requestAnimationFrame(main);

