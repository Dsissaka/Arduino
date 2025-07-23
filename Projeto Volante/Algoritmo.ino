#include <Encoder.h>
#include <Joystick.h>
// a blblioteca joystick utilizada é a personalizada de MHeironimus

Encoder volante(2, 3); 
const int acelerador = A2; 
const int freio = A1;     
const int embreagem = A0; 

long volante_centro = 0; 

Joystick_ Joystick(JOYSTICK_DEFAULT_REPORT_ID, JOYSTICK_TYPE_JOYSTICK, 0, 0, true, true, false, true, true, false, false, false, false, false, false);
// true para o eixo X (volante), eixo Y(acelerador), eixo Rx (freio) e eixo Ry (embreagem);

void setup() {
  Serial.begin(9600);
  volante_centro = volante.read();
  // alinhar o volante com o centro antes de subir a programação para o  arduino
  Joystick.begin();
}

void loop() {
  long volante_p = volante.read() - volante_centro; 
  int acelerador_p = analogRead(acelerador);  
  int freio_p = analogRead(freio);         
  int embreagem_p = analogRead(embreagem);   


  Joystick.setXAxis(volante_p);
  Joystick.setYAxis(acelerador_p);
  Joystick.setRxAxis(freio_p);
  Joystick.setRyAxis(embreagem_p);


  Serial.print("V:"); Serial.print(volante_p);
  Serial.print(" A:"); Serial.print(acelerador_p);  
  Serial.print(" F:"); Serial.print(freio_p);     
  Serial.print(" E:"); Serial.println(embreagem_p); 
  delay(10); 
}
