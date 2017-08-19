#poke data! 
import sys, os, pygame
from move_data import *

screen_x = 480
screen_y = 320

screen = pygame.display.set_mode((screen_x, screen_y))

basePath = os.path.dirname(__file__)
def image_find(direction, pokemon):
	file_path = 'images/sprites/pokemon/%s/%s.png' %(direction, pokemon)
	return os.path.join(basePath, file_path)

#~~~~~~~~~~~~~~~~~~~~~~~~
typhlosion = {'name' : 'Typhlosion', 'type1' : 'fire', 'type2' : None,  'front' : image_find('front', 'typhlosion'), 'back' : image_find('back', 'typhlosion'), 'base_hp' : 78.0, 'hp_increase' : 2.0, 'attk_increase' : 1.0, 'sattk_increase' : 0.5, 'base_attk': 84.0, 'base_def' : 78.0, 'base_sattk' : 109.0, 'base_sdef' : 85.0, 'base_spd' : 100.0, 'move1level' : 1, 'move1' : tackle, 'move2level' : 12, 'move2' : strength, 'move3level' : 9, 'move3' : strength, 'move4level' : 1, 'move4' : tackle}
snorlax = {'name' : 'Snorlax', 'type1' : 'normal', 'type2' : None, 'front' : image_find('front', 'snorlax'), 'back' : image_find('back', 'snorlax'), 'base_hp' : 160.0, 'hp_increase' : 3.0, 'attk_increase' : 1.0, 'sattk_increase' : 0.5, 'base_attk': 110.0, 'base_def' : 65.0, 'base_sattk' : 65.0, 'base_sdef' : 110.0, 'base_spd' : 30.0,  'move1level' : 16, 'move1' : flamethrower , 'move2level' : 14, 'move2' : toxic, 'move3level' : 9, 'move3' : strength, 'move4level' : 1, 'move4' : tackle}
shuckle = {'name' : 'Shuckle', 'type1' : 'bug', 'type2' : 'rock', 'front' : image_find('front', 'shuckle'), 'back' : image_find('back', 'shuckle'), 'base_hp' : 20.0, 'hp_increase' : 2.0, 'base_attk': 10.0, 'attk_increase' : 1.0, 'sattk_increase' : 0.5, 'base_def' : 230.0, 'base_sattk' : 10.0, 'base_sdef' : 230.0, 'base_spd' : 5.0,  'move1level' : 16, 'move1' : flamethrower , 'move2level' : 14, 'move2' : toxic, 'move3level' : 9, 'move3' : strength, 'move4level' : 1, 'move4' : tackle}
mew = {'name' : 'Mew', 'type1' : 'psychic', 'type2' : None, 'front' : image_find('front', 'shuckle'), 'back' : image_find('back', 'shuckle'), 'base_hp' : 20.0, 'hp_increase' : 2.0, 'base_attk': 10.0, 'attk_increase' : 1.0, 'sattk_increase' : 0.5, 'base_def' : 230.0, 'base_sattk' : 10.0, 'base_sdef' : 230.0, 'base_spd' : 5.0,  'move1level' : 16, 'move1' : flamethrower , 'move2level' : 14, 'move2' : toxic, 'move3level' : 9, 'move3' : strength, 'move4level' : 1, 'move4' : tackle}



no_poke = {'name' : 'none'}

