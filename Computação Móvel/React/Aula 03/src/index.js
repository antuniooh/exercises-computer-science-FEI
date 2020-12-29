import React from 'react';
import ReactDOM from 'react-dom';
import Botao from "./Botao";
import Soma from './Soma';
import Subtracao from './Subtracao'

import "./index.css"

class App extends React.Component{
  constructor(props){
    super(props);
    this.state={
      texto:"",
      numero1:undefined,
      numero2:undefined,
      operacao: undefined
    }
  }
  clear(){
    this.setState({texto:""});
  }

  pressionar(num){
    this.setState({texto:this.state.texto + String(num)})
  }

  soma(){
    this.setState({numero1:parseInt(this.state.texto)})
    this.clear();
    this.setState({operacao:new Soma()});
  }

  subtracao(){
    this.setState({numero1:parseInt(this.state.texto)})
    this.clear();
    this.setState({operacao:new Subtracao()});
  }

  resultado(){
    this.setState({numero2:parseInt(this.state.texto)}, () => 
    {
      this.setState({texto:
          this.state.operacao.calcula(this.state.numero1, 
            this.state.numero2)});
    });
}

  render(){
    return(
      <div>
        <h1>Calculadora</h1>
        <table>
          <tr>
            <td colSpan={"4"}>
              <input
                  style={{width:170, 
                  fontSize:"18pt"}}
                  type="text"
                  value={this.state.texto}
              />
            </td>
          </tr>
          <tr>
            <td><Botao clique={()=> this.pressionar(7)}>7</Botao></td>
            <td><Botao clique={()=> this.pressionar(8)}>8</Botao></td>
            <td><Botao clique={()=> this.pressionar(9)}>9</Botao></td>
            <td><Botao>/</Botao></td>
          </tr>
          <tr>
            <td><Botao clique={()=> this.pressionar(4)}>4</Botao></td>
            <td><Botao clique={()=> this.pressionar(5)}>5</Botao></td>
            <td><Botao clique={()=> this.pressionar(6)}>6</Botao></td>
            <td><Botao>X</Botao></td>
          </tr>
          <tr>
            <td><Botao clique={()=> this.pressionar(3)}>3</Botao></td>
            <td><Botao clique={()=> this.pressionar(2)}>2</Botao></td>
            <td><Botao clique={()=> this.pressionar(1)}>1</Botao></td>
            <td><Botao clique={()=> this.subtracao()}>-</Botao></td>
          </tr>
          <tr>
            <td><Botao clique={()=> this.clear()}>C</Botao></td>
            <td><Botao clique={()=> this.pressionar(0)}>0</Botao></td>
            <td><Botao clique={()=> this.resultado()}>=</Botao></td>
            <td><Botao clique={()=> this.soma()}>+</Botao></td>
             </tr>
        </table>
      </div>
    );
  }
}

ReactDOM.render(<App />, document.getElementById("root"));