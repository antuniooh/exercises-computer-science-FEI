#include <LiquidCrystal.h>

int potenciometro = 0;
double rpm = 0;
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

void setup() {
  pinMode(9, OUTPUT);
  pinMode(A0, INPUT);
  
  lcd.begin(16, 2);
}

void loop() {
  lcd.setCursor(0, 1);
  potenciometro = analogRead(A0);
  potenciometro = map(potenciometro,0,1023,0,255);
  analogWrite(9, potenciometro);
  rpm=map(potenciometro,0,255.0,0,8481.0);
  lcd.print(rpm);
}
 