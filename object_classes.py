import pygame, glob, os, game_state, npcs, tile_engine, random
from tile_engine import Tile

screen_x = 480
screen_y = 320

tile_size = 16

def return_coords(tile):
	y = (tile / tile_engine.Tile.V) * tile_size
	x = tile * tile_size - (tile_engine.Tile.V * y) - tile_size
	return x, y
	
def draw_npcs(screen, camera_x_offset, camera_y_offset):
	r = character.width / 2
	
	dict = {}
	
	for sprite in npcs.current_area:
		dict[sprite] =  npcs.current_area[sprite]['tile']
		
			
		
#	print 'dict'
#	print dict
	for sprite in dict:
		
		npcs.current_area_tiles.append(dict[sprite])
		x_coord_raw = return_coords(dict[sprite])[0]
		x_coord = return_coords(dict[sprite])[0] + camera_x_offset + r 
		y_coord_raw = return_coords(dict[sprite])[1]
		y_coord = return_coords(dict[sprite])[1] + camera_y_offset + r
		pygame.draw.circle(screen, [50, 50, 50], (x_coord, y_coord), r)

class character(pygame.Rect): #inherits attributes of the Rect
	width, height = Tile.tile_size, Tile.tile_size #Rect dimensions
	
	def __init__(self, x, y):
	
		self.tx, self.ty = None, None
		pygame.Rect.__init__(self, x, y, character.width, character.height) #makes a rectangle the size of a tile and 
																			#assigns it to the player's position
		
	def set_target(self, next_tile):				#sets the target to the tile in front of the player
		if self.tx == None and self.ty == None:		# 
			self.tx = next_tile.x
			self.ty = next_tile.y
	
	def get_number(self): #gets the number of the tile the player is standing on
	
		return ((self.x / self.width) + Tile.H) + ((self.y / self.height) * Tile.V)
				
class player(character):

	camera_x = 0
	camera_y = 0

	def __init__(self, x, y):	
		character.__init__(self, x, y)
		basePath = os.path.dirname(__file__)
		spritePath = os.path.join(basePath, "images/sprites/player/*.png")
		self.sprites = glob.glob(spritePath)
		
		self.orient = game_state.player_orientation
		self.initial_orient = game_state.player_orientation
		self.sprites.sort()
		self.frame_count = 0
		self.ani_pos = 0
		self.dx = 0
		self.ani_down = self.sprites[0:3]
		self.ani_left = self.sprites[4:7]
		self.ani_right = self.sprites[8:11]
		self.ani_up = self.sprites[12:15]
		self.image = pygame.image.load(self.sprites[self.ani_pos])
		self.walking = False
		self.camera_x -= self.x - screen_x / 2 + 16 #draw a diagram to help understand this formula, the +16 is an offset
		self.camera_y -= self.y - screen_y / 2      #to line the sprite up with the middle of the screen
		self.hold_time = 0
		
	def movement(self):
		if self.tx != None and self.ty != None: # Target tile is set

			init_x = self.x
			init_y = self.y
			
			X = self.x - self.tx
			Y = self.y - self.ty

			vel = 4
			
			if X < 0: # --->
				self.walking = True
				self.x += vel
				self.camera_x -= vel
			elif X > 0: # <----
				self.walking = True
				self.x -= vel
				self.camera_x += vel
			if Y > 0: # up
				self.walking = True
				self.y -= vel
				self.camera_y += vel
			elif Y < 0: # down
				self.walking = True
				self.y += vel
				self.camera_y -= vel		
			if X == 0 and Y == 0:
				self.tx, self.ty = None, None
			if init_x != self.x or init_y != self.y:
				if self.x / 16.0 % 1.0 == 0.0:
					if self.y / 16.0 % 1.0 == 0.0:
						game_state.on_tile_active = True
						game_state.encounter_lock = False
						game_state.check_for_encounter = True
#						print game_state.check_for_encounter
			else:
				game_state.on_tile_active = False
			self.frame_count += 1

			
	def draw(self, screen, camera_x_offset, camera_y_offset):
	
		r = self.width / 2
		if self.frame_count > 3:
				self.ani_pos += 1
				self.frame_count = 0
				if self.ani_pos > 3 or self.walking == False:
					self.ani_pos = 0
		if self.orient == 'up':
			self.image = pygame.image.load(self.sprites[12 + self.ani_pos])
		elif self.orient == 'down':
			self.image = pygame.image.load(self.sprites[0 + self.ani_pos])
		elif self.orient == 'left':
			self.image = pygame.image.load(self.sprites[4 + self.ani_pos])
		elif self.orient == 'right':
			self.image = pygame.image.load(self.sprites[8 + self.ani_pos])
		
		screen.blit(self.image, (self.x + camera_x_offset, self.y - r + 3 + camera_y_offset))

class Npc(character):
	
	List = []
	
	def __init__(self, tile, coords, text = None, movement = True, range = None):
		self.tile = tile
		x = coords[0] - self.width / 2
		y = coords[1] - self.width / 2
		self.walking = False
		self.frame_count = 0
		character.__init__(self, x, y)
		self.text = text
#		self.image =
		Npc.List.append(self)
		self.id = str(len(Npc.List))
		self.can_move = movement
		self.X, self.Y = 0, 0
		self.orient = "down"
		self.range = range
		
	def move_calc(self):

		move_probability = random.randint(0, 1000)
		if move_probability < 10:
			directions = ('N', 'E', 'S', 'W')
			direction_picker = random.randint(0, 3)
			movement_direction = directions[direction_picker]
			#print x + ' movement ' + movement_direction
			
			if movement_direction == 'N':
				future_tile_number = current_area[x]['tile'] - Tile.V
			if movement_direction == 'E':
				future_tile_number = current_area[x]['tile'] + Tile.H
			if movement_direction == 'S':
				future_tile_number = current_area[x]['tile'] + Tile.V
			if movement_direction == 'W':
				future_tile_number = current_area[x]['tile'] - Tile.H
				
			if future_tile_number in range(1, Tile.total_tiles + 1):
				future_tile = Tile.get_tile(future_tile_number)
				if future_tile.walkable == True:
					if future_tile_number != game_state.player_sprite.get_number():
						if future_tile_number not in current_area_tiles:
							#print future_tile_number				
							current_area[x]['target'] = future_tile_number
							#print current_area[x]['target']
		self.target = future_tile_number

	def move_with_bg(self):
		if player.tx != None and player.ty != None: # Target tile is set

			init_x = self.x
			init_y = self.y
			
			X = self.x - self.tx
			Y = self.y - self.ty

			vel = 4

			if X < 0: # --->
				self.x -= vel
#				self.camera_x -= vel
			elif X > 0: # <----
				self.x += vel
#				self.camera_x += vel
			if Y > 0: # up
				self.y += vel
#				self.camera_y += vel
			elif Y < 0: # down
				self.y -= vel
		
	def movement(self):

		if self.tx != None and self.ty != None: # Target tile is set
			
			init_tile = self.tile
			init_x = self.x
			init_y = self.y 
			
			X = self.x - self.tx
			Y = self.y - self.ty
			
			if X != 0 and Y != 0:
				X, Y = 0, 0

			if X == 0 or Y == 0:
				vel = 4
				
				if X < 0: # --->
					self.walking = True
					self.x += vel
					self.dir = "e"
				elif X > 0: # <----
					self.walking = True
					self.x -= vel
					self.dir = "w"
				if Y > 0: # up
					self.walking = True
					self.y -= vel
					self.dir = "n"
				elif Y < 0: # down
					self.walking = True
					self.y += vel
					self.dir = "s"
				if X == 0 and Y == 0:
					self.tx, self.ty = None, None
				if init_x != self.x or init_y != self.y:				
					if self.x / 16.0 % 1.0 == 0.0:
						if self.y / 16.0 % 1.0 == 0.0:
							self.walking = False
							if self.dir == "n":
								self.tile -= Tile.V
							elif self.dir == "e":
								self.tile += Tile.H
							elif self.dir == "s":
								self.tile += Tile.V
							elif self.dir == "w":
								self.tile -= Tile.H
				self.frame_count += 1
			
	def show_text(self):
		print self.text
			
	def draw(self, screen, xoffset, yoffset):
	
		r = self.width / 2
		pygame.draw.rect(screen, [0,0,255], ((self.x + xoffset, self.y + yoffset - 4), (16, 20)))			