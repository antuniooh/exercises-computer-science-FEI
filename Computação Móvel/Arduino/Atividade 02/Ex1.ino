void setup()
{
  pinMode(12, OUTPUT);
  pinMode(6, OUTPUT);
}

void loop()
{
  digitalWrite(12, HIGH);
  digitalWrite(6, LOW);
  delay(1000); // Wait for 1000 millisecond(s)
  digitalWrite(12, LOW);
  digitalWrite(6, HIGH);
  delay(1000); // Wait for 1000 millisecond(s)
}