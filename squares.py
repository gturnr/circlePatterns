import pygame, time, random

pygame.init()
black = (0,0,0)

#minimum is 2,2!!!
columns = 10
rows = 10
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

#write in patterns here

pattern1 = [[1,1,1,1],[1,1,1,1]]
pattern2 = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
pattern3 = [[1,0,1,0,1,0,1,0,1,0],[1,0,1,0,1,0,1,0,1,0],[1,0,1,0,1,0,1,0,1,0],[1,0,1,0,1,0,1,0,1,0],[1,0,1,0,1,0,1,0,1,0],[1,0,1,0,1,0,1,0,1,0],[1,0,1,0,1,0,1,0,1,0],[1,0,1,0,1,0,1,0,1,0],[1,0,1,0,1,0,1,0,1,0],[1,0,1,0,1,0,1,0,1,0]]
pattern4 = [[0,0,1,1,0,0,1,1,0,0],[1,1,0,0,1,1,0,0,1,1],[0,0,1,1,0,0,1,1,0,0],[1,1,0,0,1,1,0,0,1,1],[0,0,1,1,0,0,1,1,0,0],[1,1,0,0,1,1,0,0,1,1],[0,0,1,1,0,0,1,1,0,0],[1,1,0,0,1,1,0,0,1,1],[0,0,1,1,0,0,1,1,0,0],[1,1,0,0,1,1,0,0,1,1]]
#pattern1 = [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]

patterns = [pattern1, pattern2, pattern3, pattern4]

#replicating pattern algorithm
for pattern in patterns:

    if len(pattern) == columns & len(pattern[0] == rows):
        pass
    else:
        

        if len(pattern) == columns:
            print("equal columms")
        elif len(pattern) < columns:
            index = 0
            while len(pattern) < columns:
                
                pattern.append(pattern[index])

                index +=1

                if index >= len(pattern) - 1:
                    index = 0

        elif len(pattern > columns:
            pattern.pop(len(pattern) - columns)



print(len(patterns))

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

        print(selectedSquare, patterns[currentPattern][selectedColumn][selectedRow])

        if selectedSquare == patterns[currentPattern][selectedColumn][selectedRow]:
                print("same")

        else:
                if selectedSquare == 0:
                        column[selectedColumn][selectedRow] = 1

                elif selectedSquare == 1:
                        column[selectedColumn][selectedRow] = 0

        displayImages()
        pygame.display.update()

        currentPos += 1

        if column == patterns[currentPattern]:

            time.sleep(1)

            if currentPattern >= len(patterns) -1:
                currentPattern = 0
            else:
                currentPattern += 1
                
            generateScannerPos()
            currentPos = 0



        clock.tick(20)

pygame.quit()
