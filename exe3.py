from shapely.geometry import Point, Polygon
from geopy.distance import distance

# Coordenadas do polígono
coords = [(46.082991, 38.987384), (46.075489, 38.987599), (46.079395, 
         38.997684), (46.073822, 39.007297), (46.081741, 39.008842)]
poly = Polygon(coords)

# Lista de pontos representando os táxis
cabs = [
    Point(46.073852, 38.991890),
    Point(46.078228, 39.003949),
    Point(46.080074, 38.991289)
]

# Ponto de partida do passageiro
pick_up = Point(46.080074, 38.991289)
# Ponto de entrada no polígono
entry_point = Point(46.075357, 39.000298)

# Variáveis para rastrear o táxi mais próximo e a menor distância
closest_cab = None
min_distance = float('inf')

# Processar cada táxi
for cab in cabs:
    if cab.within(poly):
        dist = distance((pick_up.x, pick_up.y), (cab.x, cab.y)).m
    else:
        dist = distance((cab.x, cab.y), (entry_point.x, entry_point.y)).m + \
               distance((entry_point.x, entry_point.y), (pick_up.x, pick_up.y)).m
    
    print(f"Distância do táxi {cabs.index(cab)} até o local de partida: {round(dist)} metros")

    # Verificar se este é o táxi mais próximo
    if dist < min_distance:
        min_distance = dist
        closest_cab = cab

# Exibir o táxi mais próximo
print(f"O táxi mais próximo está a {round(min_distance)} metros de distância.")

