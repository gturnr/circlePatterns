import pygame, time, random
pygame.init()

#CHANGE VALUES - must be Int (Can be different!)
columns = 6
rows = 6

display_width = columns * 100
display_height = rows * 100

#define pygame window characteristics
Display = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption('Squares')
clock = pygame.time.Clock()

#load images and apply the correct transformations
square = pygame.image.load('square.jpg')
square = pygame.transform.scale(square, (100, 100))
square90 = pygame.image.load('square90.jpg')
square90 = pygame.transform.scale(square90, (100, 100))
rotations = [square, square90]

#write in patterns here (can include more than 4 patterns, just add it to the list 'patterns' below)
#patterns can be any number of columns and rows, and can also be non-uniform (eg. 4 rows in column 1, then 7 rows in column 2)

pattern1 = [[1,0],[0,1]]
pattern2 = [[0,1,0],[0,0]]
pattern3 = [[1,0,1,0,1],[1,0,1,0,1]]
pattern4 = [[1,1,0,0],[0,0,1,1]]
pattern5 = [[1,0,0,0,1],[1,1,1,1,1,0],[0,1,0,1]]

patterns = [pattern1, pattern2, pattern3, pattern4, pattern5]

'''
The below algorithm converts any inputted patern into a grid compatible with the output plane size

Firstly it checks if the columns or rows are equal to the plane size, if not, the sequence is duplicated 
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
                        item.pop()
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
                    pattern.pop()
                    i +=1

print('Patterns:')
for item in patterns:
    print(item)
print(' ')

#create pos checker for efficiency (instead of using random and checking the same tile more than once...)
global scannerMatrix
def generateScannerPos():
    global scannerMatrix
    scannerMatrix = []
    for x in range(columns):
        for y in range(rows):
            scannerMatrix.append([x,y])

    random.shuffle(scannerMatrix)

generateScannerPos()
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
                    Display.blit(rotations[image], (rowindex*100, imageindex*100))

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
        #print(selectedSquare, patterns[currentPattern][selectedColumn][selectedRow])
        if selectedSquare == patterns[currentPattern][selectedColumn][selectedRow]:
                pass
                #print("same")

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
            time.sleep(0.2)
            print('Moving to next pattern...')
            if currentPattern >= len(patterns)-1:
                currentPattern = 0
            else:
                currentPattern += 1
                
            generateScannerPos()
            currentPos = 0

        clock.tick(200)

pygame.quit()
