class Transporte:
    def __init__(self, id_transporte:str, tipo:str, vel_media_kmh:float, preco_km:float):
        self.id_transporte = id_transporte
        self.tipo = tipo
        self.vel_media_kmh = vel_media_kmh
        self.preco_km = preco_km

    def __str__(self):
        return f'{self.tipo} - ID:{self.id_transporte}'

    def calcular_preco(self, distancia_km:float) -> float:
        if distancia_km <= 0:
            raise ValueError('A distância não pode ser <= que 0.')
        else:
            self.preco = distancia_km * self.preco_km
            return self.preco
        
    def calcular_tempo(self, distancia_km:float) -> float:
        if distancia_km <= 0:
            raise ValueError('A distância não pode ser <= que 0.')
        else:
            self.tempo = distancia_km / self.vel_media_kmh
            return self.tempo
        
class TransporteCarro(Transporte):
    def __init__(self, id_transporte:str, tipo:str, vel_media_kmh:float, preco_km:float):
        super().__init__(id_transporte, tipo, vel_media_kmh, preco_km)
        self.tipo = 'Carro'
        self.vel_media_kmh = 40
        self.preco_km = 1

class TransporteMoto(Transporte):
    def __init__(self, id_transporte:str, tipo:str, vel_media_kmh:float, preco_km:float):
        super().__init__(id_transporte, tipo, vel_media_kmh, preco_km)
        self.tipo = 'Moto'
        self.vel_media_kmh = 50
        self.preco_km = 0.5

class TransporteBicicleta(Transporte):
    def __init__(self, id_transporte:str, tipo:str, vel_media_kmh:float, preco_km:float):
        super().__init__(id_transporte, tipo, vel_media_kmh, preco_km)
        self.tipo = 'Bicicleta'
        self.vel_media_kmh = 15
        self.preco_km = 0.2
