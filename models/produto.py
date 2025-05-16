class Produto:
    def __init__(self, id_produto:str, nome:str, descricao:str, preco:float, peso_kg:float, dimensao:str):
        self.id_produto = id_produto
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.pesoKg = peso_kg
        self.dimensao = dimensao

    def __str__(self):
        return f'ID: {self.id_produto}, Nome: {self.nome}, Descrição: {self.descricao}, Preço: {self.preco}, Peso: {self.pesoKg}kg, Dimensão: {self.dimensao}'