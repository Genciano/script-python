import git
import os

# Configurações para o TESTE
repo_path = "/mnt/c/Users/155298/Desktop/Guia DevOps/Projetos/Script Python (Automação - Deinar)"
arquivo = "test.txt"  # Arquivo de teste
trecho = "Trecho alvo"  # Trecho onde adicionaremos novas linhas
linhas_adicionais = ["Nova linha A\n", "Nova linha B\n"]  # Linhas que serão inseridas
mensagem_commit = "Testando modificação do arquivo"

def modificar_arquivo(arquivo, trecho, linhas_adicionais):
    arquivo_completo = os.path.join(repo_path, arquivo)  # Garante que o caminho completo seja usado
    with open(arquivo_completo, "r", encoding="utf-8") as f:
        linhas = f.readlines()
    
    nova_lista = []
    for linha in linhas:
        nova_lista.append(linha)
        if trecho in linha:
            nova_lista.extend(linhas_adicionais)  # Adiciona novas linhas após o trecho encontrado

    with open(arquivo_completo, "w", encoding="utf-8") as f:
        f.writelines(nova_lista)
    
    print(f"Arquivo {arquivo_completo} modificado com sucesso.")

def main():
    modificar_arquivo("test.txt", trecho, linhas_adicionais)

if __name__ == "__main__":
    main()