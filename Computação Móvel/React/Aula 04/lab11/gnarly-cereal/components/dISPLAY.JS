import React from 'react';
import {View, Text} from 'react-native';
import estilos from '../estilo';

class Display extends React.Component{
  render(){
    return(
      <View style={estilos.display}>
      <Text style={estilos.texto}>{this.props.children}</Text>
      </View>
    );
  }
}



export default Display;