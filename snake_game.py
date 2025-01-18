import pygame as pg
import random
from enum import Enum
from collections import namedtuple

pg.init()
font = pg.font.SysFont('arial',25)

class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4

Point = namedtuple('Point','x, y')

WHITE = (255,255,255)
RED = (200,0,0)
BLUE1 = (0,255,0)
BLUE2 = (0,100,255)
BLACK = (0,0,0)


BLOCK_SIZE = 20
SPEED = 12

class SnakeGame():

    def load_images(self):
        self.snake_head = pg.image.load("SnakeHead2.png").convert_alpha()
        self.snake_head1 = pg.transform.scale(self.snake_head, (BLOCK_SIZE, BLOCK_SIZE))
        self.snake_head_rect = self.snake_head1.get_rect()
        return [self.snake_head1, self.snake_head_rect]

    def rotate_image(self):
        if self.direction == Direction.LEFT:
            self.snake_head1 = pg.transform.rotate(self.snake_head1,-90)
        if self.direction == Direction.RIGHT:
            self.snake_head1 = pg.transform.rotate(self.snake_head1,90)
        if self.direction == Direction.UP:
            self.snake_head1 = pg.transform.rotate(self.snake_head1, 180)


    def __init__(self, width = 640, height = 480):

        self.width = width
        self.height = height

        self.display = pg.display.set_mode((self.width, self.height))
        pg.display.set_caption("Snake")
        self.clock = pg.time.Clock()

        self.direction = Direction.RIGHT

        self.head = Point(self.width/2, self.height/2)

        self.snake = [self.head,
                      Point(self.head.x-BLOCK_SIZE, self.head.y),
                      Point(self.head.x-(2*BLOCK_SIZE), self.head.y)]
        self.score = 0
        self.food = None
        self._place_food()

    def _place_food(self):
        x = random.randint(0, (self.width-BLOCK_SIZE)//BLOCK_SIZE)*BLOCK_SIZE
        y = random.randint(0, (self.height-BLOCK_SIZE)//BLOCK_SIZE)*BLOCK_SIZE
        self.food = Point(x,y)
        if self.food in self.snake:
            self._place_food()

    def play_step(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT and self.direction != Direction.RIGHT:
                    self.direction = Direction.LEFT
                    print("Direction changed to LEFT")
                elif event.key == pg.K_RIGHT and self.direction != Direction.LEFT:
                    self.direction = Direction.RIGHT
                    print("Direction changed to RIGHT")
                elif event.key == pg.K_UP and self.direction != Direction.DOWN:
                    self.direction = Direction.UP
                    print("Direction changed to UP")
                elif event.key == pg.K_DOWN and self.direction != Direction.UP:
                    self.direction = Direction.DOWN
                    print("Direction changed to DOWN")

        self._move(self.direction)
        self.snake.insert(0, self.head)

        game_over = False
        if self._is_collision():
            game_over = True
            return game_over, self.score

        if self.head == self.food:
            self.score += 1
            self._place_food()
        else:
            self.snake.pop()

        self.update_ui()
        self.clock.tick(SPEED)

        return game_over, self.score

    def _is_collision(self):
        if self.head.x > self.width - BLOCK_SIZE or self.head.x < 0 or self.head.y > self.height-BLOCK_SIZE or self.head.y <0:
            return True
        if self.head in self.snake[1:]:
            return True
        
        return False

    def _move(self, direction):
        x = self.head.x
        y = self.head.y
        if direction == Direction.RIGHT:
            x += BLOCK_SIZE
        elif direction == Direction.LEFT:
            x-= BLOCK_SIZE
        elif direction == Direction.UP:
            y -= BLOCK_SIZE
        elif direction == Direction.DOWN:
            y += BLOCK_SIZE
        
        self.head = Point(x,y)

    
    def update_ui(self):
        self.display.fill(WHITE)
        images = self.load_images()
        
        for pt in self.snake:
            pg.draw.rect(self.display, BLUE1, pg.Rect(pt.x,pt.y, BLOCK_SIZE, BLOCK_SIZE))
            pg.draw.rect(self.display, BLUE1, pg.Rect(pt.x+4,pt.y+4, 12, 12)) # snake
        
        pg.draw.rect(self.display, RED, pg.Rect(self.food.x, self.food.y, BLOCK_SIZE, BLOCK_SIZE))

        text = font.render("Score: " + str(self.score), True, BLACK)
        self.display.blit(text, [0,0])
        self.rotate_image()
        self.display.blit(self.snake_head1, self.head)

        pg.display.flip()


if __name__ == '__main__':
    game = SnakeGame()

    while True:
        game_over, score = game.play_step()

        if game_over == True:
            break

    print('Final Score', score)

    pg.quit()