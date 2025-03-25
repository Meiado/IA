# 8-Puzzle Solver

Este projeto implementa uma solução para o problema clássico do **8-Puzzle** utilizando diferentes algoritmos de busca: **Busca em Largura (BFS)**, **A\*** e **Best-First**. A interface gráfica foi criada utilizando **Tkinter**, permitindo ao usuário interagir com o sistema, escolher o tipo de busca, e visualizar a solução para o puzzle.

## **Pré-requisitos**

Antes de rodar o projeto, certifique-se de ter o seguinte instalado:

- **Python 3.x**: O código foi desenvolvido para Python 3. Você pode baixar o Python [aqui](https://www.python.org/downloads/).
- **Tkinter**: Caso não tenha o Tkinter instalado, use o comando abaixo para instalar (caso necessário):

    **Para Ubuntu/Debian**:

    ```bash
    sudo apt-get install python3-tk
    ```

    **Para outras plataformas**, o Tkinter geralmente já vem com a instalação do Python.

## **Instalação**

1. Navegue até a pasta do projeto:

    ```bash
    cd 8puzzle
    ```

2. (Opcional) Se preferir, crie um ambiente virtual para o projeto:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # Para Linux/Mac
    venv\Scripts\activate     # Para Windows
    ```

## **Executando o Projeto**

Para **rodar o projeto**, basta executar o arquivo `main.py`, que abrirá a interface gráfica:

```bash
python main.py
````