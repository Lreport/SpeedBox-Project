from typing import TYPE_CHECKING
from models.usuario import Usuario
from models.cliente import Cliente
from models.entregador import Entregador
from models.transporte import TransporteCarro, TransporteMoto, TransporteBicicleta

if TYPE_CHECKING:
    from models.localizacao import Localizacao
    from models.transporte import Transporte

class UsuarioController:
    def __init__(self):
        self.usuarios: list[Usuario] = []

    def criar_cliente(self, id_usuario: str, nome: str, email: str, senha: str, telefone: str, endereco: "Localizacao") -> Cliente:
        if self.pesquisar_id_usuario(id_usuario):
            return None
        cliente_novo = Cliente(id_usuario, nome, email, senha, telefone, endereco)
        self.usuarios.append(cliente_novo)
        return cliente_novo

    def criar_entregador(self, id_usuario: str, nome: str, email: str, senha: str, telefone: str, endereco: "Localizacao", tipo_transporte: str) -> Entregador:
        if self.pesquisar_id_usuario(id_usuario):
            return None
        
        if tipo_transporte.lower() == 'carro':
            transporte = TransporteCarro(id_usuario, tipo_transporte, 40, 1)
        elif tipo_transporte.lower() == 'moto':
            transporte = TransporteMoto(id_usuario, tipo_transporte, 50, 0.5)
        elif tipo_transporte.lower() == 'bicicleta':
            transporte = TransporteBicicleta(id_usuario, tipo_transporte, 15, 0.2)
        else:
            raise ValueError('Tipo de transporte inválido. Escolha entre "carro", "moto" ou "bicicleta".')
            
        entregador_novo = Entregador(
            id_usuario=id_usuario,
            nome=nome,
            email=email,
            senha=senha,
            telefone=telefone,
            endereco=endereco,
            id_entregador=f'ENT_{id_usuario}', 
            veiculo=transporte,
            status_disponibilidade='Disponivel'
        )
        
        self.usuarios.append(entregador_novo)
        return entregador_novo
    
    def pesquisar_id_usuario(self, id_usuario:str) -> Usuario:
        for usuario in self.usuarios:
            if usuario.id_usuario == id_usuario:
                return usuario
        return None
    
    def pesquisar_id_entregador(self, id_entregador:str) -> Entregador:
        for usuario in self.usuarios:
            if isinstance(usuario, Entregador) and usuario.id_entregador == id_entregador:
                return usuario
        return None
    
    def lista_usuarios(self):
        print('--- Lista de Usuarios ---')
        for usuario in self.usuarios:
            if isinstance(usuario, Cliente):
                print(f'Cliente: {usuario.nome} (id: {usuario.id_usuario}, email: {usuario.email})')
            elif isinstance(usuario, Entregador):
                print(f'Entregador: {usuario.nome} (id: {usuario.id_usuario}, email: {usuario.email})')        
        print('')

    def lista_cliente(self):
        print('--- Lista de Clientes ---')
        for usuario in self.usuarios:
            if isinstance(usuario, Cliente):
                print(f'Cliente: {usuario.nome} (id: {usuario.id_usuario}, email: {usuario.email})')
        print('')

    def lista_entregador(self):
        print('--- Lista de Entregadores ---')
        for usuario in self.usuarios:
            if isinstance(usuario, Entregador):
                print(f'Entregador: {usuario.nome} (id: {usuario.id_usuario}, email: {usuario.email}, veiculo: {usuario.veiculo.tipo})')
        print('')            
