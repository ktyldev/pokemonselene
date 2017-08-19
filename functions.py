import pygame, os

basePath = os.path.dirname(__file__)

def text_to_screen(screen, text, x, y, size = 15, colour = (255,255,255), font = 'monospace'):

	try:
	
		text = str(text)
		font = pygame.font.SysFont(font, size)
		text = font.render(text, True, colour)
		screen.blit(text, (x, y))
		
	except Exception, e:
		print 'Font Error'
		raise e
		
def draw_text_box(screen, text):
	height = int(screen.get_height() / 3)
	width = screen.get_width()
	pos = (0, screen.get_height() - height)
	rect = (pos, (height, width))
	pygame.draw.rect(screen, (255, 255, 255), rect)
	
def create_background(file_name):
	file_path  = 'images/backgrounds/%s' %file_name
	location = os.path.join(basePath, file_path)
	return location
	
def create_foreground(file_name):
	file_path  = 'images/foregrounds/%s' %file_name
	location = os.path.join(basePath, file_path)
	return location