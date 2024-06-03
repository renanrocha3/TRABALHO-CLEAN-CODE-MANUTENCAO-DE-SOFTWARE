def lerArquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    conteudo = arquivo.read()
    arquivo.close()
    return conteudo

# Função para escrever conteúdo em um arquivo
def escrever_arquivo(nome_arquivo,conteudo):
    arquivo = open(nome_arquivo, 'w')
    arquivo.write(conteudo)
    arquivo.close()


opcao = input("Escolha uma opção:\n1. Ler arquivo\n2. Escrever em arquivo\n")

if opcao == '1':
    nome_arquivo = input("Digite o nome do arquivo que deseja ler: ")
    texto = lerArquivo(nome_arquivo)
    print("Conteúdo do arquivo:")
    print(texto)

elif opcao == '2':
    nome_arquivo = input("Digite o nome do arquivo que deseja escrever: ")
    texto = input("Digite o texto que deseja escrever no arquivo: ")
    escrever_arquivo(nome_arquivo, texto)
    print("Texto escrito com sucesso no arquivo.")
else:
    print("Opção inválida.")