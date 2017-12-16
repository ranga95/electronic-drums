
  
int sensor;         


void setup()
{
  Serial.begin(9600);      //Only for debugging
  pinMode(buzzer, OUTPUT);
}

void loop()
{
  sensor = digitalRead(A0);

    Serial.println(sensor);
  
  delay(200); //Small delay
}
