#object_classes

import pygame, sys, events, os, tile_dictionaries, filepaths, game_state, menus, battle, npcs
from events import current_map
from tile_engine import Tile

pygame.init()

current_map = filepaths.current_map 
current_tile_map = tile_dictionaries.pallet_town
events.current_map = filepaths.current_map
event_list = events.pallet_town

def wait_for_continue():
	waiting = True
	while waiting == True:
		for event in pygame.event.get():
		
			if event.type == pygame.QUIT:

				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN or event.key == pygame.K_z:
					waiting = False
					return False
					
				else :
					print 'yay'
					return None
			
		
def check_for_exit():
	for event in pygame.event.get():
	
		if event.type == pygame.QUIT:

			pygame.quit()
			sys.exit()
			
def battle_interaction(reason): 
	waiting = True
	print waiting
	while waiting == True:
		
		for event in pygame.event.get():
			
			if event.type == pygame.QUIT:

				pygame.quit()
				sys.exit()
			
			if reason == 'wait':
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_z:
						waiting = False
						return 'yay'
			else:	
				if event.type == pygame.KEYDOWN:
					print 'input!'
					print 'cursor :' + str(game_state.battle_cursor_pos)
					if game_state.battle_menu_mode == 1:
						if event.key == pygame.K_DOWN and game_state.battle_cursor_pos < 10:
							game_state.battle_cursor_pos += 10
							waiting = False
							return 'yay'
						if event.key == pygame.K_UP and game_state.battle_cursor_pos > 1:
							game_state.battle_cursor_pos -= 10
							waiting = False
							return 'yay'
						if event.key == pygame.K_RIGHT and game_state.battle_cursor_pos % 2 == 0:
							game_state.battle_cursor_pos += 1
							waiting = False
							return 'yay'
						if event.key == pygame.K_LEFT and game_state.battle_cursor_pos %2 != 0:
							game_state.battle_cursor_pos -= 1
							waiting = False
							return 'yay'
							
						if event.key == pygame.K_z:
							if game_state.battle_cursor_pos == 0:
								print 'fight'
								print 'in interaction'
								game_state.battle_menu_mode = 2
								game_state_battle_cursor_pos = 0
								waiting = False
								return 'yay'
							elif game_state.battle_cursor_pos == 	10:
								print 'pokemon'
								waiting = False
								return 'yay'
							elif game_state.battle_cursor_pos == 1:
								print 'bag'
								waiting = False
								return 'yay'
							else:
								print 'run'
								waiting = False
								return 'run'
								if game_state.battle_type == 'wild':
									print 'add run away code here' #as a function
									game_state.run_away = True
									game_state.battle_immunity = True
								elif game_state.battle_type == 'trainer':
									print 'You can\'t run from a trainer battle!'
								elif game_state.battle_type == 'special':
									print 'Are you sure you want to run?'
									#add check, call run function
					elif game_state.battle_menu_mode == 2:
						if event.key == pygame.K_DOWN:
							print 'down'
							if game_state.battle_cursor_pos < 10:
								if game_state.battle_cursor_pos == 0 and game_state.slave['move3'] != None:
									game_state.battle_cursor_pos += 10
								elif game_state.battle_cursor_pos == 1 and game_state.slave['move4'] != None:
									game_state.battle_cursor_pos += 10
								waiting = False
								return 'yay'	
						if event.key == pygame.K_UP: 
							print 'up'
							if game_state.battle_cursor_pos > 1:
								if game_state.battle_cursor_pos == 10 and game_state.slave['move1'] != None:
									game_state.battle_cursor_pos -= 10
								elif game_state.battle_cursor_pos == 11 and game_state.slave['move2'] != None:
									game_state.battle_cursor_pos -= 10
								waiting = False
								return 'yay'	
						if event.key == pygame.K_RIGHT:
							print 'right'
							if game_state.battle_cursor_pos % 2 == 0:
								if game_state.battle_cursor_pos == 0 and game_state.slave['move2'] != None:
									game_state.battle_cursor_pos += 1
								elif game_state.battle_cursor_pos == 10 and game_state.slave['move4'] != None:
									game_state.battle_cursor_pos += 1
								waiting = False
								return 'yay'	
						if event.key == pygame.K_LEFT:
							print 'left'
							if game_state.battle_cursor_pos %2 != 0:
								game_state.battle_cursor_pos -= 1
								waiting = False
								return 'yay'
						
						
						if event.key == pygame.K_x:
							game_state.battle_menu_mode = 1
							game_state.battle_cursor_pos = 0
							waiting = False
							return 'yay'
						
						
						if event.key == pygame.K_z:
							print 'move selected'
							if game_state.battle_cursor_pos == 0:
								#print game_state.slave['move1']
								game_state.player_current_move = game_state.slave['move1']
								
								
							if game_state.battle_cursor_pos == 1:
								#print game_state.slave['move2']
								game_state.player_current_move = game_state.slave['move2']
							if game_state.battle_cursor_pos == 10:
								#print game_state.slave['move3']
								game_state.player_current_move = game_state.slave['move3']
							if game_state.battle_cursor_pos == 11:
								#print game_state.slave['move4']
								game_state.player_current_move = game_state.slave['move4']
							battle.selected = True
							waiting = False
							return 'yay'
				
		#print game_state.battle_cursor_pos	

def interaction(sprite):

	event_list = game_state.current_event_list
	
	initial_orientation = sprite.orient

	for event in pygame.event.get():
	
		if event.type == pygame.QUIT:

			pygame.quit()
			sys.exit()
	
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_UP:
				sprite.hold_time = 0
				sprite.ani_pos = 0
				sprite.walking = False
			if event.key == pygame.K_DOWN:
				sprite.hold_time = 0
				sprite.ani_pos = 0
				sprite.walking = False
			if event.key == pygame.K_LEFT:
				sprite.hold_time = 0
				sprite.ani_pos = 0
				sprite.walking = False
			if event.key == pygame.K_RIGHT:
				sprite.hold_time = 0
				sprite.ani_pos = 0
				sprite.walking = False
		
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_z:
				if sprite.orient == 'up':
					future_tile_number = sprite.get_number() - Tile.V
				elif sprite.orient == 'down':
					future_tile_number = sprite.get_number() + Tile.V
				elif sprite.orient == 'left':
					future_tile_number = sprite.get_number() - Tile.H
				elif sprite.orient == 'right':
					future_tile_number = sprite.get_number() + Tile.H
				future_tile = Tile.get_tile(future_tile_number)
				if future_tile.eventable == True:
					print event_list
					print event_list[str(future_tile_number)]
				if future_tile_number in npcs.current_area_tiles:
					if sprite.orient == 'up':
						print 'face npc down'
					elif sprite.orient == 'down':
						print 'face npc up'
					elif sprite.orient == 'left':
						print 'face npc right'
					elif sprite.orient == 'right':
						print 'face npc left'
					for thing in npcs.current_area:
						if npcs.current__area[thing]['tile'] == future_tile_number:
							print npcs.current__area[thing]['text']
					

#					print npcs.current_area[str(future_tile_number)]['text']
			if game_state.menu_open == True:
				if event.key == pygame.K_DOWN:
					game_state.cursor_pos += 1
				elif event.key == pygame.K_UP:
					game_state.cursor_pos -= 1
				if game_state.cursor_pos < 0:
					game_state.cursor_pos = 0
				elif game_state.cursor_pos > game_state.menu_max_pos:
					game_state.cursor_pos = game_state.menu_max_pos
				elif event.key == pygame.K_z:
					print game_state.cursor_pos
					print menus.start_menu[str(game_state.cursor_pos)]
					if menus.start_menu[str(game_state.cursor_pos)] == 'save':
						game_state.saving = True
				print game_state.cursor_pos
				
			if event.key == pygame.K_LSHIFT:
				if game_state.menu_open == False:
					game_state.menu_open = True
				else:
					game_state.menu_open = False
				print game_state.menu_open
				

			
	keys = pygame.key.get_pressed()
	
	if game_state.menu_open == False:
		if not (keys[pygame.K_DOWN] or keys[pygame.K_LEFT] or keys[pygame.K_RIGHT] or keys[pygame.K_UP]):
			sprite.hold_time = 0
			sprite.walking = False
			sprite.ani_pos = 0

		if keys[pygame.K_UP]:# and not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_DOWN]:
			if game_state.in_battle != False:
				game_state.in_battle = False		
			if sprite.hold_time == 0:
				if sprite.walking == False:
					if sprite.orient != 'up':
						sprite.orient = 'up'
			sprite.hold_time += 1
			if initial_orientation == 'up':
				if sprite.hold_time > 4 or sprite.orient == 'up':
					sprite.walking = True
					sprite.hold_time = 0
					future_tile_number = sprite.get_number() - Tile.V
					if future_tile_number in range(1, Tile.total_tiles + 1):
						future_tile = Tile.get_tile(future_tile_number)
						if future_tile.walkable == True and future_tile_number not in npcs.current_area_tiles:
							sprite.set_target(future_tile)
						elif future_tile.walkable == False or future_tile_number in npcs.current_area_tiles:
							sprite.ani_pos = 0
							print 'no'
						else:
							sprite.hold_time = 0
							sprite.walking = False
							sprite.ani_pos = 0
		
		if keys[pygame.K_DOWN]:# and not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_UP]:	
	#		if not keys[pygame.K_UP]:
				if game_state.in_battle != False:
					game_state.in_battle = False
				if sprite.hold_time == 0:
					if sprite.walking == False:
						if sprite.orient != 'down':
							sprite.orient = 'down'
				sprite.hold_time += 1
				if initial_orientation == 'down':
					if sprite.hold_time > 4 or sprite.orient == 'down':
						sprite.walking = True
						sprite.hold_time = 0
						future_tile_number = sprite.get_number() + Tile.V
						if future_tile_number in range(1, Tile.total_tiles + 1):
							future_tile = Tile.get_tile(future_tile_number)
							if future_tile.walkable and future_tile_number not in npcs.current_area_tiles:
								sprite.set_target(future_tile)
							elif future_tile.walkable == False or future_tile_number in npcs.current_area_tiles:
								sprite.ani_pos = 0
								print 'no'
							else:
								sprite.hold_time = 0
								sprite.walking = False
								sprite.ani_pos = 0
		
		if keys[pygame.K_LEFT]:# and not keys[pygame.K_DOWN] and not keys[pygame.K_RIGHT] and not keys[pygame.K_UP]:
	#		if not (keys[pygame.K_UP] or keys[pygame.K_DOWN]):
				if game_state.in_battle != False:
					game_state.in_battle = False
				if sprite.hold_time == 0:
					if sprite.walking == False:
						if sprite.orient != 'left':
							sprite.orient = 'left'
				sprite.hold_time += 1
				if initial_orientation == 'left':
					if sprite.hold_time > 4 or sprite.orient == 'left':
						sprite.walking = True
						sprite.hold_time = 0
						future_tile_number = sprite.get_number() - Tile.H
						if future_tile_number in range(1, Tile.total_tiles + 1):
							future_tile = Tile.get_tile(future_tile_number)
							if future_tile.walkable and future_tile_number not in npcs.current_area_tiles:
								sprite.set_target(future_tile)
							elif future_tile.walkable == False or future_tile_number in npcs.current_area_tiles:
								sprite.ani_pos = 0
								print 'no'
							else:
								sprite.hold_time = 0
								sprite.walking = False
								sprite.ani_pos = 0

		if keys[pygame.K_RIGHT]:# and not keys[pygame.K_DOWN] and not keys[pygame.K_LEFT] and not keys[pygame.K_UP]:
			#if not (keys[pygame.K_UP] or keys[pygame.K_DOWN] or keys[pygame.K_LEFT]):	
				if game_state.in_battle != False:
					game_state.in_battle = False
				if sprite.hold_time == 0:
					if sprite.walking == False:
						if sprite.orient != 'right':
							sprite.orient = 'right'
				sprite.hold_time += 1
				if initial_orientation == 'right':
					if sprite.hold_time > 4 or sprite.orient == 'right':
						sprite.walking = True
						sprite.hold_time = 0
						future_tile_number = sprite.get_number() + Tile.H 
						if future_tile_number in range(1, Tile.total_tiles + 1):
							future_tile = Tile.get_tile(future_tile_number)
							if future_tile.walkable and future_tile_number not in npcs.current_area_tiles:
								sprite.set_target(future_tile)
							elif future_tile.walkable == False or future_tile_number in npcs.current_area_tiles:
								sprite.ani_pos = 0
								print 'no'
							else:
								sprite.hold_time = 0
								sprite.walking = False
								sprite.ani_pos = 0

		
