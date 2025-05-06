import datetime
from typing import List
from localizacao import Localizacao
from pedido import Pedido

class Usuario: 
    def __init__(self, id_usuario:str, nome:str, email:str, senha:str, telefone:str, endereco:Localizacao, fone:str):
        self.id_usuario = id_usuario
        self.nome = nome
        self.email = email
        self._senha = senha
        self.endereco = endereco
        self.telefone = telefone

        self.historio = List[Pedido] = [] #tentar fazer um banco de ddados com isso

    def autenticacao(self, senha_enviada:str) -> bool:
        return self._senha == senha_enviada
    
    def ver_historico(self):
        if not self.historio:
            print("Historico vazio")
        else:
            for i in self.historio:
                print(i) #arrumar isso colocando dps coloando id, preco e status
                
