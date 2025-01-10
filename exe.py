from shapely.geometry import Point, Polygon

coord = [(46.082991, 38.987384), (46.075489, 38.987599), (46.079395,
         38.997684), (46.073822, 39.007297), (46.081741, 39.008842)]
poly = Polygon(coord)

cab_26 = Point(46.073852, 38.991890)
cab_112 = Point(46.078228, 39.003949)
pick_up = Point(46.080074, 38.991289)

print('cab_26 within the polygon:', cab_26.within(poly))
print('cab_112 within the polygon:', cab_112.within(poly))
print('pick_up within the polygon:', pick_up.within(poly))
