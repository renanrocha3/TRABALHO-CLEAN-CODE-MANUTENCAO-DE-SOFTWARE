from utils import ler_arquivo, escrever_arquivo


def exibir_menu():
    print("Escolha uma opção:")
    print("1. Ler arquivo")
    print("2. Escrever em arquivo")
    print("3. Sair")


def main():
    while True:
        exibir_menu()
        opcao = input("Digite a opção desejada: ")

        if opcao == '1':
            nome_arquivo = input("Digite o nome do arquivo que deseja ler: ")
            try:
                texto = ler_arquivo(nome_arquivo)
                print("Conteúdo do arquivo:")
                print(texto)
            except FileNotFoundError:
                print("Arquivo não encontrado.")

        elif opcao == '2':
            nome_arquivo = input("Digite o nome do arquivo que deseja escrever: ")
            texto = input("Digite o texto que deseja escrever no arquivo: ")
            escrever_arquivo(nome_arquivo, texto)
            print("Texto escrito com sucesso no arquivo.")

        elif opcao == '3':
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


if __name__ == "__main__":
    main()
