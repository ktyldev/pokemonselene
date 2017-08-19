#filepaths
import pygame, sys, os

basePath = os.path.dirname(__file__)

music1 = 'Route ice music!.wav'

pallet_town = 'pallet town.png'
pokemon_centre_ground_floor = 'pokemon centre ground floor.png'
pokemon_centre_top_floor = 'pokemon centre top floor.png'

current_map = ''

start_menu = 'menu.png'

save_file = 'save_file.txt'

text_box_location = 'images/menu/text_box.png'

text_box = os.path.join(basePath, text_box_location)

def change_current_map(new_map):
	current_map = (new_map)