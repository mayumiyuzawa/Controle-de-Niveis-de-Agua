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


# Simulação dos níveis do reservatório
for nivel in range(1, 6):
    cor = definir_cor(nivel)

    print(
        cor
        + f"Nível {nivel}: {situacoes[nivel - 1]}"
        + Style.RESET_ALL
    )