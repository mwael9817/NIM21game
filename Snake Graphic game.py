import pygame
import sys
import random
#بسم الله الرحمن الرحيم
pygame.font.init()

WIDTH = 500
HEIGHT = 500
FPS = 14
font_name = pygame.font.match_font('arial')
score = 0

window = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("Snake")

fps = pygame.time.Clock()

class Snake():

    def __init__(self):
        self.position = [100,50]
        self.body = [[100,50],[100,40],[100,30]]
        self.direction = "DOWN"
        self.changeDirectionTo = self.direction

    def changeDirTo(self,dir):
        if dir=="RIGHT" and not self.direction=="LEFT":
            self.direction = "RIGHT"
        if dir=="LEFT" and not self.direction=="RIGHT":
            self.direction = "LEFT"
        if dir=="UP" and not self.direction=="DOWN":
            self.direction = "UP"
        if dir=="DOWN" and not self.direction=="UP":
            self.direction = "DOWN"

    def move(self,foodPos):
        if self.direction == "RIGHT":
            self.position[0] += 10
        if self.direction == "LEFT":
            self.position[0] -= 10
        if self.direction == "UP":
            self.position[1] -= 10
        if self.direction == "DOWN":
            self.position[1] += 10
        self.body.insert(0,self.position[:])
        if self.position == foodPos:
            return 1
        else:
            self.body.pop()
            return 0

    def checkCollision(self):
        if self .position[0] > WIDTH-1 or self.position[0] < 0:
            return 1
        elif self.position[1] > HEIGHT-1 or self.position[1] < 0:
            return 1
        for part in self.body[1:]:
                if self.position == part:
                    return 1
        else:
            return 0
    def reset(self):
        self.position = [100,50]
        self.body = [[100,50],[100,40],[100,30]]
        self.direction = "DOWN"
        self.changeDirectionTo = self.direction

    def getBody(self):
        return self.body

class FoodSpawner():

    def __init__(self):
        self.position = [random.randrange(1,WIDTH/10)*10, random.randrange(1,HEIGHT/10)*10]
        self.isFoodOnScreen = True

    def spawnFood(self):
        if self.isFoodOnScreen == False:
            self.position = [random.randrange(1,50)*10, random.randrange(1,50)*10]
            self.isFoodOnScreen = True
        return self.position

    def setFoodOnScreen(self,b):
        self.isFoodOnScreen = b

snake =  Snake()
foodSpawner = FoodSpawner()

def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, (173, 0, 0))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver();
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.changeDirTo('RIGHT')
            if event.key == pygame.K_LEFT:
                snake.changeDirTo('LEFT')
            if event.key == pygame.K_UP:
                snake.changeDirTo('UP')
            if event.key == pygame.K_DOWN:
                snake.changeDirTo('DOWN')
    foodPos = foodSpawner.spawnFood()
    if(snake.move(foodPos)==1):
        score += 1
        foodSpawner.setFoodOnScreen(False)

    window.fill(pygame.Color(0, 0, 0))
    for pos in snake.getBody():
        pygame.draw.rect(window,pygame.Color(0,225,0),pygame.Rect(pos[0],pos[1],10,10))
    pygame.draw.rect(window,pygame.Color(225,0,0),pygame.Rect(foodPos[0],foodPos[1],10,10))
    if(snake.checkCollision()==1):
        gameOver()
        score = 0
    pygame.display.set_caption("Snake | Score: "+ str(score))
    pygame.display.flip()
    fps.tick(FPS)
