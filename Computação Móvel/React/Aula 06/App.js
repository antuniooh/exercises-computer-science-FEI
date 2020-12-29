import * as React from 'react';
import { Text, View, StyleSheet, Button, TextInput, AsyncStorage } from 'react-native';
import {NavigationContainer} from '@react-navigation/native';
import {createStackNavigator} from '@react-navigation/stack';
import { createDrawerNavigator } from '@react-navigation/drawer';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import { MaterialCommunityIcons } from '@expo/vector-icons';

import estilos from './estilo';

class Login extends React.Component{
  constructor(props){
    super(props);
    this.state={
      user: undefined,
      password:undefined,
    }
  }

  leitura(){
    AsyncStorage.getItem(this.state.user, (erro, senha) => {
      if(erro ==undefined && senha != null){
        if(senha == this.state.password)
          alert("Logado")
        else 
          alert("senha incorreta")
    }
    else{
      alert("Nao achou")
    }
    })
  }

  render(){
    return(
      <View style={estilos.container}>
        <Text>Login</Text>
        <Text>Login:</Text>
        <TextInput style={estilos.caixa}
        onChangeText={(texto) =>this.setState({user:texto}) }
        ></TextInput>
        <Text>Senha:</Text>
        <TextInput style={estilos.caixa}
        onChangeText={(texto) =>this.setState({password:texto}) }
        ></TextInput>
        <Button title="Login" onPress={() => this.leitura()}> </Button>
      </View>
    )
  }

  goDetails(){
    this.props.navigation.navigate("Cadastro");
  }
}

/*function Cadastro (){
    return(
      <View style={estilos.container}>
        <Text>"AAAAA"</Text>
      </View>
    );
}*/

class Cadastro extends React.Component{
  constructor(props){
    super(props);
    this.state={
      user: undefined,
      password:undefined,
    }
  }

  gravar(){
    AsyncStorage.setItem(this.state.user, this.state.password,
    (erro) => {
      if(erro == undefined)
        alert("Gravou");
    })
  }
  render(){
    return(
      <View style={estilos.container}>
        <Text>Cadastro</Text>
        <Text>Login:</Text>
        <TextInput style={estilos.caixa}
        onChangeText={(texto) =>this.setState({user:texto}) }
        ></TextInput>
        <Text>Senha:</Text>
        <TextInput style={estilos.caixa}
        onChangeText={(texto) =>this.setState({password:texto}) }
        ></TextInput>
        <Button title="cadastro" onPress={() => this.gravar()}> </Button>
      </View>
    )
  }

  goDetails(){
    this.props.navigation.navigate("Cadastro");
  }
}
const Stack = createBottomTabNavigator();

export default class App extends React.Component{
  render(){
    return(
      <NavigationContainer>
        <Stack.Navigator>
          <Stack.Screen name="Login" component={Login}
          options={{
            tabBarLabel:"Login",
            tabBarIcon: ({cor, size}) => (
              <MaterialCommunityIcons name = "home" color={cor} size={size}/>
            )
          }}
          />
          <Stack.Screen name="Cadastro" component={Cadastro}
           options={{
            tabBarLabel:"Cadastro",
            tabBarIcon: ({cor, size}) => (
              <MaterialCommunityIcons name = "account-details" color={cor} size={size}/>
            )
          }}
          />
        </Stack.Navigator>
      </NavigationContainer>
    );
  }
}
