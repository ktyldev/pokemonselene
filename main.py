	#catcode main
import pygame, sys, functions, object_classes, tile_engine, tile_dictionaries, os, filepaths, game_state, warps, battle, battle_tilez, random, menu
from tile_engine import *
from object_classes import character, player, Npc
from interaction import *
from game_state import screen

#INITIALISATION~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

pygame.init()
pygame.font.init()
pygame.mixer.init()

#LOAD GAME~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

screen_x = 480
screen_y = 320

#colours
black = ((0,0,0))
white = ((255,255,255))

#not colours
#screen = pygame.display.set_mode((screen_x, screen_y))

#basePath = os.path.dirname(__file__)

save_file = os.path.join(functions.basePath, filepaths.save_file)

clock = pygame.time.Clock()
fps = 30
total_frames = 0

tile_size = 16

width = 0
height = 0
bg_x = 0
bg_y = 0
camera_x = 0
camera_y = 0
spawn_x = 0
spawn_y = 0

text_box = pygame.image.load(filepaths.text_box)
	
def create_menu(file_name):
	file_path  = 'images/menu/%s' %file_name
	location = os.path.join(basePath, file_path)
	return location	
	
def play_music(file_name):
	file_path = 'music/%s' %file_name
	print file_path
	music1 = pygame.mixer.music.load(file_path)
	pygame.mixer.music.play()
	
def battle_run(tile):
	battle.commence('wild', battle_tilez.pallet_town[str(tile)], player_sprite.orient, tile)
#	battle.commence('trainer', joey, 'up', 13)

def encounter_probability(n):
	x = random.randint(1, 100)
	print 'X = ' + str(x)
	if x <= n:
		return True
		
def return_coords(tile):
	y = (tile / tile_engine.Tile.V) * tile_size
	x = tile * tile_size - (tile_engine.Tile.V * y) - tile_size
	return x, y
	
#LOAD TILEMAP~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def load_tiles(background):
	global spawn_x, spawn_y
	for y in range(0, background.get_height(), Tile.tile_size):
		for x in range(0, background.get_width(), Tile.tile_size):			
			if Tile.total_tiles in invalids:
				Tile(x, y, 'solid')
			elif Tile.total_tiles in battle_tiles:
				Tile(x, y, 'battle_tile')
			elif Tile.total_tiles == spawn_tile:
				Tile(x, y, 'spawn')
				spawn_x = x
				spawn_y = y
			elif Tile.total_tiles in event_tiles:
				Tile(x, y, 'event_tile')				
			elif Tile.total_tiles in warp_tiles:
				Tile(x, y, 'warp_tile')
			else:
				Tile(x, y, 'empty')
				
#NPC SHIT~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def player_npc_in_front():
	l = []
	l.append(player_sprite.get_number())
	for x in Npc.List:
		l.append(x.tile)
	for i in sorted(l):
		if i == player_sprite.get_number():
			player_sprite.draw(screen, player_sprite.camera_x, player_sprite.camera_y)
		else:
			for x in Npc.List:
				if i == x.tile:
					x.draw(screen, player_sprite.camera_x, player_sprite.camera_y)
		
def gen_npcs():
	object_classes.Npc.List = []
	for sprite in npcs.current_area.keys():
		#dict[sprite] =  npcs.current_area[sprite]['tile']
		tile = npcs.current_area[sprite]["tile"]
		coords = return_coords(tile)
		x = coords[0] + object_classes.character.width / 2		
		y = coords[1] + object_classes.character.width / 2
		coords = (x, y)
		text = npcs.current_area[sprite]["text"]
		movement = npcs.current_area[sprite]["movement"]
		if movement == True:
			range = npcs.current_area[sprite]["range"]
		else:
			range = None
		object_classes.Npc(tile, coords, text, movement, range)

#ACTUALLY RUN PROGRAM~~~~~~~~~~~~~~~~~~~~~~~~~~~

game_state.load()
game_state.update()

current_tile_map = game_state.current_tile_map

Tile.V = current_tile_map['V']
invalids = current_tile_map['invalids']
spawn_tile = current_tile_map['spawn_tile']
battle_tiles = current_tile_map['battle_tiles']
warp_tiles = current_tile_map['warp_tiles']
event_tiles = current_tile_map['event_tiles']

background = game_state.current_background
foreground = game_state.current_foreground
background = pygame.image.load(functions.create_background(background))
foreground = pygame.image.load(functions.create_foreground(foreground))
load_tiles(background)
 
game_state.check_loaded_save()
spawn_tile = game_state.player_tile
spawn_tile = int(spawn_tile)
spawn_y = (spawn_tile / tile_engine.Tile.V) * tile_size

game_state.spawn_y = spawn_y
spawn_x = spawn_tile * tile_size - (tile_engine.Tile.V * spawn_y) - tile_size

game_state.spawn_x = spawn_x

player_sprite = object_classes.player(spawn_x, spawn_y)

game_state.player_sprite = player_sprite
gen_npcs()

in_battle = False
#play_music(filepaths.music1)

while True:
	"""
	while game_state.menu_open == True: #start menu
		
		menu_image = pygame.image.load(create_menu(filepaths.start_menu))
		screen.blit(menu_image, (screen.get_width() - 120, screen.get_height() - 310))
		
		interaction(player_sprite)
		
		pygame.draw.rect(screen, black, (screen.get_width() - 115, screen.get_height() - (297  - game_state.cursor_pos * 30), 100, 31), 3)
		pygame.display.flip()
		if game_state.saving == True:
			print game_state.current_area
			game_state.save()
			game_state.saving = False
		#menu
	"""
	menu.fixed_by_function()
	if player_sprite.get_number() in warp_tiles: #WARP SPEED
		persistent_orientation = player_sprite.orient
		game_state.current_area = game_state.current_warp_list[str(player_sprite.get_number())] #finds dictionary entry for warp tile
		
		for i in range(0,13):
			
			clock.tick(fps)
			pygame.draw.rect(screen, black , (0, 0+ i*(screen_y/15), screen_x, (screen_y/15)), 0)
			# GET RECT
			pygame.display.flip()
		game_state.screen.fill((black))
		
		game_state.update() #updates files
		
		background = game_state.current_background
		foreground = game_state.current_foreground
		current_tile_map = game_state.current_tile_map				
		background = pygame.image.load(functions.create_background(background))
		foreground = pygame.image.load(functions.create_foreground(foreground))	
		
		Tile.List = []#re-initialising tiles
		Tile.total_tiles = 1
		Tile.V = current_tile_map['V']
		invalids = current_tile_map['invalids']
		spawn_tile = current_tile_map['spawn_tile']
		battle_tiles = current_tile_map['battle_tiles']
		warp_tiles = current_tile_map['warp_tiles']
		event_tiles = current_tile_map['event_tiles']		
		
		load_tiles(background)
		
		#re-initialising npc layer
#		npcs.current_area = {}
#		npcs.current_area_tiles = []
		gen_npcs()
		
		print 'NPC_LAYER = '+str(game_state.current_area)
		
		print 'CHECK AREA ' + str(game_state.current_area)
		warp_spawn = game_state.current_area[1]
		print warp_spawn
		spawn_y = (warp_spawn / tile_engine.Tile.V) * tile_size
		print spawn_y
		game_state.spawn_y = spawn_y
		spawn_x = warp_spawn * tile_size - (tile_engine.Tile.V * spawn_y) - tile_size
		print spawn_x
		game_state.spawn_x = spawn_x

		player_sprite = object_classes.player(spawn_x, spawn_y)
		print 'player_sprite'
		print player_sprite
		game_state.player_sprite = player_sprite
		if game_state.current_area[2] == False:
			player_sprite.orient = persistent_orientation
		else:
			if persistent_orientation == 'up':
				player_sprite.orient = 'down'
			elif persistent_orientation == 'down':
				player_sprite.orient = 'up'
			elif persistent_orientation == 'left':
				player_sprite.orient = 'right'
			elif persistent_orientation == 'right':
				player_sprite.orient = 'left'
	
	if player_sprite.get_number() in battle_tiles: #BATTLE SWAG
		if game_state.encounter_lock != True and encounter_probability(10) == True:
			print game_state.encounter_lock
			print 'battle!:D'
			n = player_sprite.get_number()
			print game_state.current_area
			#print battle_tilez.tile_data
			#print  battle_tilez.tile_data[current_tile_map]
			#print area_data[areas][area]
			a =  battle_tilez.tile_data[game_state.current_area][str(n)] 
			
			battle.commence('wild', a)
			
			#battle_run(player_sprite.get_number())
		game_state.encounter_lock = True
	
#ENTERING THE DRAW PHASE~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~		
	screen.fill((black))
	screen.blit(background, (player_sprite.camera_x, player_sprite.camera_y))
	interaction(player_sprite)
	player_npc_in_front()

	screen.blit(foreground, (player_sprite.camera_x, player_sprite.camera_y))
	Tile.draw_tiles(background)
	if game_state.current_npc_text != None:
		screen.blit(text_box, (0, 220))
		screen.blit(battle.poke_font_16.render(game_state.current_npc_text, 1, (0, 0 , 0)), (10, 230))
		pygame.display.flip()
		print game_state.current_npc_text
		
		wait_for_continue() #in interaction, fyi
		game_state.current_npc_text = None
	pygame.display.flip()
	player_sprite.movement()
	for x in object_classes.Npc.List:
		if x.can_move:
			if not x.walking:
				r = random.randint(0, 1000)
				if r < 5:
					dirs = ["n", "e", "s", "w"]
					dir = random.choice(dirs)
					if dir == "n":
						ntile = x.tile - Tile.V
					elif dir == "e":
						ntile = x.tile + Tile.H
					elif dir == "s":
						ntile = x.tile + Tile.V
					elif dir == "w":
						ntile = x.tile - Tile.H
					targ = Tile.get_tile(ntile)
					if targ.walkable:
						if not targ.warpable:
							l = []
							for n in Npc.List:
								l.append(n.tile)
							for i in l:
								if i == x.tile:
									l.remove(i)
							if targ.number not in l:
								if targ.number != player_sprite.get_number():
									x.set_target(targ)
		x.movement()
	clock.tick(fps)
	
#UPDATE VARIABLES~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	
	total_frames += 1
	game_state.player_tile = player_sprite.get_number()
	game_state.player_orientation = player_sprite.orient
#	game_state.check_for_encounter = False