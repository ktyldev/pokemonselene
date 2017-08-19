import sys, os
from area_data import *

#416,417,418,419,440,441,442,443
pallet_town = {'416' : test_area, '417' : test_area, '418' : test_area, '419' : test_area, '440' : test_area, '441' : test_area, '442' : test_area, '443' : test_area}  

d = { }
d['pallet_town'] = [pallet_town]
print d['pallet_town']


tile_data = {'pallet_town' : pallet_town}