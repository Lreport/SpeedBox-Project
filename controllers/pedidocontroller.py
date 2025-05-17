from models.pedido import Pedido
from models.produto import Produto
from models.cliente import Cliente
from models.entregador import Entregador
from models.transporte import Transporte
from models.localizacao import Localizacao

class PedidoController:
    def __init__(self):
        self.pedidos: list[Pedido] = []

    def criar_pedido_novo(self, id_pedido: str, cliente: Cliente, lista_produtos: list[Produto], endereco_final: Localizacao, endereco_inicial: Localizacao) -> Pedido:
        if self.pesquisar_id_pedido(id_pedido):
            print(f"Erro: Pedido com ID {id_pedido} já existe.")
            return None

        novo_pedido = Pedido(id_pedido, cliente, lista_produtos, endereco_final, endereco_inicial)
        self.pedidos.append(novo_pedido)
        print(f"Pedido {id_pedido} criado com sucesso!")
        return novo_pedido

    def pesquisar_id_pedido(self, id_pedido:str) -> Pedido:
        for pedido in self.pedido:
            if pedido.id_pedido == id_pedido:
                return pedido
            else:
                return None
            
    def atribuir_entrgador_ao_pedido(self, id_pedido:str, entregador:Entregador):
        pedido = self.pesquisar_id_pedido(id_pedido)
        if pedido:
            pedido.entregador = entregador
            print(f"Entregador {entregador.nome} atribuído ao pedido {id_pedido}.")
            return True
        else:
            print(f"Erro: Pedido com ID {id_pedido} não encontrado.")
            return False
        
    def atualiar_status_pedido(self, id_pedido:str, status:str):
        pedido = self.pesquisar_id_pedido(id_pedido)
        if pedido:
            pedido.status = status
            print(f"Status do pedido {id_pedido} atualizado para {status}.")
            return True
        else:
            print(f"Erro: Pedido com ID {id_pedido} não encontrado.")
            return False
        
    def calcular_preco_pedido(self, id_pedido: str) -> float:
        pedido = self.pesquisar_id_pedido(id_pedido)
        if pedido:
            distancia_km = pedido.endereco_final.calcular_distancia(pedido.endereco_inicial)
            preco_total = sum(produto.preco for produto in pedido.produtos)
            preco_transporte = pedido.entregador.veiculo.calcular_preco(distancia_km)
            return preco_total + preco_transporte
        else:
            print(f"Erro: Pedido com ID {id_pedido} não encontrado.")
            return None
        
    def calcular_tempo_pedido(self, id_pedido: str) -> float:
        pedido = self.pesquisar_id_pedido(id_pedido)
        if pedido:
            distancia_km = pedido.endereco_final.calcular_distancia(pedido.endereco_inicial)
            tempo_transporte = pedido.entregador.veiculo.calcular_tempo(distancia_km)
            return tempo_transporte
        else:
            print(f"Erro: Pedido com ID {id_pedido} não encontrado.")
            return None
        
    def lista_pedidos(self):
        print('--- Lista de Pedidos ---')
        for pedido in self.pedidos:
            print(f'ID: {pedido.id_pedido}, Cliente: {pedido.cliente.nome}, Status: {pedido.status}')
        print('')

    def formatar_detalhes_pedido(self, pedido: Pedido):
        print(f"\n--- Detalhe pedido id: {pedido.id_pedido} ---")
        print(f"Cliente: {pedido.cliente.nome} ({pedido.cliente.id_usuario})")
        entregador_nome = pedido.entregador.nome if pedido.entregador else "N/A"
        entregador_id = pedido.entregador.id_entregador if pedido.entregador else "N/A"
        print(f"Entregador: {entregador_nome} ({entregador_id})")
        print(f"Origem: {pedido.endereco_origem}")
        print(f"Destino: {pedido.endereco_destino}")
        print(f"Distancia: {pedido.distancia_km:.0f} km")
        
        print("Produtos:")
        for produto in pedido.lista_produtos:
            print(f"\t- {produto.nome} (ID: {produto.id_produto}, Valor: R${produto.valor_unitario:,.2f}, Peso: {produto.peso_kg:.1f}kg)")
        
        print(f"Taxa entrega: R${pedido.taxa_entrega:,.2f}")
        print(f"Valor total do pedido: R${pedido.valor_total:,.2f}")
        
        print(f'Data de Emissão: {pedido.data_hora_solicitacao.strftime("%Y-%m-%d %H:%M:%S")}')
        data_entrega_str = pedido.data_hora_real_entrega.strftime("%Y-%m-%d %H:%M:%S") if pedido.data_hora_real_entrega else "N/A"
        if hasattr(pedido, '_data_entrega_override_obj') and pedido._data_entrega_override_obj:
            data_entrega_str = pedido._data_entrega_override_obj.strftime("%Y-%m-%d %H:%M:%S")
        print(f"Data da Entrega: {data_entrega_str}")

    def mostrar_detalhes_pedido(self, id_pedido:str):
        pedido = self.pesquisar_id_pedido(id_pedido)
        if pedido:
            self.formatar_detalhes_pedido(pedido)
        else:
            print(f"Pedido com ID {id_pedido} não encontrado.")
