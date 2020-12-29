import React from 'react';
import { Text, View, ImageBackgroud } from 'react-native';
import estilos from './estilo.js'

class Hora extends React.Component{
  constructor(props){
    super(props)
    console.log("Constr")
  }
  componentWillUnmount(){
    console.log("componentWillUnmount chamado");
  }

  componentDidMount(){
    console.log("componentDidMount chamado");
  }

  shouldComponentUpdate(){
    console.log("shouldComponentUpdate chamado");
    return true;
  }

  componentDidUpdate(){
    console.log("componentDidUpdate chamado");
  }

  render(){
    return(
        <Text style={estilos.texto}>{this.props.children}</Text>
    )
  }
}

export default Hora;