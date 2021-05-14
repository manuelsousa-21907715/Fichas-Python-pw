import analise_pasta

def main():
    analise_pasta.pede_pasta()
    calculo = analise_pasta.faz_calculos()
    analise_pasta.guarda_resultados()
    analise_pasta.faz_grafico_queijos("Volume", calculo)
    analise_pasta.faz_grafico_barras("Volume", calculo)


if __name__ == "__main__":
    main()