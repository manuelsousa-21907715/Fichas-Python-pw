import os
import csv
from matplotlib import pyplot as plt

def pede_pasta():
    path = input("Insira o path do ficheiro:")
    return path

def faz_calculos():
    path = pede_pasta()
    listaTipoFicheiro = []
    tamanhoPasta = {}
    ficheiros = os.listdir(path)

    for ficheiro in ficheiros:
        if len(ficheiro.split('.')) > 1:
            listaTipoFicheiro.append(f"{ficheiro.split('.')[1]}")

    for tipoFicheiro in set(listaTipoFicheiro):
        f_size = 0
        for ficheiro in ficheiros:
            if len(ficheiro.split('.')) > 1:
                if ficheiro.split('.')[1] == tipoFicheiro:
                    f_path = os.path.join(path, ficheiro)
                    f_size += (os.path.getsize(f_path) / 1024)
        n_tipo = sum([1 for tipo in listaTipoFicheiro if tipoFicheiro == tipo])
        tamanhoPasta[tipoFicheiro] = [f"Volume: {round(f_size,)}", f"Quantidade:{round(n_tipo,)}"]

    return tamanhoPasta





def guarda_resultados():
    with open('employee_file2.csv', mode='w') as csv_file:
        fieldnames = ['Tipo','Volume', 'Quantidade']
        dict = faz_calculos()
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for values in dict:
            value_list = dict[values]
            writer.writerow({"Tipo": values, "Volume":value_list[0], "Quantidade":value_list[1]})


def faz_grafico_queijos(titulo, resultados):
    lista_valores = []
    for resultado in resultados.values():
        lista_valores.append(resultado[0].split(':')[1])
    plt.pie(lista_valores, labels=resultados.keys(), autopct='%1.0f%%')
    plt.title(titulo)
    plt.show()


def faz_grafico_barras(titulo, resultados):
    lista_valores = []
    lista_chaves = []

    for item in sorted(resultados, key=resultados.get):
        lista_chaves.append(item)
        lista_valores.append(resultados.get(item)[0].split(':')[1])

    plt.bar(lista_chaves, lista_valores)
    plt.title(titulo)
    plt.show()

