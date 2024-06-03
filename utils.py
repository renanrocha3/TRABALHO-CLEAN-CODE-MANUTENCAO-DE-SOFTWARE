def ler_arquivo(nome_arquivo: str) -> str:
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.read()

    return conteudo


def escrever_arquivo(nome_arquivo: str, conteudo: str):
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        arquivo.write(conteudo)
