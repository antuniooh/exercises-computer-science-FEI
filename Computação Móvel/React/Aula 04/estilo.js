import React from 'react';
import {StyleSheet} from 'react-native';

const estilos = StyleSheet.create({
  botao:{
    backgroundColor:"black",
    width:'25%',
    borderColor:'white',
    borderWidth:2,
    alignItems:"center"
  },
  texto:{
    color:'white',
    fontSize:50,
  },
  container:{
    display:'flex',
    flexDirection:'column',
    justifyContent:'center',
    height:'100%',
    backgroundColor:'black',
  },
  subcontainer:{
    flexDirection:'row',
  },
  display:{
    height:'60px',
    borderWidth:2,
    borderColor:'white',
    backgroundColor:'black',
    alignItems:'flex-end'
  }
})

export default estilos;