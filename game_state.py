#game_state
import pygame, sys, os, events, filepaths, tile_dictionaries, warps, menus, npcs

#admin variables
basePath = os.path.dirname(__file__)

save_file = os.path.join(basePath, filepaths.save_file)

#save variables
current_area = ''
player_orientation = ''
player_tile = 0

#not save variables

current_background = ''
current_foreground = ''
current_tile_map = ''
init_area = ''
current_event_list = {}
current_warp_list = {}
t_box = True
menu_open = False
in_battle = False
saving = False
cursor_pos = 0
battle_cursor_pos = 0
menu_max_pos = 8
battle_type = 0
trainer_current_poke = 0
slave = 0
text_speed = 10 #1x, text_speed = 5 is a 5* speed
player_character = 0 #0 = girl, 1 = boy
battle_menu_mode = 1 #1 = top menu, 2 = move menu
wild_level = 0
player_current_move = None
battle_immunity = False
on_tile_active = False
check_for_encounter = False
encounter_lock = True
spawn_x = None
spawn_y = None
player_sprite = None
current_npc_text = None

trainer_1 = False #true if pokemon trainer pokemon exists and has not fainted
trainer_2 = False
trainer_3 = False
trainer_4 = False
trainer_5 = False
trainer_6 = False

screen_size = (480, 320)
screen = pygame.display.set_mode(screen_size)

def update(): #there's certainly a better way to do this
	global current_area, current_background, current_foreground, current_tile_map, current_event_list, current_warp_list
	print 'gogo gadget update'
	print 'current area: '+str(current_area)
	if isinstance(current_area, list) == True:
		print 'list'
		new_area = current_area[0]
		print new_area		
	else:
		print 'not list'
		new_area = current_area
		print new_area
	if new_area == 'pallet_town':
		print 'update: pallet_town'
		filepaths.current_map = filepaths.pallet_town
		current_background = filepaths.pallet_town
		current_foreground = filepaths.pallet_town
		current_tile_map = tile_dictionaries.pallet_town
		current_event_list = events.pallet_town
		current_warp_list = warps.pallet_town
		npcs.current_area = npcs.pallet_town
	elif new_area == 'pokemon_centre_ground_floor':
		print 'update: pkm centre'
		filepaths.current_map = filepaths.pokemon_centre_ground_floor
		current_background = filepaths.pokemon_centre_ground_floor
		current_foreground = filepaths.pokemon_centre_ground_floor
		current_tile_map = tile_dictionaries.pokemon_centre_ground_floor
		current_event_list = events.pokemon_centre_ground_floor
		current_warp_list = warps.pokemon_centre_ground_floor
		npcs.current_area = npcs.pokemon_centre_ground_floor
	elif new_area == 'pokemon_centre_top_floor':
		print 'update: pkm centre top'
		filepaths.current_map = filepaths.pokemon_centre_top_floor
		current_background = filepaths.pokemon_centre_top_floor
		current_foreground = filepaths.pokemon_centre_top_floor
		current_tile_map = tile_dictionaries.pokemon_centre_top_floor
		current_event_list = events.pokemon_centre_top_floor
		current_warp_list = warps.pokemon_centre_top_floor
		npcs.current_area = npcs.pokemon_centre_top_floor
	print str(current_background)

		
def save():
	print 'current_area = ' + str(current_area)
	print 'init_area = '+init_area
	if current_area == init_area:
		area = str(current_area)
#		area = area[1:-1]
	else:
		area = str(current_area[0])
	print area
	save_variables = [area, player_orientation, player_tile]
	fo = open(save_file, 'w')
	fo.write(repr(save_variables))
#	cleanup_save_file()
	print save_variables
	
def load():
	#cleanup_save_file()
	global current_area, player_orientation, player_tile, init_area
	fo = open(save_file, 'r')
	f = fo.read()
#	print f
#	fo.close()
	f = f[1:-1]
	x = f.split(', ')
	current_area = x[0][1:-1]
	init_area = current_area
#	print init_area
	player_orientation = x[1]
	player_tile = x[2]

def cleanup_save_file():
	with open(save_file, 'r') as infile, open(save_file, 'w') as outfile:
		data = infile.read()
		data = data.replace('/','')
		data = data.replace('"','')
		outfile.write(data)
#		print data
	
def check_loaded_save():
	print current_area
	print player_orientation
	print player_tile
	
