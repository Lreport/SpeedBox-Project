from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .pedido import Pedido  
    from .localizacao import Localizacao 
class Usuario:
    def __init__(self, id_usuario: str, nome: str, email: str, senha: str, telefone: str, endereco: 'Localizacao'):
        self.id_usuario = id_usuario
        self.nome = nome
        self.email = email
        self.senha = senha
        self.telefone = telefone
        self.endereco = endereco
        self.historico_pedidos = []  

    def adc_historico_pedidos(self, pedido: 'Pedido'):
        self.historico_pedidos.append(pedido)
        print(f'Pedido {pedido.id_pedido} adicionado ao histórico de {self.nome}.')

    def historico_pedidos(self):
        if not self.historico_pedidos:
            return f'{self.nome} não possui pedidos realizados.'
        
        print(f'--- Pedidos realizados por {self.nome} ---')
        for pedido in self.historico_pedidos:
            print(f'- Pedido ID:{pedido.id_pedido}, Data: {pedido.data_pedido}, Status: {pedido.status}')