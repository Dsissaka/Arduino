**Objetivo:**

Criar um volante caseiro estilo joystick para jogos de corrida no PC, com leitura precisa de direção, pedal de aceleração e freio, utilizando componentes simples e acessíveis. O sistema simula um controle analógico USB.


| Componente                                      | Função                                                                             |
| ----------------------------------------------- | ---------------------------------------------------------------------------------- |
| Arduino Leonardo                                | Atua como interface USB HID para leitura dos eixos analógicos                      |
| 3 Potenciômetros lineares (10kΩ)                | Captam os movimentos de: volante (eixo X), acelerador (eixo Y) e freio (eixo Z)    |
| Encoder Magnético                               | Capta com alta precisão a rotação do volante (substitui um potenciômetro rotativo) |
| Resistores e jumpers                            | Conexões físicas e leitura estável                                                 |
