int buttonState = 0;

void setup()
{
  Serial.begin(9600);
  
  pinMode(6, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(4, OUTPUT);
  
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
  
  pinMode(7, INPUT);
}

void loop()
{
  int potentiometer = analogRead(1);
  buttonState = digitalRead(7);
  
  //1 - carro verde e pedestre vermelho
  digitalWrite(6,HIGH);
  digitalWrite(11,HIGH);
  
  if(buttonState == HIGH){
    Serial.print("liguei");

    //liga o amarelo e deixa no vermleho o pedestre
    digitalWrite(6,LOW);
    digitalWrite(5,HIGH);
    
    delay(2000);
    
    //liga o vermelho e deixa no verde o pedestre
    digitalWrite(11,LOW);
    digitalWrite(5,LOW);
    
    digitalWrite(4,HIGH);
    digitalWrite(10,HIGH);
    delay(potentiometer);
    
    //vermelho e dps fecha 
    digitalWrite(10,LOW);
    digitalWrite(11,HIGH);
    
    digitalWrite(11,LOW);
    delay(500);
    digitalWrite(11,HIGH);
    delay(500);
    digitalWrite(11,LOW);
    delay(500);
    digitalWrite(11,HIGH);
    delay(500);
    digitalWrite(11,LOW);
    
    //deixa em verde o dos carros
    //volta pro inicio
  }
}