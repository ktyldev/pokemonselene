import sys, os
from pokemon_data import *

def image_find(sprite):
	file_path = 'images/sprites/npc/%s.png' %sprite

#general form is [0poke1, 1poke1lvl, 2poke2, 3poke2lv, 4poke3, 5poke3lv, 6poke4, 7poke4lv, 8poke5, 9poke5lv, 10poke6, 11poke6lv, 12win text, 13lose text, 14opening text, 15sprite name, 16name, 17background]
joey = [shuckle, 16, typhlosion, 20, snorlax, 11, no_poke, 0, no_poke, 0, no_poke, 0, 'You lose sucka', 'aww, shucks', 'Trainer Joey says : Come at me bro!', 'youngster', 'Joey', 'battle1.png']