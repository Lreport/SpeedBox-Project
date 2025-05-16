from usuario import Usuario
from pedido import Pedido


class Cliente(Usuario):
    def __init__(self, id_cliente:str, nome:str, email:str, senha:str, telefone:str, endereco:str):
        super().__init__(id_cliente, nome, email, senha, telefone, endereco)
        self._senha = senha
        self.endereco = endereco
        self.telefone = telefone

    def __str__(self):
        return f'Cliente: {self.nome} (id: {self.id_usuario}, email: {self.email})'
    
    def fazer_pedido(self, pedido: Pedido):
        pass

    def avaliar_entrega(self):
        