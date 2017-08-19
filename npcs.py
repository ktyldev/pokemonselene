#npcs.py
import pygame, sys, random, tile_dictionaries, game_state
from tile_engine import Tile

current_area_tiles = []

pallet_town = {'sprite 1':{'sprite':'', 'tile':200, 'text':'i\'m a test npc!:D', "movement": True, "range": [199, 200, 201,
																											223, 224, 225]},
				'sprite 2':{'sprite':'', 'tile':249, 'text':'well hi there', "movement": True, "range": [223, 224, 225,
																										248, 249, 250]}}
pokemon_centre_ground_floor = {'38':{'sprite':'', 'tile':38, 'text':'', "movement": False}}
pokemon_centre_top_floor = {}

current_area = pallet_town

def movement():
	pass

	