import pygame, time, random
pygame.init()

#CHANGE THESE VALUES

#number of columns and rows on the plane - must be Int (Can be diff6erent!)
columns = 20
rows = 20

#x,y of each tile. If increasing tileSize, considerdecreasing the rows and columns variables above...
tileSize = 50

#Enter the desired fps of the display - note the higher the fps the faster each pattern will be completed
#This is the desired FPS, if the value is too high, the program will only run at the fastest it can
#If you wish to leave the fps uncapped, set the value to 0
fps = 0

#write in patterns here (can include any number of patterns, just add the variable to the list 'patterns' below)
#patterns can be any number of columns and rows, and can also be non-uniform (eg. 4 rows in column 1, then 7 rows in column 2)
pattern1 = [[1,0],[0,1]]
pattern2 = [[0, 0, 0, 0, 0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]]
pattern3 = [[1,1],[0,0]]
pattern4 = [[0,1,0],[0,0]]
pattern5 = [[1,0,1,0,1],[1,0,1,0,1]]
pattern6 = [[1,1,0,0],[0,0,1,1]]
pattern7 = [[1,0,0,0,1],[1,1,1,1,1,0],[0,1,0,1]]

patterns = [pattern1, pattern2, pattern3, pattern4, pattern5, pattern6, pattern7]
#patterns = [pattern2]

########################################
### DO NOT CHANGE ANY VARIABLES BELOW ##
########################################

display_width = columns * tileSize
display_height = rows * tileSize

#define pygame window characteristics, and clock (used for FPS)
Display = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Squares')
clock = pygame.time.Clock()

#load images and apply the correct transformations (scaling)
square = pygame.image.load('square.jpg')
square = pygame.transform.scale(square, (tileSize, tileSize))
square90 = pygame.image.load('square90.jpg')
square90 = pygame.transform.scale(square90, (tileSize, tileSize))
rotations = [square, square90]

'''
The below algorithm converts any inputted patern into a list compatible with the output plane size

Firstly it checks if the columns or rows are equal to the plane size, if not, the sequence is either duplicated or reduced
so that there are the correct number of columns in each list position. Then if needed the pattern is ammended to have the same 
number of rows (replicating itself based off of row 1 to the next entry, then row 2 and so on)
'''

for pattern in patterns:
    if len(pattern) == columns & len(pattern[0]) == rows:
        print('equal rows & columns')

    else:
        #columns check
        if len(pattern[0]) == rows:
            print("equal columns")

        elif len(pattern[0]) < rows:
            for item in pattern:
                index = 0
                while len(item) < rows:
                    item.append(item[index])
                    index +=1

                    if index >= len(item) - 1:
                        index = 0
        
        elif len(pattern[0]) > rows:
            for item in pattern:
                i = 0
                val = True
                while val == True:
                    if len(item) == rows:
                        val = False
                    else:
                        if i % 2 == 0:
                            item.pop()
                        else:
                            item.pop(0)
                        i +=1

        #row checks
        if len(pattern) == columns:
            print("equal rows")

        elif len(pattern) < columns:
            index = 0
            while len(pattern) < columns:
                pattern.append(pattern[index])
                index +=1

                if index >= len(pattern) - 1:
                    index = 0

        elif len(pattern) > columns:
            i = 0
            val = True
            while val == True:
                if len(pattern) == columns:
                        val = False
                else:
                    if i % 2 == 0:
                            pattern.pop()
                    else:
                            pattern.pop(0)
                    
                    i +=1

#Outputs the generated patterns to the console
print('Patterns:')
for item in patterns:
    print(item)
print(' ')

#create pos checker list for efficiency (instead of using random and checking the same tile more than once...)
global scannerMatrix
def generateScannerPos():
    global scannerMatrix
    scannerMatrix = []
    for x in range(columns):
        for y in range(rows):
            scannerMatrix.append([x,y])
    random.shuffle(scannerMatrix)

generateScannerPos()

#Randomly generates the plane on launch, all tiles are randomly orientated and then compared to begin generating the first pattern
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

def displayImages():
    for rowindex, row in enumerate(column):
            for imageindex, image in enumerate(row):
                    Display.blit(rotations[image], (rowindex*tileSize, imageindex*tileSize))

gameExit = False
currentPos = 0
currentPattern = 0
while not gameExit:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        gameExit = True

        selectedRow = scannerMatrix[currentPos][1]
        selectedColumn = scannerMatrix[currentPos][0]
        selectedSquare = column[selectedColumn][selectedRow]

        if selectedSquare == patterns[currentPattern][selectedColumn][selectedRow]:
                pass

        else:
                if selectedSquare == 0:
                        column[selectedColumn][selectedRow] = 1

                elif selectedSquare == 1:
                        column[selectedColumn][selectedRow] = 0

        displayImages()
        pygame.display.update()
        currentPos += 1

        if column == patterns[currentPattern]:
            print('Completed pattern')
            time.sleep(0.3)
            print('Moving to next pattern...')
            if currentPattern >= len(patterns)-1:
                currentPattern = 0
            else:
                currentPattern += 1
                
            generateScannerPos()
            currentPos = 0

        clock.tick(fps)

pygame.quit()
