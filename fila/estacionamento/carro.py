class Carro:
    def __init__(self, modelo, placa, tipo):
        self.modelo = modelo
        self.placa = placa
        self.tipo = tipo

    def exibir_detalhes(self):
        print(f'Carro: {self.modelo}, placa: {self.placa}, tipo: {self.tipo}')
