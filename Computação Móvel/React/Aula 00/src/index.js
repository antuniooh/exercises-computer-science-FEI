import React from 'react';
import ReactDOM from 'react-dom';

const html=

  <section style={{display:"flex",flexDirection: "column"}}>
      <header style={{backgroundColor: "beige"}}>
        <h1>CC4670 - Computação Móvel</h1>
        <h2>React</h2>
        <h3>Biblioteca JavaScript para criar interfaces com o usuário</h3>
        <a>Primeira Aula</a>
      </header>

      <div style={{backgroundColor: "yellow"}}>
        <h1>Vamos utilizar:</h1>

        <ul>
          <li><h1>HTML</h1></li>
          <li><h1>CSS</h1></li>
          <li><h1>JavaScript</h1></li>
        </ul>
      </div>

  </section>;

ReactDOM.render(html, document.getElementById("root"));