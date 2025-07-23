#include <MD5.h>
#include <MemoryFree.h>

const int acelerador = A2;
const int freio = A0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  int valor_acelerador = analogRead(acelerador);
  int valor_freio = analogRead(freio);

  char dados[16];
  snprintf(dados, sizeof(dados), "%d,%d", valor_acelerador, valor_freio); // escreve os dados num vetor char dados

  MD5 classehash;
  unsigned char* hash = classehash.make_hash(dados); // faz o hash
  char* hash_str = classehash.make_digest(hash, 16);  // retorna o hash em forma de string em hexadecimal
  char json_output[64];
  snprintf(json_output, sizeof(json_output), "{\"data\":\"%s\",\"hash\":\"%s\"}", dados, hash_str); //printas os dados e o hash

  Serial.println(json_output);
  free(hash);
  free(hash_str); // liberação dos dados visando economizar ram

  Serial.print("Memória livre (bytes): ");
  Serial.println(freeMemory()); //monitoração da quantidade de Ram livre do arduino (testes apenas)

  delay(1000);
}
