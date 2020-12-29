int echo1 = 2;
int trigger1 = 3;

int echo2 = 11;
int trigger2 = 12;

int sound = 100;

int ledGreen = 9;
int ledRed = 10;

int distancia1 = 0;
int distancia2 = 0;

int time1 = 0;
int time2 = 0;

void setup()
{
  pinMode(trigger1, OUTPUT);
  pinMode(echo1, INPUT);
  
  pinMode(trigger2, OUTPUT);
  pinMode(echo2, INPUT);
  
  pinMode(ledGreen, OUTPUT);
  pinMode(ledRed, OUTPUT);

  //SOM
  pinMode(6, OUTPUT);
  
  Serial.begin(9600);
}

void sonar1()
{
  digitalWrite(trigger1, LOW);
  delayMicroseconds(2); 
  digitalWrite(trigger1, HIGH);
  delayMicroseconds(10); 
  digitalWrite(trigger1, LOW);
  
  time1 = pulseIn(echo1, HIGH);
  distancia1 = time1/100000*170;
  
  Serial.println(distancia1);
}  

void sonar2()
{
  digitalWrite(trigger2, LOW);
  delayMicroseconds(2); 
  digitalWrite(trigger2, HIGH);
  delayMicroseconds(10); 
  digitalWrite(trigger2, LOW);

  time2 = pulseIn(echo2, HIGH);
  distancia2 = time2/100000*170;
  
  Serial.println(distancia2);
} 


void loop()
{  
  sonar1();
  sonar2();
  
  if(distancia1 <= 1 || distancia2 <= 1){
    analogWrite(6,sound);
    digitalWrite(ledRed, HIGH);
    delay(5000);
  }else{
    digitalWrite(ledGreen, HIGH);
    digitalWrite(ledRed, LOW);
  }
  
}