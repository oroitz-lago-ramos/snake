import pygame as pg
import game
import graphics

class Snake:
    def __init__(self) -> None:
        self.body = [pg.Vector2(10,9)]
        self.direction = pg.Vector2(0,0)
        self.new_block = False
    def draw_snake(self):
        screen = graphics.get_screen()
        for body_part in self.body:
            x = int(body_part.x * graphics.CELL_SIZE)
            y = int(body_part.y * graphics.CELL_SIZE)
            body_rectangle = pg.Rect(x, y, graphics.CELL_SIZE, graphics.CELL_SIZE)
            pg.draw.rect(screen,'blue', body_rectangle)
    def move_snake(self):
        if self.direction != pg.Vector2(0,0):
            if self.new_block:
                body_copy = self.body[:]
                body_copy.insert(0, body_copy[0] + self.direction)
                self.body = body_copy[:]
                self.new_block = False
            else:
                if len(self.body) == 1:
                    body_copy = self.body
                    body_copy[0] += self.direction
                    self.body = body_copy[:]
                else:
                    body_copy = self.body[:-1]
                    body_copy.insert(0, body_copy[0] + self.direction)
                    self.body = body_copy[:]
    def add_block(self):
        self.new_block = True
    def get_score(self):
        return (len(self.body) - 1)