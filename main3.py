import os
import random


# arquivos = os.listdir()
# print(arquivos)

# nova_pasta = "Projetossss"
# os.makedir(nova_pasta, exist_ok=True)
# os.mkdir(nova_pasta)
# os.chdir(nova_pasta)
# print(f"Agora estamos em: {os.getcwd()}")

os.makedirs("Projetos", exist_ok=True)

for i in range(5): # irá criar 5 arquivos cuidar com a identação


    nome_arquivo = f"arquivo_{random.randint(1, 99)}.txt" # cria um nome com um numero aleatório

    # seleciona o caminho do arquivo
    caminho_arquivo = os.path.join("Projetos", nome_arquivo)

    try: # se der bom
        # escreve dentro do arquivo novo
            with open(caminho_arquivo, 'w') as f:
                f.write("Olá tudo bem")
                print("Sucesso")
    except: # se der erro
            print("Erro ao executar")

# caramba usar try e except é muito bom para achar erros