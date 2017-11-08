import pygame #Module for makingthe game run
import sys #MOdule to exit the game when the user prompts	
from settings import Settings
from ship import Ship

def run_game():
	pygame.init() #Initialised Pygame conditions
	initial_settings=Settings() #Creating an instance of settings
	screen=pygame.display.set_mode((initial_settings.screen_width,initial_settings.screen_height))#Created a screen of size 1200*800
	ship=Ship(screen)
	pygame.display.set_caption("Shoot_Aliens")
	bg_color=(230,230,230)#Background color

	while True:
		gf.check_events(ship);
		gf.update_screen(initial_settings,screen,ship)

run_game()

