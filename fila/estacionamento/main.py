from carro import Carro
from estacionamento import Estacionamento

fusca79 = Carro(modelo='Fusca 79', placa='AER-8909', tipo='hatch')
fiat147 = Carro(modelo='Fiat 147', placa='AWR-1234', tipo='hatch')
corcel = Carro(modelo='Corcel 2', placa='B6W-5690', tipo='hatch')
voyage = Carro(modelo='Voyage 95', placa='FGT-1231', tipo='sedan')
saveiro = Carro(modelo='Saveiro 2000', placa='BHG-1234', tipo='caminhonete')

vagas = Estacionamento()

print(f'Está vazio: {vagas.esta_vazio()}')

vagas.estacionar(fusca79)
vagas.estacionar(fiat147)
vagas.estacionar(corcel)
vagas.estacionar(voyage)
vagas.estacionar(saveiro)

print(f'Está vazio: {vagas.esta_vazio()}')

print(f'Qtde carros estacionamentos: {vagas.verificar_carros_estacionados()}')

vagas.carro_saida()

vagas.verificar_carro_frente()

vagas.mostrar_carros_estacionados()

vagas.calcular_valor()

vagas.carro_saida()

vagas.calcular_valor()



