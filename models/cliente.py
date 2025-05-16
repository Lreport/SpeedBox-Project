from usuario import Usuario
from pedido import Pedido
from localizacao import Localizacao


class Cliente(Usuario):
    def __init__(self, id_cliente:str, nome:str, email:str, senha:str, telefone:str, endereco:str):
        super().__init__(id_cliente, nome, email, senha, telefone, endereco)
        self._senha = senha
        self.endereco = endereco
        self.telefone = telefone

    def __str__(self):
        return f'Cliente: {self.nome} (id: {self.id_usuario}, email: {self.email})'
    
    def fazer_pedido(self, id_pedido:str, produtos:list, endereco_final: Localizacao) -> Pedido:
        endereco_inicial = self.endereco
        pedido = Pedido(id_pedido, self, produtos, endereco_final, endereco_inicial)
        print(f"Pedido {id_pedido} criado com sucesso!")
        return pedido

    def avaliar_entrega(self, pedido: Pedido, nota: int, comentario: str):
        if not hasattr(Pedido, 'avaliacao'):
            pedido.avaliacao = {}
        pedido.avaliacao['nota'] = nota
        pedido.avaliacao['comentario'] = comentario
        print(f"Pedido {pedido.id_pedido}, nota {nota} e comentário: {comentario}")