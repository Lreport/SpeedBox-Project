from typing import TYPE_CHECKING
from .usuario import Usuario

if TYPE_CHECKING:
    from .pedido import Pedido  
    from .localizacao import Localizacao  
    from .produto import Produto  

class Cliente(Usuario):
    def __init__(self, id_cliente: str, nome: str, email: str, senha: str, telefone: str, endereco: 'Localizacao'):
        super().__init__(id_cliente, nome, email, senha, telefone, endereco)

    def fazer_pedido(self, id_pedido: str, produtos: list['Produto'], endereco_final: 'Localizacao') -> 'Pedido':
        from .pedido import Pedido  
        endereco_inicial = self.endereco
        pedido = Pedido(id_pedido, self, produtos, endereco_final, endereco_inicial)
        return pedido

    def avaliar_entrega(self, pedido: 'Pedido', nota: int, comentario: str):
        if not hasattr(pedido, 'avaliacao'):
            pedido.avaliacao = {}
        pedido.avaliacao['nota'] = nota
        pedido.avaliacao['comentario'] = comentario
        print(f'Pedido {pedido.id_pedido}, nota {nota} e comentário: {comentario}')