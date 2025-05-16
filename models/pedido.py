import datetime
from produto import Produto
from localizacao import Localizacao
from transporte import Transporte
from cliente import Cliente
from entregador import Entregador

class Pedido:
    def __init__(self, id_pedido:str, cliente:Cliente, produtos:list, endereco_final:Localizacao, endereco_inicial:Localizacao):
        self.id_pedido = id_pedido
        self.cliente = cliente
        self.produtos = produtos
        self.endereco_inicial = endereco_inicial
        self.endereco_final = endereco_final
        self.entregador = None
        self.transporte = None
        self.status = 'Pendente'
        self.datetime_solicitacao = datetime.datetime.now()
        self.avaliacao = None

    def __str__(self):
        return(
            f'--- Detalhes do Pedido ---\n'
            f'ID do Pedido: {self.id_pedido}\n'
            f'Cliente: {self.cliente.nome}\n'
            f'Endereço inicial: {self.endereco_inicial.formatar_endereco()}\n'
            f'Endereço final: {self.endereco_final.formatar_endereco()}\n'
            f'Produtos:\n' + '\n'.join(str(produto) for produto in self.produtos) + '\n'
            f'Entregador: {self.entregador.nome if self.entregador else "Não atribuído"}\n'
            f'status: {self.status}\n'
            f'Data e hora da solicitação: {self.datetime_solicitacao.strftime("%d/%m/%Y %H:%M:%S")}\n'
        )

    def calcular_preco_total(self) -> float:
        return sum(produto.preco for produto in self.produtos)
    
    def calcular_custo_frete(self, transporte:Transporte, distancia_km:float) -> float:
        if not transporte:
            print("Transporte não definido.")
        
        return transporte.calcular_preco(distancia_km)
    
    def calcular_tempo_entrega(self, transporte:Transporte, distancia_km:float) -> float:
        if not transporte:
            print("Transporte não definido.")
        
        return transporte.calcular_tempo(distancia_km)
    
    def atualizar_status(self, status:str):
        self.status = status
        print(f"Status do pedido {self.id_pedido} atualizado para: {self.status}")

    def avaliar_entrega(self, nota:int, comentario:str):
        self.avaliacao = {
            'nota': nota,
            'comentario': comentario
        }
        print(f"Pedido {self.id_pedido} avaliado com nota {nota} e comentário: {comentario}")
