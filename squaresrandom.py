import pygame, time, random

pygame.init()
black = (0,0,0)

columns = 5
rows = 5
#define window size
display_width = columns * 100
display_height = rows * 100

#define pygame window characteristics
Display = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption('Squares')
clock = pygame.time.Clock()

square = pygame.image.load('square.jpg')
square = pygame.transform.scale(square, (100, 100))
square90 = pygame.image.load('square90.jpg')
square90 = pygame.transform.scale(square90, (100, 100))
rotations = [square, square90]


gameExit = False

while not gameExit:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        gameExit = True

        column = []
        j = 0
        while j < columns:
                row = []
                i = 0
                while i < rows:
                        squareChoice = random.randint(0,1)
                        row.append(squareChoice)
                        i += 1
                column.append(row)
                j += 1

        for rowindex, row in enumerate(column):
                for imageindex, image in enumerate(row):
                        Display.blit(rotations[image], (rowindex*100, imageindex*100))

        pygame.display.update()
        clock.tick(10)

pygame.quit()
