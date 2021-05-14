class automovel():

    def __init__(self,capacidade,quantidade,consumo):
        self.cap_dep = capacidade
        self.quant_comb = quantidade
        self.consumo = consumo

    def combustivel(self):
        return self.quant_comb

    def autonomia(self):
        return int((self.quant_comb / self.consumo) * 100)

    def abastece(self, n_litros):
        if (n_litros + self.quant_comb ) < self.cap_dep:
            self.quant_comb = n_litros + self.quant_comb
            return self.autonomia()
        else:
            print("Erro: Excedeu capacidade de combustivel")

    def percorre(self, n_km):
        if (self.autonomia() > n_km):
            self.quant_comb -= (n_km * self.consumo) / 100
            return self.autonomia()
        else:
            return -1



def main():
    a1 = automovel(60, 10, 15)
    print(a1.autonomia())
    print(a1.abastece(45))
    print(a1.percorre(150))
    print(a1.percorre(250))


if __name__ == "__main__":
    main()

