import { StyleSheet } from 'react-native';

const estilos = StyleSheet.create({
  container:{
    display:'flex',
    flexDirection:'column',
    justifyContent:'center',
    height:'100%',
    backgroundColor: 'rgba(255,255,255,0.8)',
  },
  imagem:{
    resizeMethod:'auto',
    resizeMode:'cover',
    flex: 1,
  },
  texto:{
    alignSelf:'center',
    fontSize:20,
    fontWeight:'bold',
    color:'blue'
  }
})

export default estilos;