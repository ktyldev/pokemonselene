import os, pygame, random, interaction, game_state, time

from area_data import *
from pokemon_data import *
from player_data import *
from trainer_data import *

pygame.init()
pygame.font.init()

basePath = os.path.dirname(__file__)

poke_font_10 = pygame.font.Font(os.path.join(basePath, 'images/fonts/tf2.ttf'), 10)
poke_font_12 = pygame.font.Font(os.path.join(basePath, 'images/fonts/tf2.ttf'), 12)
poke_font_16 = pygame.font.Font(os.path.join(basePath, 'images/fonts/tf2.ttf'), 16)

player_hp_menu = pygame.image.load(os.path.join(basePath, 'images/sprites/battle/player_hp.png'))
enemy_hp_menu = pygame.image.load(os.path.join(basePath, 'images/sprites/battle/enemy_hp.png'))
top_menu = pygame.image.load(os.path.join(basePath, 'images/sprites/battle/top_menu.png'))
text_menu = pygame.image.load(os.path.join(basePath, 'images/sprites/battle/text_menu.png'))
cursor = pygame.image.load(os.path.join(basePath, 'images/sprites/cursor.png'))
enter_cursor = pygame.image.load(os.path.join(basePath, 'images/sprites/enter.png'))
full_hp = pygame.image.load(os.path.join(basePath, 'images/sprites/battle/hp_100.png'))
move_menu =  pygame.image.load(os.path.join(basePath, 'images/sprites/battle/move_menu.png'))

hp_0 = pygame.image.load(os.path.join(basePath, 'images/sprites/battle/hp_0.png'))
hp_1 = pygame.image.load(os.path.join(basePath, 'images/sprites/battle/hp_1.png'))
hp_3 = pygame.image.load(os.path.join(basePath, 'images/sprites/battle/hp_3.png'))
hp_5 = pygame.image.load(os.path.join(basePath, 'images/sprites/battle/hp_5.png'))
hp_10 = pygame.image.load(os.path.join(basePath, 'images/sprites/battle/hp_10.png'))
hp_15 = pygame.image.load(os.path.join(basePath, 'images/sprites/battle/hp_15.png'))
hp_20 = pygame.image.load(os.path.join(basePath, 'images/sprites/battle/hp_20.png'))
hp_25 = pygame.image.load(os.path.join(basePath, 'images/sprites/battle/hp_25.png'))
hp_30 = pygame.image.load(os.path.join(basePath, 'images/sprites/battle/hp_30.png'))
hp_35 = pygame.image.load(os.path.join(basePath, 'images/sprites/battle/hp_35.png'))
hp_40 = pygame.image.load(os.path.join(basePath, 'images/sprites/battle/hp_40.png'))
hp_45 = pygame.image.load(os.path.join(basePath, 'images/sprites/battle/hp_45.png'))
hp_50 = pygame.image.load(os.path.join(basePath, 'images/sprites/battle/hp_50.png'))
hp_55 = pygame.image.load(os.path.join(basePath, 'images/sprites/battle/hp_55.png'))
hp_60 = pygame.image.load(os.path.join(basePath, 'images/sprites/battle/hp_60.png'))
hp_65 = pygame.image.load(os.path.join(basePath, 'images/sprites/battle/hp_65.png'))
hp_70 = pygame.image.load(os.path.join(basePath, 'images/sprites/battle/hp_70.png'))
hp_75 = pygame.image.load(os.path.join(basePath, 'images/sprites/battle/hp_75.png'))
hp_80 = pygame.image.load(os.path.join(basePath, 'images/sprites/battle/hp_80.png'))
hp_85 = pygame.image.load(os.path.join(basePath, 'images/sprites/battle/hp_85.png'))
hp_90 = pygame.image.load(os.path.join(basePath, 'images/sprites/battle/hp_90.png'))
hp_95 = pygame.image.load(os.path.join(basePath, 'images/sprites/battle/hp_95.png'))
hp_100 = pygame.image.load(os.path.join(basePath, 'images/sprites/battle/hp_100.png'))


#---------------Screen----------
#128*128 sprites
screen_x = 480
screen_y = 320

screen = pygame.display.set_mode((screen_x, screen_y))

#---------functions------------

def create_background(file_name):
	file_path  = 'images/backgrounds/%s' %file_name
	location = os.path.join(basePath, file_path)
	background = pygame.image.load(location)
	print type(background)
	return background

def draw_opening_background(info, type, background):
	
	if type == 'wild':
		image = pygame.image.load(info['front'])
		screen.blit(background, (0, 0))
		screen.blit(image, (285, 30))
		screen.blit(text_menu, (0, 224))
		screen.blit(battle_sprite, (85,114))
	
		
	elif type == 'trainer':
		location = 'images/sprites/npc/%s.png' %info[15]
		trainer_image = pygame.image.load(os.path.join(basePath, location))
		screen.blit(background, (0, 0))
		screen.blit(text_menu, (0, 224))
		screen.blit(trainer_image, (325, 30))
		screen.blit(battle_sprite, (85,114))
	
def load_pokes(type, info):
	if type == 'wild':
		number  = random.randint(0, 100) 
		if number <= info[1]:
			#print info[0]['name']
			return info[0]
		elif number <= info[3]:
			#print info[2]['name']
			return info[2]
		elif number <= info[5]:
			#print info[4]['name']
			return info[4]
		elif number <= info[7]:
			#print info[6]['name']
			return info[6]
		#randomly pick poke from list for each area
	elif type == 'trainer':
		
		if loop_counter == 0:
			game_state.trainer_current_poke = 0
			return info[0]
			
		elif trainer_change == True : 	
			num = random.randint(1,6)
			if num == 1 and game_state.trainer_1 == True:
				game_state.trainer_current_poke = 0
				enemy = info[0]
			if num == 2 and game_state.trainer_2 == True:
				
				game_state.trainer_current_poke = 2
				enemy = info[2]
				
			if num == 3 and game_state.trainer_3 == True:
				
				game_state.trainer_current_poke = 4
				enemy = info[4]
				
			if num == 4 and game_state.trainer_4 == True:
				
				game_state.trainer_current_poke = 6
				enemy = info[6]
				
			if num == 5 and game_state.trainer_5 == True:
				
				game_state.trainer_current_poke = 8
				enemy = info[8]
				
			if num == 6 and game_state.trainer_6 == True:
				
				game_state.trainer_current_poke = 10
				enemy = info[10]
						
		
		#load pokes from a file with trainer info
	elif type == 'special':
		pass
		#load special poke
		

		
		
def type_matchup(attack_move, defense_type_1, defense_type_2):
	pass
	
def calculate_enemy_damage(enemy, slave, player_move):
	#Damage = ((((2 * Level / 5 + 2) * AttackStat * AttackPower / DefenseStat) / 50) + 2) * STAB * Weakness/Resistance * RandomNumber / 100
	type_multiplier = 1
	random_multiplier = random.randint(85, 100)	
	if slave['poke']['type1'] == player_move['type'] or slave['poke']['type2'] == player_move['type']:
		stab = 1.5
	else:
		stab = 1
	
	if player_move['catagory'] == 'physical':
		attack_over_defense = player_move['attk'] / enemy['base_def']
		slave_attack = slave['poke']['base_attk'] + slave['attk']
	else:
		attack_over_defense = player_move['attk'] / enemy['base_sdef']
		slave_attack = slave['poke']['base_sattk'] + slave['sattk']
	#print 'attk/def: ' + str(attack_over_defense)
	#print 'slave attack: ' + str(slave_attack)
	#print 'stab: ' + str(stab)
	#print 'random :' + str(random_multiplier)
	#print 'level : ' + str(slave['level'])
	damage = ((((2 * slave['level'] / 5) + 2) *slave_attack * attack_over_defense) /50 )  *stab * type_multiplier * random_multiplier / 100
	#print 'damage : ' + str(damage)
	return damage

	
def calculate_slave_damage(enemy, slave, enemy_move, enemy_level):
	type_multiplier = 1
	random_multiplier = random.randint(85, 100)	
	if enemy['type1'] == enemy_move['type'] or enemy['type2'] == enemy_move['type']:
		print 'stab!'
		stab = 1.5
	else:
		stab = 1
	
	if enemy_move['catagory'] == 'physical':
		attack_over_defense = enemy_move['attk'] / (slave['poke']['base_def'] + slave['def'])
		enemy_attack = (enemy['base_attk'] + (enemy_level * enemy['attk_increase']))
	else:
		attack_over_defense = enemy_move['attk'] / (slave['poke']['base_sdef'] + slave['sdef'])
		enemy_attack = enemy['base_sattk'] + (enemy_level * enemy['sattk_increase'])
	#print 'attk/def: ' + str(attack_over_defense)
	#print 'slave attack: ' + str(slave_attack)
	#print 'stab: ' + str(stab)
	#print 'random :' + str(random_multiplier)
	#print 'level : ' + str(slave['level'])
	damage = ((((2 * enemy_level / 5) + 2) *enemy_attack * attack_over_defense) /50 )  *stab * type_multiplier * random_multiplier / 100
	#print 'damage : ' + str(damage)
	return damage
	
def enemy_turn(enemy, enemy_level):
	print 'enemy\'s turn'
	e_move1 = False
	e_move2 = False
	e_move3 = False
	e_move4 = False
	random_number = random.randint(0, 100)
	if random_number <= 25:
		if enemy_level >= enemy['move1level']:
			e_move1 = True
			print 'enemy uses %s' %enemy['move1']['name']
			
		elif enemy_level >= enemy['move2level']:
			
			e_move2 = True
			print 'enemy uses %s' %enemy['move2']['name']
		elif enemy_level >= enemy['move3level']:
			
			e_move3 = True
			print 'enemy uses %s' %enemy['move3']['name']
		elif enemy_level >= enemy['move4level']:
			
			e_move4 = True	
			print 'enemy uses %s' %enemy['move4']['name']
			
	elif random_number <= 50:
	
		if enemy_level >= enemy['move2level'] and e_move2 != True:
			
			e_move2 = True
			print 'enemy uses %s' %enemy['move2']['name']
		elif enemy_level >= enemy['move3level'] and e_move3 != True:
		
			e_move3 = True
			print 'enemy uses %s' %enemy['move3']['name']
		elif enemy_level >= enemy['move4level'] and e_move4 != True:
			
			e_move4 = True	
			print 'enemy uses %s' %enemy['move4']['name']
			
	elif random_number <= 75:
	
		if enemy_level >= enemy['move3level'] and e_move3 != True:
			
			e_move3 = True
			print 'enemy uses %s' %enemy['move3']['name']
		elif enemy_level >= enemy['move4level'] and e_move4 != True:
			
			e_move4 = True		
			print 'enemy uses %s' %enemy['move4']['name']
			
	elif random_number <= 100:
	
		if enemy_level >= enemy['move4level'] and e_move4 != True:
			
			e_move4 = True	
			print 'enemy uses %s' %enemy['move4']['name']
			
	
	if e_move1 == True:
		return enemy['move1']
	elif e_move2 == True:
		return enemy['move2']
	elif e_move3 == True:
		return enemy['move3']
	elif e_move4 == True:
		return enemy['move4']
		
	
def load_player_pokes():
	 
	if loop_counter == 0:
		game_state.slave = player_pokes[0]
		return player_pokes[0]
		
	elif player_change == True:
		pass #pick from poke menu

def opening_trainer(info, background):
	type = 'trainer'
	draw_opening_background(info, type, background)
	pygame.display.flip()
	text = ' '
	wait = None
	text_done = False
	while wait == None:
		
		if text_done == False:
			for i in range(len(info[14])):
				interaction.check_for_exit()
				draw_opening_background(info, type, background)
				time.sleep(.1/game_state.text_speed)
				text += info[14][i]
				text_image = poke_font_12.render(text, 1, (5, 5, 5))
				screen.blit(text_image, (15, 250))
				pygame.display.flip()
				text_done = True
		screen.blit(enter_cursor, (450 , 290))	
		pygame.display.flip()
		#wait = interaction.wait_for_continue()
		game_state.battle_menu_mode = 1
		wait = interaction.battle_interaction('wait')
		

def opening_wild(enemy, background):
	type = 'wild'
	text = ' '
	end_text = 'A wild %s attacks!' %enemy['name']
	wait = None
	text_done = False
	while wait == None:
		
		if text_done == False:
			for i in range(len(end_text)):
				interaction.check_for_exit()
				draw_opening_background(enemy, type, background)
				time.sleep(.1/game_state.text_speed)
				text += end_text[i]
				text_image = poke_font_12.render(text, 1, (255, 5, 5))
				screen.blit(text_image, (15, 250))
				pygame.display.flip()
				text_done = True
		screen.blit(enter_cursor, (450 , 290))	
		pygame.display.flip()
		#wait = interaction.wait_for_continue()
		game_state.battle_menu_mode = 1
		wait = interaction.battle_interaction('wait')
		
		
def load_images(enemy, slave):
	enemy_sprite = pygame.image.load(enemy['front'])
	slave_sprite = pygame.image.load(slave['poke']['back'])
	return enemy_sprite, slave_sprite
	
def get_enemy_level(type, info):
	
	if type == 'wild':
		if loop_counter == 0:
			game_state.wild_level = random.randint(info[12], info[13])
		return game_state.wild_level	
			
	elif type == 'trainer':
		level = info[game_state.trainer_current_poke + 1]
		return level
	elif type == 'special':
		pass

def get_hp(enemy, slave, enemy_damage, slave_damage, enemy_level):
	base_enemy_hp = (enemy['base_hp'] +(enemy_level * enemy['hp_increase']))
	enemy_hp = base_enemy_hp - enemy_damage
	print 'enemy_hp : ' + str(enemy_hp)
	base_slave_hp = (slave['poke']['base_hp'] + slave['hp'] + (slave['level']*slave['poke']['hp_increase']))
	slave_hp = base_slave_hp - slave_damage
	return enemy_hp, slave_hp, base_enemy_hp, base_slave_hp
	
def draw_hp(enemy_hp, slave_hp, base_enemy_hp, base_slave_hp):
	enemy_percentage = enemy_hp/base_enemy_hp
	print 'e%:' + str(enemy_percentage)
	slave_percentage = slave_hp/base_slave_hp
	
	#print enemy_percentage, slave_percentage
	if enemy_percentage == 1:
		enemy_bar = full_hp
	elif enemy_percentage > .95:
		enemy_bar = hp_95
		print '95'
	elif enemy_percentage > .9:
		enemy_bar = hp_90
		print '90'
	elif enemy_percentage > .85:
		enemy_bar = hp_85
		print '85'
	elif enemy_percentage > .8:
		enemy_bar = hp_80	
		print '80'
	elif enemy_percentage > .75:
		enemy_bar = hp_75	
	elif enemy_percentage > .7:
		enemy_bar = hp_70	
	elif enemy_percentage > .65:
		enemy_bar = hp_65	
	elif enemy_percentage > .6:
		enemy_bar = hp_60	
	elif enemy_percentage > .55:
		enemy_bar = hp_55
	elif enemy_percentage > .5:
		enemy_bar = hp_50
	elif enemy_percentage > .45:
		enemy_bar = hp_45
	elif enemy_percentage > .4:
		enemy_bar = hp_40
	elif enemy_percentage > .35:
		enemy_bar = hp_35
	elif enemy_percentage > .3:
		enemy_bar = hp_30
	elif enemy_percentage > .25:
		enemy_bar = hp_25	
	elif enemy_percentage > .2:
		enemy_bar = hp_20
	elif enemy_percentage > .15:
		enemy_bar = hp_15
	elif enemy_percentage > .1:
		enemy_bar = hp_10
	elif enemy_percentage > .05:
		enemy_bar = hp_5		
	elif enemy_percentage > .03:
		enemy_bar = hp_3
	elif enemy_percentage < 0:
		enemy_bar = hp_0	
	else:
		enemy_bar = hp_1

		
	if slave_percentage == 1:
		slave_bar = full_hp
	elif slave_percentage > .95:
		slave_bar = hp_95
	elif slave_percentage > .9:
		slave_bar = hp_90
	elif slave_percentage > .85:
		slave_bar = hp_85
	elif slave_percentage > .8:
		slave_bar = hp_80	
	elif slave_percentage > .75:
		slave_bar = hp_75	
	elif slave_percentage > .7:
		slave_bar = hp_70	
	elif slave_percentage > .65:
		slave_bar = hp_65	
	elif slave_percentage > .6:
		slave_bar = hp_60	
	elif slave_percentage > .55:
		slave_bar = hp_55
	elif slave_percentage > .5:
		slave_bar = hp_50
	elif slave_percentage > .45:
		slave_bar = hp_45
	elif slave_percentage > .4:
		slave_bar = hp_40
	elif slave_percentage > .35:
		slave_bar = hp_35
	elif slave_percentage > .3:
		slave_bar = hp_30
	elif slave_percentage > .25:
		slave_bar = hp_25	
	elif slave_percentage > .2:
		slave_bar = hp_20
	elif slave_percentage > .15:
		slave_bar = hp_15
	elif slave_percentage > .1:
		slave_bar = hp_10
	elif slave_percentage > .05:
		slave_bar = hp_5		
	elif slave_percentage > .03:
		slave_bar = hp_3
	elif slave_percentage > 0.1:
		slave_bar = hp_1
	else:
		slave_bar = hp_0	
		
	return enemy_bar, slave_bar


#-----------stuff-----------


#enemy_changed = False
current_poke = 1
player_move = ''


def commence(type, info):		#info is area or trainer info or special poke info(all as lists or dictionaries)
	global turn_counter, selected, no_pp_text, attacked, enemy_changed, run, loop_counter, trainer_change, player_change, player_move, enemy_damage, enemy_battle_turn, change_run
	enemy_changed = False
	no_pp_text = ''
	turn_counter = 0.0
	run = 0
	loop_counter = 0
	trainer_change = False
	player_change = False
	player_move = None
	enemy_damage = 0
	enemy_battle_turn = False
	change_run = False
	
	
	if type == 'wild':
		enemy = load_pokes(type, info)
		game_state.battle_type = 'wild'
		background = create_background(info[14])
		opening_wild(enemy, background)
		
		
	elif type == 'trainer':
		game_state.battle_type = 'trainer'
		background = create_background(info[17])
		opening_trainer(info, background)
		
		if info[0] != no_poke:
			game_state.trainer_1 = True
			if info[2] != no_poke:
				game_state.trainer_2 = True
				if info[4] != no_poke:
					game_state.trainer_3 = True
					if info[6] != no_poke:
						game_state.trainer_4 = True
						if info[8] != no_poke:
							game_state.trainer_5 = True
							if info[10] != no_poke:
								game_state.trainer_6 = True
	
	
	elif type == 'special':
		game_state.battle_type = 'special'
		pass

	
	
	while True:
		
		print 'menu' + str(game_state.battle_menu_mode)
		
		
		
		for event in pygame.event.get():
	
			if event.type == pygame.QUIT:

				pygame.quit()
				sys.exit()
		
		
		if loop_counter == 0:
			enemy_damage = 0
			slave_damage = 0
		
		if loop_counter == 0 or trainer_change == True:
			enemy = load_pokes(type, info)
			enemy_level = get_enemy_level(type, info)
		
		if loop_counter == 0 or player_change == True:
			slave = load_player_pokes() 
		
		enemy_hp, slave_hp, base_enemy_hp, base_slave_hp = get_hp(enemy, slave, enemy_damage, 0, enemy_level)
		print 'enemy_hp' + str(enemy_hp)
		
		enemy_level_text = poke_font_12.render(str(enemy_level), 1, (5, 5, 5))
		slave_level_text = poke_font_12.render(str(slave[('level')]), 1, (5, 5, 5))
		

		enemy_name_text = poke_font_12.render(enemy['name'], 1, (5, 5, 5))
		slave_name_text = poke_font_12.render(slave['nick'], 1, (5, 5, 5))
		
		
		enemy_image, slave_image = load_images(enemy, slave) 
		
		
		slave_move1_pp = slave['move1']['pp'] - slave['pp1']
		slave_move2_pp = slave['move2']['pp'] - slave['pp2']
		slave_move3_pp = slave['move3']['pp'] - slave['pp3']
		slave_move4_pp = slave['move4']['pp'] - slave['pp4']
		
		
		enemy_hp_text = '%d / %d' %(enemy_hp, base_enemy_hp)
		enemy_hp_text_image = poke_font_16.render(enemy_hp_text, 1, (5, 5, 5))
		slave_hp_text = '%d / %d' %(slave_hp, base_slave_hp)
		slave_hp_text_image = poke_font_16.render(slave_hp_text, 1, (5, 5, 5))
	
		enemy_bar, slave_bar = draw_hp(enemy_hp, slave_hp, base_enemy_hp, base_slave_hp)
		
		
		
		"""
		else:
			
			screen.blit(background, (0, 0))
			#screen.blit(enemy_image, (285,30))
			screen.blit(slave_image, (70, 135))
			screen.blit(player_hp_menu, (275, 150))
			screen.blit(slave_bar, (350, 188))
			screen.blit(slave_name_text, (300, 170))
			screen.blit(slave_level_text, (430, 172))
			screen.blit(slave_hp_text_image, (300, 190))
			screen.blit(enemy_hp_menu, (20, 40))
			screen.blit(enemy_bar, (88, 83))
			screen.blit(enemy_name_text, (30, 65))
			screen.blit(enemy_level_text, (167, 67))
			screen.blit(enemy_hp_text_image, (30, 85))
			screen.blit(text_menu, (0, 224))
			text = ' '
			end_text = '%s fainted!' %enemy['name']
			wait = None
			text_done = False
			while wait == None:
				
				if text_done == False:
					for i in range(len(end_text)):
						interaction.check_for_exit()
						time.sleep(.1/game_state.text_speed)
						text += end_text[i]
						text_image = poke_font_16.render(text, 1, (5, 5, 5))
						screen.blit(text_menu, (0, 224))
						screen.blit(text_image, (15, 250))
						pygame.display.flip()
						text_done = True
				screen.blit(enter_cursor, (450 , 290))	
				pygame.display.flip()
				wait = interaction.wait_for_continue()	
		
			
			if game_state.trainer_current_poke == 0:
				game_state.trainer_1 = False
			if game_state.trainer_current_poke == 2:
				game_state.trainer_2 = False
			if game_state.trainer_current_poke == 4:
				game_state.trainer_3 = False
			if game_state.trainer_current_poke == 6:
				game_state.trainer_4 = False	
			if game_state.trainer_current_poke == 8:
				game_state.trainer_5 = False
			if game_state.trainer_current_poke == 10:
				game_state.trainer_6 = False	
				
			
			if type == 'wild' or type == 'special':
				print 'now return to overworld'
				
			else:
				if game_state.trainer_1 == False and game_state.trainer_2 == False:
					if game_state.trainer_3 == False and game_state.trainer_4 == False:
						if game_state.trainer_5 == False and game_state.trainer_6 == False:
							print 'opponent is defeat. :D now return to overworld'
							
				unchosen = True
				while unchosen == True:
					num = random.randint(1,6)
					if num == 1 and game_state.trainer_1 == True:
						unchosen = False
						game_state.trainer_current_poke = 0
						enemy = info[0]
						enemy_level = info[1]
					if num == 2 and game_state.trainer_2 == True:
						unchosen = False
						game_state.trainer_current_poke = 2
						enemy = info[2]
						enemy_level = info[3]
					if num == 3 and game_state.trainer_3 == True:
						unchosen = False
						game_state.trainer_current_poke = 4
						enemy = info[4]
						enemy_level = info[5]
					if num == 4 and game_state.trainer_4 == True:
						unchosen = False
						game_state.trainer_current_poke = 6
						enemy = info[6]
						enemy_level = info[7]
					if num == 5 and game_state.trainer_5 == True:
						unchosen = False
						game_state.trainer_current_poke = 8
						enemy = info[8]
						enemy_level = info[9]
					if num == 6 and game_state.trainer_6 == True:
						unchosen = False
						game_state.trainer_current_poke = 10
						enemy = info[10]
						enemy_level = info[11]
					enemy_damage = 0	
					enemy_changed = True
					print enemy['name']
					print enemy_level
				
		"""
		#whatever = interaction.battle_interaction()
		""" enemy_turn here
		if turn_counter % 1 != 0:
			
			enemy_move = enemy_turn(enemy, enemy_level)
			damage_to_slave = calculate_slave_damage(enemy, slave, enemy_move, enemy_level)
			enemy_move_text = '%s uses %s' %(enemy['name'], enemy_move['name'])
			
			
			
			print damage_to_slave
			wait = None
			text_done = False
			word = ''
			
			while wait == None:
				if text_done == False:
					for i in range(len(enemy_move_text)):
						
						word += enemy_move_text[i]
						word_text = poke_font_16.render(word, 1, (5, 5, 5))
						screen.blit(text_menu, (0, 224))
						screen.blit(word_text, (20, 250))
						
						
						pygame.display.flip()
						time.sleep(.1/game_state.text_speed)
						
						
						
					text_done = True		
			
			
				screen.blit(enter_cursor, (450 , 290))
				pygame.display.flip()
				wait = interaction.wait_for_continue()
			
			
			
			slave_hp -= damage_to_slave
			slave_hp_text_image = poke_font_16.render(slave_hp_text, 1, (5, 5, 5))
			screen.blit(slave_hp_text_image, (300, 190))
			pygame.display.update()
			turn_counter += 0.5
		"""
		
		if run == 1:
			whatever = interaction.battle_interaction('none')
		else:
			change_run = True
		
		enemy_bar, slave_bar = draw_hp(enemy_hp, slave_hp, base_enemy_hp, base_slave_hp)
		
		screen.blit(background, (0, 0))
		screen.blit(enemy_image, (285,30))
		screen.blit(slave_image, (70, 135))
		screen.blit(player_hp_menu, (275, 150))
		screen.blit(slave_bar, (350, 188))
		screen.blit(slave_name_text, (300, 170))
		screen.blit(slave_level_text, (430, 172))
		screen.blit(slave_hp_text_image, (300, 190))
		screen.blit(enemy_hp_menu, (20, 40))
		screen.blit(enemy_bar, (88, 83))
		screen.blit(enemy_name_text, (30, 65))
		screen.blit(enemy_level_text, (167, 67))
		screen.blit(enemy_hp_text_image, (30, 85))
		screen.blit(text_menu, (0, 224))	
		
		if turn_counter % 1 != 0:
			
			enemy_move = enemy_turn(enemy, enemy_level)
			damage_to_slave = calculate_slave_damage(enemy, slave, enemy_move, enemy_level)
			enemy_move_text = '%s uses %s' %(enemy['name'], enemy_move['name'])
			
			
			
			print damage_to_slave
			wait = None
			text_done = False
			word = ''
			
			while wait == None:
				if text_done == False:
					for i in range(len(enemy_move_text)):
						
						word += enemy_move_text[i]
						word_text = poke_font_16.render(word, 1, (5, 5, 5))
						screen.blit(text_menu, (0, 224))
						screen.blit(word_text, (20, 250))
						
						
						pygame.display.flip()
						time.sleep(.1/game_state.text_speed)
						
						
						
					text_done = True		
			
			
				screen.blit(enter_cursor, (450 , 290))
				pygame.display.flip()
				#wait = interaction.wait_for_continue()
				wait = 'some'
			
			
			slave_hp -= damage_to_slave
			slave_hp_text_image = poke_font_16.render(slave_hp_text, 1, (5, 5, 5))
			screen.blit(slave_hp_text_image, (300, 190))
			screen.blit(background, (0, 0))
			screen.blit(enemy_image, (285,30))
			screen.blit(slave_image, (70, 135))
			screen.blit(player_hp_menu, (275, 150))
			screen.blit(slave_bar, (350, 188))
			screen.blit(slave_name_text, (300, 170))
			screen.blit(slave_level_text, (430, 172))
			screen.blit(slave_hp_text_image, (300, 190))
			screen.blit(enemy_hp_menu, (20, 40))
			screen.blit(enemy_bar, (88, 83))
			screen.blit(enemy_name_text, (30, 65))
			screen.blit(enemy_level_text, (167, 67))
			screen.blit(enemy_hp_text_image, (30, 85))
			screen.blit(text_menu, (0, 224))	
			pygame.display.flip()
			turn_counter += 0.5
			enemy_battle_turn = True
		
		if enemy_battle_turn != True:
			print 'gets to menu 1 code'
			print 'menu mode = ' +  str(game_state.battle_menu_mode)
			if game_state.battle_menu_mode == 1:
				print 'enters menu 1'
				
				screen.blit(top_menu, (260, 224))
				ask = 'What will %s do?' %slave['poke']['name']
				ask_text = poke_font_12.render(ask, 1, (5,5,5))
				screen.blit(ask_text, (20,250))
				if game_state.battle_cursor_pos == 0:
					screen.blit(cursor, (277,245))
				elif game_state.battle_cursor_pos == 10:
					screen.blit(cursor, (277, 275))
				elif game_state.battle_cursor_pos == 1:
					screen.blit(cursor, (383, 245))
				elif game_state.battle_cursor_pos == 11:
					screen.blit(cursor, (383, 275))
			
			elif game_state.battle_menu_mode == 2:
				print 'menu mode 2'
				
			
				if slave['move1'] != None:
					move1 = slave['move1']['name']
					move1text = poke_font_12.render(move1, 1, (5,5,5)) 
					m1 = True
				else:
					m1 = False
				if slave['move2'] != None:
					move2 = slave['move2']['name']
					move2text = poke_font_12.render(move2, 1, (5,5,5)) 
					m2 = True
				else:
					m2 = False
				if slave['move3'] != None:
					move3 = slave['move3']['name']
					move3text = poke_font_12.render(move3, 1, (5,5,5)) 
					m3 = True
				else:
					m3 = False
				if slave['move4'] != None:
					move4 = slave['move4']['name']
					move4text = poke_font_12.render(move4, 1, (5,5,5)) 
					m4 = True
				else:
					m4 = False
				
				screen.blit(move_menu, (0, 227))
				
				if m1 == True:
					screen.blit(move1text, (50, 250))
				if m2 == True:
					screen.blit(move2text, (150, 250))
				if m3 == True:
					screen.blit(move3text, (50, 290))
				if m4 == True:
					screen.blit(move4text, (150, 290))
				
				if game_state.battle_cursor_pos == 0:
					screen.blit(cursor, (30,245))
					max_pp_text = poke_font_16.render(str(slave['move1']['pp']), 1, (5, 5, 5))
					pp_text = poke_font_16.render(str(slave_move1_pp), 1, (5, 5, 5))
					type_text = poke_font_16.render(slave['move1']['type'], 1, (5, 5, 5))
				elif game_state.battle_cursor_pos == 10:
					screen.blit(cursor, (30, 285))
					max_pp_text = poke_font_16.render(str(slave['move3']['pp']), 1, (5, 5, 5))
					pp_text = poke_font_16.render(str(slave_move3_pp), 1 , (5, 5, 5))
					type_text = poke_font_16.render(slave['move3']['type'], 1, (5, 5, 5))
				elif game_state.battle_cursor_pos == 1:
					max_pp_text = poke_font_16.render(str(slave['move2']['pp']), 1, (5, 5, 5))
					screen.blit(cursor, (130, 245))
					pp_text = poke_font_16.render(str(slave_move2_pp), 1, (5, 5, 5))
					type_text = poke_font_16.render(slave['move2']['type'], 1, (5, 5, 5))
				elif game_state.battle_cursor_pos == 11:
					max_pp_text = poke_font_16.render(str(slave['move4']['pp']), 1, (5, 5, 5))
					screen.blit(cursor, (130, 285))
					pp_text = poke_font_16.render(str(slave_move4_pp), 1, (5, 5, 5))
					type_text = poke_font_16.render(slave['move4']['type'], 1, (5, 5, 5))
				screen.blit(pp_text, (408, 250))
				screen.blit(max_pp_text, (443, 250))
				screen.blit(type_text, (393, 283))
				
				pygame.display.flip()
			
			run = 1
			
			
			if turn_counter % 1 == 0:
			
				if player_move != None:
					print 'there is a battle move'
					print player_move['name']
					
			
					if player_move == slave['move1'] :
						if slave_move1_pp  > 0 :
							slave['pp1'] += 1
							attacked = True
						else :
							no_pp_text = '%s has no PP!' %slave['move1']['name']
							attacked = False
						
					elif player_move == slave['move2'] :
						if slave_move2_pp > 0 :
							slave['pp2'] += 1
							attacked = True
						else:
							no_pp_text = '%s has no PP!' %slave['move2']['name']
							attacked = False	
						
					elif player_move == slave['move3'] :
						if slave_move3_pp > 0 :
							slave['pp3'] += 1
							attacked = True
						else:
							no_pp_text = '%s has no PP!' %slave['move3']['name']
							attacked = False
						
					elif player_move == slave['move4'] :
						if slave_move4_pp  > 0 :
							slave['pp4'] += 1
							attacked = True
						else:
							no_pp_text = '%s has no PP!' %slave['move4']['name']
							attacked = False
						
					
					word = ''
					wait = None
					text_done = False
					if attacked == True:
					
						attack_text = '%s used %s!' %(slave['nick'], player_move['name'])
						
						screen.blit(text_menu, (0, 224))
						
						while wait == None:
							if text_done == False:
								for i in range(len(attack_text)):
									word += attack_text[i]
									screen.blit(text_menu, (0, 224))
									word_text = poke_font_16.render(word, 1, (5, 5, 5))
									screen.blit(word_text, (20, 250))
									pygame.display.flip()
									time.sleep(.1/game_state.text_speed)
								
								text_done = True
							
							
							screen.blit(enter_cursor, (450 , 290))
							pygame.display.flip()
							#wait = interaction.wait_for_continue()
							wait = interaction.battle_interaction('wait')
							
						
						enemy_damage += calculate_enemy_damage(enemy, slave, player_move)
						print 'damage to enemy : ' + str(enemy_damage)
						
						print 'enemy_hp' + str(enemy_hp)
						enemy_hp_text = '%d / %d' %(enemy_hp, base_enemy_hp)
						enemy_hp_text_image = poke_font_16.render(enemy_hp_text, 1, (5, 5, 5))
						
						#pygame.display.flip()
						turn_counter += 0.5
						player_move = None
						
					else:
						#no_pp_text_image = poke_font_16.render(no_pp_text, 1,  (5, 5, 5))
						screen.blit(text_menu, (0, 224))
						word = ''
						wait = None
						text_done = False
						
						while wait == None:
							if text_done == False:
								for i in range(len(no_pp_text)):
									word += no_pp_text[i]
									screen.blit(text_menu, (0, 224))
									word_text = poke_font_16.render(word, 1, (5, 5, 5))
									screen.blit(word_text, (20, 250))
									pygame.display.flip()
									time.sleep(.1/game_state.text_speed)
									text_done = True
							
							screen.blit(enter_cursor, (450 , 290))
							pygame.display.flip()	
							wait = interaction.wait_for_continue()
							
							screen.blit(background, (0, 0))
							screen.blit(enemy_image, (285,30))
							screen.blit(slave_image, (70, 135))
							screen.blit(player_hp_menu, (275, 150))
							screen.blit(slave_bar, (350, 188))
							screen.blit(slave_name_text, (300, 170))
							screen.blit(slave_level_text, (430, 172))
							screen.blit(slave_hp_text_image, (300, 190))
							screen.blit(enemy_hp_menu, (20, 40))
							screen.blit(enemy_bar, (88, 83))
							screen.blit(enemy_name_text, (30, 65))
							screen.blit(enemy_level_text, (167, 67))
							screen.blit(enemy_hp_text_image, (30, 85))
							screen.blit(text_menu, (0, 224))	
				
							
							
			player_move = None
		#print turn_counter 
		
		
		
		#print 'enemy_hp' + str(enemy_hp)
		
		
		
		pygame.display.flip()
		
		loop_counter += 1
		enemy_battle_turn = False
		
		
		if change_run == True:
			run = 1
		
		print 'loop_counter :' + str(loop_counter)
		print 'enemy_damage :' + str(enemy_damage)
		
		
