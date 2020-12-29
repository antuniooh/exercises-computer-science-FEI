import React from 'react';
import { Text, View, StyleSheet, Image, ImageBackground } from 'react-native';
import estilos from './estilo.js'
import Hora from './hora.js'

class App extends React.Component{
  constructor(props){
    super(props);

    this.state ={
      data: new Date(),
      cont:0
    }
  }

  tick(){
    this.setState({
      data: new Date()
    })
    this.setState({
      cont: this.state.cont + 1
    })
  }

  componentDidMount(){
    this.timer = setInterval(() => this.tick(), 1000);
  }

  componentWillUnmount(){
    clearInterval(this.timer);
  }

  render(){
    var componente = null;
    if(this.state.cont < 10)
      componente =  <Hora style={estilos.texto}>
          {this.state.data.toLocaleTimeString()}</Hora>
    else
      componente = null

    return(
      <ImageBackground style={estilos.imagem} 
        source={require('./assets/relogio.png')}>
        <View style={estilos.container}>
         {componente}
          <Text style={estilos.texto}>
          {this.state.data.getDate()}/
          {this.state.data.getMonth() + 1}/
          {this.state.data.getFullYear()}
          </Text>
        </View>
      </ImageBackground>
    )
  }
}

export default App;