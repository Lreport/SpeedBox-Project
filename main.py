from controllers.usuariocontroller import UsuarioController
from controllers.pedidocontroller import PedidoController
from models.localizacao import Localizacao
from models.produto import Produto


usuario_controller = UsuarioController()
pedido_controller = PedidoController()

cliente1 = usuario_controller.criar_cliente('CLI01', 'Gabriel', 'gabriel@email.com', '123', '11999999999', Localizacao('Rua dos boiadeiros', '444', 'Morumbi', 'Nioaque', 'MS', '15385-000'))
cliente2 = usuario_controller.criar_cliente('CLI02', 'Pedro', 'pedro@email.com', '123','11999999999', Localizacao('Rua dos leitores', '777', 'Palmeiras', 'Vitoria', 'AC', '15385-001'))
cliente3 = usuario_controller.criar_cliente('CLI03', 'Ben10', 'salvadordagalaxia@email.com', 'senha123', '11999999999', Localizacao('Rua dos Heróis', '456', 'Centro', 'Metro City', 'AC', '15385-002'))


entregador1 = usuario_controller.criar_entregador('ENT_001', 'Juninho', 'juninho@email.com', 'senha123', '11999999999', Localizacao('Rua dos Entregadores', '1', 'Centro', 'Metro City', 'AC', '15385-003'), 'moto')
entregador2 = usuario_controller.criar_entregador('ENT_002', 'Marquinhos', 'marquinhos@email.com', 'senha123', '11999999999', Localizacao('Rua dos Entregadores', '2', 'Centro', 'Metro City', 'AC', '15385-004'), 'bicicleta')
entregador3 = usuario_controller.criar_entregador('ENT_003', 'Carlinhos', 'carlinhos@email.com', 'senha123', '11999999999', Localizacao('Rua dos Entregadores', '3', 'Centro', 'Metro City', 'AC', '15385-005'), 'carro')


produto1 = Produto('PROD_001', 'Pack chapéus', 'Vários chapéus', 100.00, 1.0, '30x20x10cm')
produto2 = Produto('PROD_002', 'Livro Receitas', 'Receitas da vovó', 49.90, 0.5, '20x15x2cm')
produto3 = Produto('PROD_003', 'Camiseta', 'Camiseta personalizada', 125.90, 0.8, '70x53x1cm')


pedido1 = pedido_controller.criar_pedido_novo('PED_001', cliente1, [produto1], Localizacao('Rua Dos lobos', '111', 'Caxias', 'Ilha Solteira', 'SP', '15385-000'), cliente1.endereco)
pedido2 = pedido_controller.criar_pedido_novo('PED_002', cliente2, [produto2], Localizacao('Rua das Rosas', '10', 'Jardim Aeroporto', 'Coxim', 'SP', '15385-001'), cliente2.endereco)
pedido3 = pedido_controller.criar_pedido_novo('PED_003', cliente3, [produto3], Localizacao('Rua das Capivaras', '20', 'Bassit', 'São José do Rio Preto', 'SP', '15385-002'), cliente3.endereco)


pedido_controller.atribuir_entrgador_ao_pedido('PED_001', entregador1)
pedido_controller.atribuir_entrgador_ao_pedido('PED_002', entregador2)
pedido_controller.atribuir_entrgador_ao_pedido('PED_003', entregador3)


print('--- 1) Usuários (Clientes e Entregadores) ---')
usuario_controller.lista_usuarios()

print('--- 2) Clientes ---')
usuario_controller.lista_cliente()

print('--- 3) Entregadores ---')
usuario_controller.lista_entregador()

print('--- 4) Pedidos ---')
for pedido in pedido_controller.pedidos:
    print(f'- Pedido ID: {pedido.id_pedido} para cliente {pedido.cliente.id_usuario}')

print('--- 5) Detalhes dos pedidos ---')
for pedido in pedido_controller.pedidos:
    pedido_controller.mostrar_detalhes_pedido(pedido.id_pedido)
