# Multímetro Inteligente

Projeto de Microcontroladores com o objetivo de montar um Multímetro Inteligente utilizando um arduino e programação em python para os gráficos. O multímetro é capaz de medir tensão, corrente, resistência, diodo e capacitância, além de testar um servo motor. O display TFT mostra o menu e o valor medido em tempo real. Além disso, as medições são enviadas via serial para os gráficos no computador que plotam os dados de grandeza x tempo.

## Recursos

- Menu interativo navegado por encoder rotativo, com seleção via botão
- Medição de Tensão (V)
- Medição de Corrente (mA)
- Medição de Resistência (Ohm), com identificação automática da faixa de leitura e desenho do resistor com as cores correspondentes
- Teste de Diodo
- Medição de Capacitância (uF), por tempo de carga do capacitor
- Controle de Servo Motor, com indicador de ângulo na tela
- Interface gráfica em Python (Tkinter + Matplotlib)
- Início e finalização da leitura dos gráficos controlados pela própria interface do PC

## Tecnologias e componentes utilizados

### Arduino

- Display TFT (biblioteca Adafruit_GFX + MCUFRIEND_kbv)
- Encoder rotativo (RotaryEncoder)
- Botão (GFButton)
- Servo motor (Servo)
- Leituras analógicas para resistência, diodo e capacitância

### Interface

- Biblioteca Tkinter para a janela e os controles
- Biblioteca Matplotlib para os gráficos
- Biblioteca pyserial para comunicação serial com o Arduino

## Esquemático

<img width="3318" height="2237" alt="MODELO CIRCUITO FINAL_bb22" src="https://github.com/user-attachments/assets/2fad9d85-91fd-49e7-86f5-1115730a1e1d" />

## Vídeo de demonstração

Nosso video: https://youtu.be/gy5ccD67Qa0
