void setup()
{
  for(int i = 1; i < 11;i++)
  	pinMode(i, OUTPUT);
}

void loop()
{
  int i = 10, j = 1;
  while(j < 10){
    for(i; i > 0; i--){
      digitalWrite(i, HIGH);
      delay(100); 
      if(i != 1)
      	digitalWrite(i, LOW);
  	}
    
    for(i; i <= 10 - j; i++){
	  digitalWrite(i, HIGH);
      delay(100); 
      digitalWrite(i, LOW);
 	 }
    j++;
  }

}