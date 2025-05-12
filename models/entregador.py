from usuario import Usuario
from transporte import Transporte
from pedido import Pedido
from localizacao import Localizacao

class Entregador(Usuario):
    def __init__(self, id_usuario:str, nome:str, email:str, senha:str, endereco:Localizacao, telefone:str, id_entregador:str, veiculo:Transporte, status_disponibilidade:str = 'Disponivel'):
        super().__init__(id_usuario, nome, email, senha, telefone, endereco)
        self.id_entregador = id_entregador
        self.veiculo = veiculo
        self.status_disponibilidade = status_disponibilidade
        self.entregas_concluidas = list[Pedido] = [] #tentar fazer um banco da dados com isso

    def aceitar_encomenda(self, pedido:Pedido) -> bool:
        if self.status_disponibilidade == 'Disponivel' and pedido.entregador == None:
            pedido.entregador(self)
            pedido.atualizar_status('Aguardando Coleta')
            self.status_disponibilidade = 'Em Entrega'
            print(f"Entregador {self.nome} aceitou o pedido {pedido.id_pedido}.")

    def atualizar_status_entrega(self, pedido:Pedido, novo_status:str, localizacao_atual:Localizacao = None):
        if pedido.entregador == self:
            pedido.atualizar_status(novo_status)
            if localizacao_atual:
                pedido.adicionar_historico(f"Localização atual do entregador {self.nome}: {localizacao_atual}")
            print(f"Pedido {pedido.id_pedido} atualizado para: {novo_status} pelo entregador {self.nome}.")
            if novo_status == 'Entregue':
                self.status_disponibilidade = 'Disponivel'
                if pedido not in self.entregas_concluidas:
                    self.entregas_concluidas.append(pedido)
        else:
            print(f"Entregador {self.nome} não está atribuído ao pedido {pedido.id_pedido}.")


