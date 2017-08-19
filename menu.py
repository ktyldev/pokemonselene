import pygame, game_state, sys, os, filepaths, interaction

basePath = os.path.dirname(__file__)

black = (0, 0 ,0)

screen_x = 480
screen_y = 320

screen = pygame.display.set_mode((screen_x, screen_y))

def create_menu(file_name):
	file_path  = 'images/menu/%s' %file_name
	location = os.path.join(basePath, file_path)
	return location	
	
#-------------------------------------------------


def fixed_by_function():
			
	while game_state.menu_open == True: 
			menu_image = pygame.image.load(create_menu(filepaths.start_menu))
			screen.blit(menu_image, (screen.get_width() - 120, screen.get_height() - 310))
			interaction.interaction(game_state.player_sprite)
			pygame.draw.rect(screen, black, (screen_x - 115, screen_y - (297  - game_state.cursor_pos * 30), 100, 31), 3)
			pygame.display.flip()
			if game_state.saving == True:
				print game_state.current_area
				game_state.save()
				game_state.saving = False	