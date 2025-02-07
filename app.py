import git
import os

repo_path = "/mnt/c/Users/155298/Desktop/Guia DevOps/Projetos/Script Python (Automação - Deinar)"
arquivo = "test.txt"  
trecho = "Trecho alvo"
linhas_adicionais = ["Nova linha teste A\n", "Nova linha teste B\n"]

def atualizar_repositorio(repo_path, branch):
    repo = git.Repo(repo_path)

    if branch not in repo.heads:
        raise ValueError(f"🚨 Branch '{branch}' não encontrada no repositório!")

    repo.git.checkout(branch)
    repo.git.pull()
    print(f"✅ Repositório atualizado na branch {branch}.")

def modificar_arquivo(arquivo, trecho, linhas_adicionais):
    with open(arquivo, "r", encoding="utf-8") as f:
        linhas = f.readlines()
    
    nova_lista = []
    for linha in linhas:
        nova_lista.append(linha)
        if trecho in linha:
            nova_lista.extend(linhas_adicionais)

    with open(arquivo, "w", encoding="utf-8") as f:
        f.writelines(nova_lista)
    
    print(f"✅ Arquivo {arquivo} modificado com sucesso.")

def commit_e_push(repo_path, arquivo, branch, mensagem_commit):
    repo = git.Repo(repo_path)
    repo.git.add(arquivo)
    repo.index.commit(mensagem_commit)
    repo.git.push("origin", branch)  
    print(f"🚀 Alterações enviadas para a branch {branch} no repositório remoto.")

def main():
    branch = input("Digite o nome da branch que deseja modificar (ex: develop, producao): ").strip()

    mensagem_commit = f"Alteração automática no arquivo {arquivo} na branch {branch}"
    
    atualizar_repositorio(repo_path, branch)
    
    arquivo_completo = os.path.join(repo_path, arquivo)
    modificar_arquivo(arquivo_completo, trecho, linhas_adicionais)
    
    commit_e_push(repo_path, arquivo, branch, mensagem_commit)

if __name__ == "__main__":
    main()