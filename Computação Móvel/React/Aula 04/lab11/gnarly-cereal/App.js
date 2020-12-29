import  React from 'react';
import { Text, View, StyleSheet } from 'react-native';
import Botao from './components/Botao';
import estilos from './estilo';
import Display from './components/dISPLAY.JS';
import Soma from './Soma';
import Subtracao from './Subtracao';
import Multiplicao from './Multiplicacao';
import Divisao from './Divisao';

class App extends React.Component{
  constructor(props){
    super(props)
    this.state = {
        num1: undefined,
        num2: undefined,
        texto:"",
        resultado: undefined,
        operacao: null
    }
  }

  soma(){
    this.setState({num1:parseInt(this.state.texto)})
    this.clear()
    this.setState({operacao:new Soma()})
  }

  subtracao(){
    this.setState({num1:parseInt(this.state.texto)})
    this.clear()
    this.setState({operacao:new Subtracao()})
  }

  divisao(){
    this.setState({num1:parseInt(this.state.texto)})
    this.clear()
    this.setState({operacao:new Divisao()})
  }

  multiplicacao(){
    this.setState({num1:parseInt(this.state.texto)})
    this.clear()
    this.setState({operacao:new Multiplicao()})
  }

  resultado(){
    this.setState({num2:parseInt(this.state.texto)},
    () => 
    {
      this.setState({
        texto: this.state.operacao.calcula(this.state.num1, this.state.num2)});
    })
  }

  clear(){
    this.setState({texto: ""});
  }

  pressionar(num){
    this.setState({texto: this.state.texto + String(num)});
  }

  render(){
    return(
        <View style={estilos.container}>
        <Display>{this.state.texto}</Display>
          <View style={estilos.subcontainer}>
            <Botao onPress={() => this.pressionar(7)}>7</Botao>
            <Botao onPress={() => this.pressionar(8)}>8</Botao>
            <Botao onPress={() => this.pressionar(9)}>9</Botao>
            <Botao onPress={() => this.multiplicacao()}>*</Botao>
          </View>
          <View style={estilos.subcontainer}>
            <Botao onPress={() => this.pressionar(4)}>4</Botao>
            <Botao onPress={() => this.pressionar(5)}>5</Botao>
            <Botao onPress={() => this.pressionar(6)}>6</Botao>
            <Botao onPress={() => this.divisao()}>/</Botao>
          </View>
          <View style={estilos.subcontainer}>
            <Botao onPress={() => this.pressionar(1)}>1</Botao>
            <Botao onPress={() => this.pressionar(2)}>2</Botao>
            <Botao onPress={() => this.pressionar(3)}>3</Botao>
            <Botao onPress={() => this.subtracao()}>-</Botao>
          </View>
          <View style={estilos.subcontainer}>
            <Botao onPress={() => this.clear()}>C</Botao>
            <Botao onPress={() => this.pressionar(0)}>0</Botao>
            <Botao onPress={() => this.resultado()}>=</Botao>
            <Botao onPress={() => this.soma()}>+</Botao>
          </View>
        </View>
    );
  }
}

export default App;