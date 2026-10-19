#💧 Controle de Níveis de Água

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Colorama](https://img.shields.io/badge/Biblioteca-Colorama-green)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen)
![Projeto](https://img.shields.io/badge/Projeto-Acadêmico-orange)

##📌 Sobre o projeto

Este projeto foi desenvolvido como uma atividade prática em Python.

O objetivo é criar um sistema simples para simular o monitoramento do nível de água de um reservatório.

O programa utiliza a biblioteca `colorama` para mostrar mensagens com diferentes cores no terminal, facilitando a identificação da situação do reservatório.

## 🚰 Níveis do reservatório

O sistema possui cinco níveis:

- 🔴 **Nível 1:** Muito baixo (crítico)
- 🟡 **Nível 2:** Baixo
- 🟢 **Nível 3:** Médio
- 🔵 **Nível 4:** Alto
- 🔵 **Nível 5:** Muito alto (alerta)

As cores apresentadas no terminal são definidas utilizando a biblioteca `colorama`.

## 🛠️ Tecnologias utilizadas

- Python
- Biblioteca Colorama
- Terminal

## 📚 Conceitos utilizados

Durante o desenvolvimento foram utilizados alguns conceitos básicos de Python:

- Listas;
- Funções;
- Estruturas condicionais `if`, `elif` e `else`;
- Estrutura de repetição `for`;
- Bibliotecas;
- F-strings.

## 💻 Código

```python
from colorama import Fore, Style, init

# Inicializa o Colorama
init()

# Lista com as situações do reservatório
situacoes = [
    "Muito baixo (crítico)",
    "Baixo",
    "Médio",
    "Alto",
    "Muito alto (alerta)"
]


# Função responsável por definir a cor
def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    else:
        return Fore.WHITE


# Simulação dos níveiscor = definir_cor(nivel)

    print(
        cor
        + f"Nível {nivel}: {situacoes[nivel - 1]}"
        + Style.RESET_ALL
    )