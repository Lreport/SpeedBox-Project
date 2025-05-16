from localizacao import Localizacao
from pedido import Pedido
from typing import List

class Usuario: 
    def __init__(self, id_usuario:str, nome:str, email:str, senha:str, telefone:str, endereco:Localizacao):
        self.id_usuario = id_usuario
        self.nome = nome
        self.email = email
        self._senha = senha
        self._endereco = endereco
        self.telefone = telefone
        self.historico_pedidos:List[Pedido] = []

    def __str__(self) -> str:
        return f'Usuario: {self.nome} (ID:{self.id_usuario}, email:{self.email} )'

    def autenticacao(self, senha_enviada:str) -> bool:
        return self._senha == senha_enviada
                
    def adc_historico_pedidos(self, pedido:Pedido):
        self.historico_pedidos.append(pedido)

    def historico_pedidos(self):
        if not self.historico_pedidos:
            return f'{self.nome} não possui pedidos realizados.'
        
        print(f'--- Pedidos realizados por {self.nome} ---')
        for pedido in self.historico_pedidos:
            print(f'- Pedido ID:{pedido.id_pedido}, Data: {pedido.data_pedido}, Status: {pedido.status}')