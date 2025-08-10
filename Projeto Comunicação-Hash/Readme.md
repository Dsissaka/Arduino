# 🔒📡 Comunicação Serial Segura Arduino → Python → Web

Este repositório contém um projeto completo que realiza a **transmissão segura de dados via comunicação serial entre um Arduino e um sistema Python**, utilizando verificação de integridade com **hashes**, armazenamento local em **JSON**, e exibição dos dados em um **site local**.

## 🧠 Visão Geral

O projeto consiste em três etapas principais:

1. **Arduino**: coleta e transmite dados via comunicação serial com um código hash para garantir integridade.
2. **Python**: recebe os dados pela porta serial, verifica o hash, armazena os dados íntegros em um arquivo `.json`.
3. **Servidor Web (localhost)**: lê os dados do JSON e os exibe em uma página web local.


## 🔧 Componentes Utilizados

### Hardware

| Componente           | Função                                         |
|----------------------|-----------------------------------------------|
| Arduino (ex: Leonardo)| Geração e transmissão de dados via Serial     |
| Potenciometros        | Captar informações                            |


### Software

| Tecnologia         | Função                                                                 |
|--------------------|------------------------------------------------------------------------|
| Arduino IDE        | Programação e envio do código para o Arduino                          |
| Python 3.x         | Leitura da porta serial, verificação de hash, escrita em JSON         |
| websocket (Node.js)| Exibição dos dados via site em `localhost` em tempo real              |
| JSON               | Armazenamento estruturado dos dados recebidos                         |
