import colorama
from colorama import Fore, Style

# Inicializa o colorama (necessário para Windows)
colorama.init()

def monitorar_reservatorio():
    # 1. Lista de situações conforme os níveis (do 1 ao 5)
    niveis_situacao = [
        "Muito baixo (crítico)", # Nível 1
        "Baixo",                 # Nível 2
        "Médio",                 # Nível 3
        "Alto",                  # Nível 4
        "Muito alto (alerta)"    # Nível 5
    ]

    # 2. Função para definir a cor e exibir a mensagem
    def exibir_alerta(nivel_index):
        situacao = niveis_situacao[nivel_index]
        numero_nivel = nivel_index + 1
        
        if numero_nivel == 1:
            cor = Fore.RED
        elif numero_nivel == 2:
            cor = Fore.YELLOW
        elif numero_nivel == 3:
            cor = Fore.GREEN
        elif numero_nivel == 4:
            cor = Fore.CYAN
        elif numero_nivel == 5:
            cor = Fore.BLUE
        else:
            cor = Fore.WHITE

        print(f"{cor}Nível {numero_nivel}: {situacao}{Style.RESET_ALL}")

    # 3. Simulação do Monitoramento
    print("--- SISTEMA DE MONITORAMENTO DE ÁGUA ---")
    for i in range(len(niveis_situacao)):
        exibir_alerta(i)
    print("----------------------------------------")

    # Garante que o estilo padrão seja restaurado
    print("Monitoramento concluído. Terminal restaurado.")

if __name__ == "__main__":
    monitorar_reservatorio()