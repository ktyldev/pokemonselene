#tile_engine
import pygame, tile_dictionaries

current_tile_map = tile_dictionaries.current_tile_map
#print current_tile_map

class Tile(pygame.Rect):
	
	tile_size = 16
	List = []
	width, height = tile_size, tile_size
	total_tiles = 1
	H, V = 1, tile_dictionaries.current_tile_map['V']
	
	invalids = current_tile_map['invalids']
	spawn_tile = current_tile_map['spawn_tile']
	warp_tiles = current_tile_map['warp_tiles']
	event_tiles = current_tile_map['event_tiles']
		
	"""spawn_tile = 199
	
	event_tiles = (173,182)
	
	warp_tiles = (175, 184)
	
	invalids = (12,15,27,28,29,30,31,32,33,34,35,36,39,40,41,42,43,44,45,46,50,71,74,95,98,102,103,104,105,106,
				111,112,113,114,115,119,122,126,130,135,139,143,146,150,154,159,163,167,170,174,176,177,178,183,
				185,186,187,191,194,215,218,239,242,254,255,256,257,258,259,260,263,266,270,271,272,273,278,284,
				287,290,302,308,311,314,326,327,328,330,331,332,335,338,359,362,383,386,398,399,400,402,403,407,
				410,431,434,455,459,460,461,462,463,464,465,466,467,468,469,470,471,472,473,474,475,476,477,478)
	"""
	def __init__(self, x, y, Type):

		self.type = Type
		self.number = Tile.total_tiles
		Tile.total_tiles += 1
		
		if Type == 'empty':
			self.walkable = True
			self.eventable = False
			self.warpable = False
			self.battleable = False
		elif Type == 'battle_tile':
			self.walkable = True
			self.eventable = False
			self.warpable = False
			self.battleable = True
		elif Type == 'spawn':
			self.walkable = True
			self.eventable = False
			self.warpable = False
			self.battleable = False
		elif Type == 'event_tile':
			self.walkable = False
			self.eventable = True
			self.warpable = False
			self.battleable = False
		elif Type == 'warp_tile':
			self.walkable = True
			self.eventable = False
			self.warpable = True
			self.battleable = False
		else:
			self.eventable = False
			self.walkable = False
			self.warpable = False
			self.battleable = False

		pygame.Rect.__init__(self, (x, y) , (Tile.width, Tile.height) )

		Tile.List.append(self)
			
	@staticmethod
	def get_tile(number):
		for tile in Tile.List:
			if tile.number == number:
				return tile
	
	@staticmethod	
	def clear_tiles():
		for tile in Tile.List:
			tile.type == 'empty'

	@staticmethod
	def draw_tiles(screen):
		for tile in Tile.List:

			if tile.type == 'solid':
				pygame.draw.rect(screen, [255, 0, 0], tile)
			if tile.type == 'battle_tile':
				pygame.draw.rect(screen, [100, 100, 0], tile)
			if tile.type == 'spawn':
				pygame.draw.rect(screen, [0, 0, 255], tile)
			if tile.type == 'event_tile':
				pygame.draw.rect(screen, [0, 255, 0], tile)
			if tile.type == 'warp_tile':
				pygame.draw.rect(screen, [255, 255, 0], tile)
			#functions.text_to_screen(screen, tile.number, tile.x, tile.y, 7)