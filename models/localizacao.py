class Localizacao:
    def __init__(self, rua:str, num:str, bairro:str, cidade:str, estado:str, cep:str):
        self.rua = rua
        self.numero = num
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.cep = cep

    def formato_endereco(self) -> str:
        return f'Rua: {self.rua}, Numero: {self.numero}, Bairro: {self.bairro}, Cidade: {self.cidade}, Estado: {self.estado}, CEP: {self.cep}'