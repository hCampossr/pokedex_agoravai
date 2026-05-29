import os

def limpar_term():
    os.system('cls' if os.name == 'nt' else 'clear')

def voltar():
    input("Pressione ENTER para voltar ao menu principal")