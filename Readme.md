## Machine Learning em Microcontroladores

Este projeto apresenta a implementação de um modelo de Machine Learning (ML) no microcontrolador Arduino Nano 33 BLE para contar pulos com base em dados do acelerômetro. Utilizando o TensorFlow Lite Micro, conseguimos realizar a inferência diretamente no microcontrolador, reduzindo a necessidade de conectividade e o consumo de energia em dispositivos operados por bateria.

## Introdução ao TensorFlow Lite Micro

TensorFlow Lite Micro (TinyML) é uma versão do TensorFlow adaptada para execução em microcontroladores com recursos limitados. Ele permite que modelos de ML sejam implementados sem sistemas operacionais, bibliotecas padrão em C/C++ ou alocação dinâmica de memória, ocupando apenas alguns quilobytes. Esta biblioteca foi utilizada para criar um modelo que detecta movimentos de pulos em tempo real.

### Pré-requisitos

1. **Arduino IDE**: Baixe e instale a Arduino IDE: [Arduino Software](https://www.arduino.cc/en/software).
2. **Gerenciamento de Placas e Bibliotecas**:
   - Instale o pacote "Arduino Mbed OS Nano Boards" no Gerenciador de Placas.
   - Adicione as bibliotecas "Arduino_LSM9DS1" e "ArduinoBLE" no Gerenciador de Bibliotecas.
3. **TensorFlow Lite Micro**: Clone o repositório do TensorFlow Lite Micro na pasta de bibliotecas:
   ```bash
   git clone https://github.com/tensorflow/tflite-micro-arduino-examples Arduino_TensorFlowLite
   ```

## Configuração do Projeto

### Captura de Dados

1. **Upload do Código de Leitura do Sensor**: Envie o código do Arduino para capturar dados do acelerômetro e giroscópio. Arquivo `coleta.ino` 
2. **Salvamento dos Dados em CSV**:
   - Prenda o Arduino na cintura ou tornozelo e execute o código em Python `logger.py`  para salvar os dados em arquivos `pulo.csv` (durante pulos) e `nao_pulo.csv` (em repouso).
   
### Treinamento do Modelo

1. **Carregue os Dados no Google Colab**: Use o notebook disponível [aqui](https://colab.research.google.com/github/arduino/ArduinoTensorFlowLiteTutorials/blob/master/GestureToEmoji/arduino_tinyml_workshop.ipynb) ou arquivo `ReconhecimentoPulo.ipynb` 
2. **Configuração do Modelo**:
   - Defina `GESTURES = ["pulo", "nao_pulo"]`.
   - Configure e treine a rede neural com 600 épocas para classificar entre "pulo" e "não pulo".
3. **Conversão para TensorFlow Lite**: Converta o modelo treinado para o formato TensorFlow Lite e gere uma matriz C que será incluída como `model.h`.

## Deploy na Placa

1. **Carregue o Código Principal**: Envie o código final que está dentro da pasta `classifier` para a placa, que usa o modelo para inferir os movimentos em tempo real, contando os pulos detectados.
2. **Model Header**: Adicione a matriz gerada pelo treinamento no arquivo `model.h`.

## Executando o Projeto

Após o upload, a placa começará a capturar e classificar os movimentos. Sempre que um pulo é detectado, o contador de pulos será incrementado e exibido no Serial Monitor.

## Referências

- [TensorFlow Lite Micro no GitHub](https://github.com/tensorflow/tflite-micro)
- [Arduino Nano 33 BLE](https://store.arduino.cc/products/arduino-nano-33-ble)

Este README cobre o básico para entender, configurar e executar o projeto de Machine Learning em microcontroladores com o TensorFlow Lite Micro.