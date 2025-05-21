from typing import TYPE_CHECKING
from .usuario import Usuario

if TYPE_CHECKING:
    from .localizacao import Localizacao  
    from .transporte import Transporte  
    from .pedido import Pedido  


class Entregador(Usuario):
    def __init__(self, id_usuario: str, nome: str, email: str, senha: str, endereco: 'Localizacao', telefone: str, id_entregador: str, veiculo: 'Transporte', status_disponibilidade: str = 'Disponivel'):
        super().__init__(id_usuario, nome, email, senha, telefone, endereco)
        self.id_entregador = id_entregador
        self.veiculo = veiculo
        self.status_disponibilidade = status_disponibilidade
        self.entregas_concluidas = []

    def aceitar_pedido(self, pedido: 'Pedido') -> bool:
        if self.status_disponibilidade == 'Disponivel' and pedido.entregador is None:
            pedido.entregador = self
            pedido.status = 'Aguardando Coleta'
            self.status_disponibilidade = 'Em Entrega'
            return True
        return False
        
    def adicionar_historico(self, pedido: 'Pedido', mensagem: str):
        if pedido.entregador == self:
            pedido.adicionar_historico(mensagem)
            print(f'Historico adicionado ao pedido {pedido.id_pedido} pelo entregador {self.nome}.')
        else:
            print(f'Entregador {self.nome} não esta associado ao pedido {pedido.id_pedido}.')

    def atualizar_status_entrega(self, pedido: 'Pedido', novo_status: str, localizacao_atual: 'Localizacao' = None):
        if pedido.entregador == self:
            pedido.atualizar_status(novo_status)
            if localizacao_atual:
                pedido.adicionar_historico(f'Localizacao atual do entregador {self.nome}: {localizacao_atual.formatar_endereco()}')
                print(f'Pedido {pedido.id_pedido} atualizado para {novo_status} pelo entregador {self.nome}')
            if novo_status == 'Entregue':
                self.status_disponibilidade = 'Disponivel'
                if pedido not in self.entregas_concluidas:
                    self.entregas_concluidas.append(pedido)
                    print(f'Pedido {pedido.id_pedido} concluído pelo entregador {self.nome}.')
        else:
            print(f'Entregador {self.nome} não esta associado ao pedido {pedido.id_pedido}.')


    def ver_entregas_disponiveis(self):
        pass
