import pygame,sys

CELL_SIZE = 30
CELL_NUMBER = 20
WINDOW_SIZE = CELL_SIZE * CELL_NUMBER
screen = None

def init():
	"""
	Initializes pygame and sets up the window.
	and any other graphics related stuff.
	"""
	global screen
	pygame.init()
	pygame.display.set_caption("Super Snake")
	screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))

def quit():
	"""
	Shuts down pygame.
	"""
	pygame.quit()
	sys.exit()

def get_screen():
    return screen

def fill_screen():
	global screen
	screen.fill("green")
	bg = pygame.image.load("graphics/assets/images/bg.png")
	screen.blit(bg, (0, 0))



    