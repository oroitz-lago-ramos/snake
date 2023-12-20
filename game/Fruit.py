import pygame as pg
import game
import graphics
import random

class Fruit:
    def __init__(self) -> None:
        self.x = random.randint(0, graphics.CELL_NUMBER - 1)
        self.y = random.randint(0, graphics.CELL_NUMBER - 1) 
        self.pos = pg.Vector2(self.x, self.y)
    
    def draw_fruit(self):
        screen = graphics.get_screen()
        x = self.pos.x * graphics.CELL_SIZE
        y = self.pos.y * graphics.CELL_SIZE
        fruit_rectangle = pg.Rect(x, y,graphics.CELL_SIZE,graphics.CELL_SIZE)
        APPLE = pg.image.load('graphics/assets/images/apple.png').convert_alpha()
        APPLE = pg.transform.scale(APPLE, (graphics.CELL_SIZE, graphics.CELL_SIZE))
        screen.blit(APPLE, fruit_rectangle)
        # pg.draw.rect(screen,'red', fruit_rectangle)
    
    def randomize(self):
        self.x = random.randint(0, graphics.CELL_NUMBER - 1)
        self.y = random.randint(0, graphics.CELL_NUMBER - 1) 
        self.pos = pg.Vector2(self.x, self.y)


        