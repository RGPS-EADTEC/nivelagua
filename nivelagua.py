#nivelagua.py
#Controle de Niveis de Agua

from colorama import init, Fore

# Inicializa o colorama para garantir o reset automático das cores
init(autoreset=True)

def exibir_status_reservatorio(nivel):
    # Lista contendo os dados de cada nível do reservatório
    configuracoes = [
        {"nivel": 1, "situacao": "Muito baixo (crítico)", "cor": Fore.RED},
        {"nivel": 2, "situacao": "Baixo", "cor": Fore.YELLOW},
        {"nivel": 3, "situacao": "Médio", "cor": Fore.GREEN},
        {"nivel": 4, "situacao": "Alto", "cor": Fore.CYAN},
        {"nivel": 5, "situacao": "Muito alto (alerta)", "cor": Fore.BLUE}
    ]

    # Itera pela lista para encontrar o nível correspondente
    for config in configuracoes:
        if config["nivel"] == nivel:
            print(f"{config['cor']}Nível {config['nivel']}: {config['situacao']}")
            return

    print(f"{Fore.WHITE}Nível {nivel} inválido.")

# Exemplos de execução
if __name__ == "__main__":
    exibir_status_reservatorio(1)
    exibir_status_reservatorio(2)
    exibir_status_reservatorio(3)
    exibir_status_reservatorio(4)
    exibir_status_reservatorio(5)
    exibir_status_reservatorio(6)

#SAIDAS NA TELA:

#Nível 1: Muito baixo (crítico) EM VERMELHO
#Nível 2: Baixo EM AMARELO
#Nível 3: Médio EM VERDE
#Nível 4: Alto EM CIANO (AZUL CLARO)
#Nível 5: Muito alto (alerta) EM AZUL MARINHO
#Nível 6 inválido. EM BRANCO
