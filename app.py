import git
import os 

def download_repo

    if not os.path.exists(local_path):
        git.Repo.clone_from(repo_url, local_path)
    else:
        print(f"Repositório já existe em {local_path}")

def alterar_arquivo(local_path, arquivo, trecho, linhas_adicionais):
    arquivo_path = os.path.join(local_path, arquivo)

    with open(arquivo_path, 'r') as f:
        conteudo = f.readlines()
        
    novo_conteudo = []
    for linha in conteudo:
        novo_conteudo.append(linha)
        if trecho in linha:
            
            novo_conteudo.extend(linhas_adicionais)
            
    with open(arquivo_path, 'w') as f:
        f.writelines(novo_conteudo)
        
def commit_alteracoes(local_path, mensagem_commit):
    repo = git.Repo(local_path)
    repo.Git.add(A=True)
    repo.index.commit(mensagem_commit)
    print(f"Commit realizado: {mensagem_commit}")
    
def main():
    repo_url = 'https://github.com/usuario/repo.git'
    local_path = '/caminho/para/repositorio'
    arquivo = 'caminho/do/arquivo/para/modificar.txt'
    trecho = 'texto a ser encontrado'
    linhas_adicionais = ['Nova linha 1\n', 'Nova linha 2\n']
    mensagem_commit = 'Adicionando novas linhas no arquivo'
    
    download_repo(repo_url, local_path)
    
    alterar_arquivo(local_path, arquivo, trecho, linhas_adicionais)
    
    commit_alteracoes(local_path, mensagem_commit)
    
if __name__'__main__':
    main()
