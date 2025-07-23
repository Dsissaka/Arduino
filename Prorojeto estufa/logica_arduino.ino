#include <dht.h>

int DHT11 = A1;
int pinoRele = 2;
int Temp;                
int Umd;              
int contador = 0;
bool estado = true;
dht sensor;

void setup() {
  Serial.begin(9600);       
  pinMode(pinoRele, OUTPUT);  
  digitalWrite(pinoRele, HIGH);
}

void loop() {
  sensor.read11(DHT11);
  Temp = sensor.temperature;
  Umd = sensor.humidity;

  if (estado && contador < 28800) { // 8 horas * 60 min * 60 s = 28800 segundos
    contador++;
    delay(1000);
    if (contador >= 28800) {
      estado = false;
      digitalWrite(pinoRele, LOW);
      contador = 0;
    }
  } 
  else if (!estado && contador < 57600) { 
    contador++;
    delay(1000);
    if (contador >= 57600) {
      estado = true;
      digitalWrite(pinoRele, HIGH); 
      contador = 0;
    }
  }
  Serial.print ("Temperatura: ");
  Serial.print (Temp);
  Serial.print ("\260C. Umidade: ");     //  o código “\260” exibe o símbolo de grau: “ ° ”.
  Serial.print (Umd);
  Serial.println ("%");
}
