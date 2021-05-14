import json

def calcula_linhas(nomeFicheiro):

    file = open(f"{nomeFicheiro}.txt", "r")
    count = 0
    for linha in file:
        if linha != "\n":
            count += 1
    file.close()
    return count


def calcula_carateres(nomeFicheiro):

    file = open(f"{nomeFicheiro}.txt" , "r")
    count = 0
    for caracter in file:
        line = caracter.strip("\n")

    count += len(caracter)
    file.close()
    return count

def calcula_palavra(nomeFicheiro):

    file = open(f"{nomeFicheiro}.txt", "r")

    for caracter in file:
        maior = max(caracter.split(), key=len)

    return maior


def calcula_ocorrencia_de_letras(nomeFicheiro):
    file = open(f"{nomeFicheiro}.txt", "r")
    ocorrencias = {}

    texto = file.read()
    file.close()
    textoLower = ''.join(texto).lower()

    for letra in set(textoLower):
        if letra != " " and letra != "\n":
            ocorrencias[letra] = textoLower.count(letra)

    return ocorrencias

