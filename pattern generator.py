import pygame, time, random
pygame.init()

#CHANGE THESE VALUES
#number of columns and rows on the plane - must be Int (Can be different!)
columns = 10
rows = 10

#x,y of each tile. If increasing tileSize, considerdecreasing the rows and columns variables above...
tileSize = 100

#Enter the desired fps of the display - note the higher the fps the faster each pattern will be completed
#This is the desired FPS, if the value is too high, the program will only run at the fastest it can
#If you wish to leave the fps uncapped, set the value to 0
fps = 0

########################################
### DO NOT CHANGE ANY VARIABLES BELOW ##
########################################

display_width = columns * tileSize
display_height = rows * tileSize

#define pygame window characteristics, and clock (used for FPS)
Display = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Pattern Designer')
clock = pygame.time.Clock()

global lastPressed
lastPressed = time.time()

#load images and apply the correct transformations (scaling)
square = pygame.image.load('square.jpg')
square = pygame.transform.scale(square, (tileSize, tileSize))
square90 = pygame.image.load('square90.jpg')
square90 = pygame.transform.scale(square90, (tileSize, tileSize))
rotations = [square, square90]

#Randomly generates the plane on launch, all tiles are randomly orientated and then compared to begin generating the first pattern
column = []
j = 0
while j < columns:
        row = []
        i = 0
        while i < rows:
                squareChoice = 0 #random.randint(0,1)
                row.append(squareChoice)
                i += 1

        column.append(row)
        j += 1

print(column)
buttonIndex = []

def displayImages():
    for rowindex, row in enumerate(column):
            for imageindex, image in enumerate(row):
                    Display.blit(rotations[image], (rowindex*tileSize, imageindex*tileSize))
                    buttonIndex.append([rowindex*tileSize, imageindex*tileSize, image, rowindex, imageindex])

displayImages()
print(buttonIndex)

def button(x,y,ro, r, c):
    global lastPressed

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+tileSize > mouse[0] > x and y+tileSize > mouse[1] > y:

        if click[0] == 1:
            print('click')
            #currenttime = time.time()
            #timeSpace = currenttime - lastPressed
            #print(timeSpace)

            #if timeSpace > 0.1: 
            if ro == 0:
                column[r][c] = 1
            elif ro == 1:
                column[r][c] = 0

                #lastPressed = time.time()     

gameExit = False
currentPattern = 0
while not gameExit:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        gameExit = True

        for image in buttonIndex:
            button(image[0], image[1], image[2], image[3], image[4])

        displayImages()
        pygame.display.update()

        clock.tick(fps)

pygame.quit()
print("Copy and paste this pattern into a variable in 'squares Master.py': ")
print(" ")
print(column)