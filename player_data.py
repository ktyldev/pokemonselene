import sys, os, game_state
from move_data import *
from pokemon_data import *

#oh shit

basePath = os.path.dirname(__file__)

if game_state.player_character == 0:
	battle_sprite = pygame.image.load(os.path.join(basePath, 'images/sprites/battle/girlback.png'))

#None if no move
# all move names are lowercase
# pp is how much pp used per move
poke2 = {'poke' : shuckle, 'level' : 30, 'nick' : 'kawaii', 'move1' : tackle, 'move2' : wrap, 'move3' : strength, 'move4' : toxic, 'hp' : 1, 'attk' : 0, 'def' : 0, 'sdef' : 1, 'sattk' : 0, 'spd' : 0, 'exp' : 0, 'dam' : 0, 'pp1' : 0, 'pp2' : 0, 'pp3' : 0, 'pp4' : 0, 'hp_lost' : 0} #stats are the amount increased artifically


poke1 = {'poke' : typhlosion, 'level' : 20, 'nick' : 'ty bro ty',  'move1' : tackle, 'move2' : flamethrower, 'move3' : strength, 'move4' : toxic, 'hp' : 1, 'attk' : 0, 'def' : 0, 'sdef' : 1, 'sattk' : 0, 'spd' : 0, 'exp' : 0, 'dam' : 0, 'pp1' : 0 , 'pp2' : 0, 'pp3' : 0, 'pp4' : 0, 'hp_lost' : 0} #pp = pp used

player_pokes = [poke1, poke2, None, None, None, None]

print poke1['pp1']

