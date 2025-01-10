from shapely.geometry import Point, Polygon
from geopy.distance import distance

coords = [(46.082991, 38.987384), (46.075489, 38.987599), (46.079395, 
         38.997684), (46.073822, 39.007297), (46.081741, 39.008842)]

poly = Polygon(coords)
cab_26 = Point(46.073852, 38.991890)
pick_up = Point(46.080074, 38.991289)
entry_point = Point(46.075357, 39.000298)

if cab_26.within(poly):
    dist = distance((pick_up.x, pick_up.y), (cab_26.x, cab_26.y)).m
else:
    dist = distance((cab_26.x, cab_26.y), (entry_point.x, entry_point.y)).m + \
           distance((entry_point.x, entry_point.y), (pick_up.x, pick_up.y)).m

print(round(dist))
