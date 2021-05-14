import json

def pede_nome():
    ficheiroExiste = False

    while not ficheiroExiste:
        nome = input("Introduza o nome do ficheiro de texto:")

        try:
            file = open(f"{nome}.txt")

            print(nome)
            ficheiroExiste = True

        except FileNotFoundError:
            print("ficheiro não existe, tente de novo")
            continue

def gera_nome(nomeFicheiro):
    f = open(f"{nomeFicheiro}.txt", "r")
    conteudo_dict = f.read()
    f.close()
    with open(f'{nomeFicheiro}.json', 'w') as json_file:
        json.dump(conteudo_dict, json_file, indent=4)


