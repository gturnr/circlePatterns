import pygame, time, random

pygame.init()
black = (0,0,0)

columns = 4
rows = 4
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

#pattern = [[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1]]
pattern = [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]
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

gameExit = False

positionsx = [0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3]
positionsy = [0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3]
pos1 = 0
pos2 = 0

while not gameExit:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        gameExit = True

        try:
                selectedRow = positionsx[pos1]
                selectedColumn = positionsy[pos2]
        except:
                input()

        selectedSquare = column[selectedColumn][selectedRow]

        print(selectedSquare, pattern[selectedColumn][selectedRow])

        if selectedSquare == pattern[selectedColumn][selectedRow]:
                print("same")

        else:
                #print("invalid square")
                #print(selectedSquare)
                if selectedSquare == 0:
                        Display.blit(rotations[1], (selectedRow*100, selectedColumn*100))

                elif selectedSquare == 1:
                        Display.blit(rotations[0], (selectedRow*100, selectedColumn*100))

        pos1 += 1
        pos2 += 1


        pygame.display.update()
        clock.tick(20)

pygame.quit()
