import datetime
from produto import Produto
from localizacao import Localizacao
from transporte import Transporte
from cliente import Cliente
from entregador import Entregador

class Pedido:
    def __init__(self, id_pedido:str, cliente:Cliente, produtos:list):
        self.id_pedido = id_pedido
        self.cliente = cliente
        self.entregador = Entregador
        self.produto = Produto #fazer uma lista dos produtos ou entao fazer integração com o banco de dados
        self.endereco_inicial = Localizacao #arrumar localizacao e criar classe de endereco inicial
        self.endereco_final = Localizacao #arrumar localizacao e criar classe de endereco final
        self.transporte = Transporte
        self.status = 'Pendente' #arrumar isso depois
        self.datetime_solicitacao = datetime.datetime.now()
