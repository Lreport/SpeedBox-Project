from usuario import Usuario
from pedido import Pedido


class Cliente(Usuario):
    def __init__(self, id_cliente:str, nome:str, email:str, senha:str, telefone:str, endereco:str):
        super().__init__(id_cliente, nome, email, senha, telefone, endereco)
        self._senha = senha
        self.endereco = endereco
        self.telefone = telefone

    def criar_pedido(self, pedido:Pedido):
        pass #criar isso a logica de criar/cancelar pedidido e adicionar no historico do cliente