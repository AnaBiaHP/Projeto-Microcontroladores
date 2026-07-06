# Multímetro Inteligente

Projeto de microcontroladores que transforma um Arduino em um multímetro com display gráfico, capaz de medir tensão, corrente, resistência, diodo e capacitância, além de testar um servo motor. O display TFT do próprio dispositivo mostra o menu e o valor medido em tempo real. Além disso, as medições são enviadas via serial para uma interface em Python no computador, que plota os dados em gráficos (grandeza x tempo) — os gráficos ficam apenas na interface do PC, não no display do Arduino.

## Recursos

- Menu interativo navegado por encoder rotativo, com seleção via botão físico
- Medição de Tensão (V)
- Medição de Corrente (mA)
- Medição de Resistência, com identificação automática da faixa de leitura e desenho do resistor com as cores correspondentes
- Teste de Diodo
- Medição de Capacitância, por tempo de carga do capacitor
- Controle de Servo Motor via encoder, com indicador de ângulo na tela
- Interface gráfica em Python (Tkinter + Matplotlib), rodando no computador, que recebe os dados via serial e plota gráficos em tempo real para cada tipo de medição (V x t, I x t, R x t, C x t, D x t)
- Início e finalização da leitura controlados pela própria interface do PC


## Tecnologias e componentes utilizados

### Arduino

- Display TFT (biblioteca Adafruit_GFX + MCUFRIEND_kbv)
- Encoder rotativo (RotaryEncoder)
- Botão físico (GFButton)
- Servo motor (Servo)
- Leituras analógicas para resistência, diodo e capacitância

### Interface / Python

- tkinter para a janela e os controles
- matplotlib para os gráficos
- pyserial para comunicação serial com o Arduino

## Esquemático

## Vídeo de demonstração
