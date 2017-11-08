import sys #Module to exit the game when the user prompts
import pygame

def check_events(ship):
	"Responds to keypresses and events"
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			sys.exit()
		elif event.type==pygame.KEYDOWN:#Event to regsiter key presses
			if event.key==pygame.K_RIGHT:#When right key is presses, increase the x-coordinate of the ship
				#The ship will be moved toward the right
				ship.rect.centerx+=5

			elif event.key==pygame.K_LEFT:#When left key is pressed, decrease the x-cordinate to make the ship move left
				#The ship will be moved toward the right
				ship.rect.centerx-=5

def update_screen(initial_settings,screen,ship):
	"Updates the screen and casts the recently created screen"
	screen.fill(initial_settings.bg_color)
	ship.blitme()
	pygame.display.flip()#To make the most recently drwan screen visible

