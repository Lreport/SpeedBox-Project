class Transporte:
    def __init__(self, id_transporte:str, tipo:str, vel_media_kmh:float, preco_km:float):
        self.id_transporte = id_transporte
        self.tipo = tipo
        self.vel_media_kmh = vel_media_kmh
        self.preco_km = preco_km

    def calcular_preco(self, distancia_km:float) -> float:
        if distancia_km <= 0:
            raise ValueError("A distância não pode ser <= que 0.")
        else:
            self.preco = distancia_km * self.preco_km
            return self.preco
        
    def calcular_tempo(self, distancia_km:float) -> float:
        if distancia_km <= 0:
            raise ValueError("A distância não pode ser <= que 0.")
        else:
            self.tempo = distancia_km / self.vel_media_kmh
            return self.tempo
        
#depois fazer classes para cada tipo de transporte(carro, moto e bicicleta)