import sys

# Conways' Game of Life: Ke Deng
# Input sets the global variables width and height, which are width and height of the game board respectively.
# Coordinates start at 0,0 so if boardColumn and boardRow are 5, then the bottom right cell has coordinates 4,4.

width = 0
height = 0
numiter = 0

# When given a cell, find the neighbors of the cell. Since the grid wraps around, look for the left and right columns that are adjacent.
# Also look for the rows above and below. If they wrap, change it. Return the coordinates of the neighbors in a list.
def neighbors(cell):
    x, y = cell;
    neighborset = set()
    r = range(-1,2)
    for row in r:
        for col in r:
            x = x + row
            y = y + col

            # Account for edge cases because the grid wraps around
            if x + row < 0:
                x = width - 1
            if x + row >= width:
                x = 0
            if y + col < 0:
                y = height - 1
            if y + col >= height:
                y = 0

            neighborset.add((x,y))
    return neighborset


# For each iteration, update the gameboard. Look at each live cell, count its neighbors. If there are exactly 3 live neighbors, it stays alive.
# For each neighbor of a live cell, count its neighbors and if there are 3 neighboring live cells, it is alive too.
# Any cell that has fewer than or more than 3 live neighbors does not make it to the next gameBoard.
def update(gameBoard):
    newBoard = set()
    for cell in gameBoard:
        cellNeighbors = neighbors(cell)

        if len(cellNeighbors & gameBoard) == 2 or len(cellNeighbors & gameBoard) == 3: 
            newBoard.add(cell)

        for neighbor in cellNeighbors:
            if len(gameBoard & neighbors(neighbor)) == 3:
                newBoard.add(neighbor)

    return newBoard

# Print the board for each iteration. First have an empty gameboard, matrix, with 0's.
# For each live cell, put a 1 in that cell's spot. Lastly, print them all.
def printBoard(gameBoard):
    # Initialize matrix with dead cells
    matrix = [[0 for x in range(width)] for y in range(height)]
    
    for cell in gameBoard:
        x, y = cell
        matrix[x][y] = 1

    for i in range(0, height):
        for j in range(0, width):
            print(matrix[i][j], end='')
        print()

# Main function that takes in a txt file in the appropriate format, and prints out the board for each iteration.
def main(fname):
    with open(fname) as f:
        content = f.readlines()
    content = [x.strip() for x in content]

    # Set global variables
    numiter = int(content[0])
    global width
    width = int(content[1].split(' ')[0])
    global height
    height = int(content[1].split(' ')[1])
    gameBoard = set()

    # Parse and find which cells are live
    for i in range(0, height):
        row = list(map(int, content[i + 2].split(' ')))
        for j in range(0,width):
            if row[j] == 1:
                gameBoard.add((i,j))

    printBoard(gameBoard)
    print()

    # For the iterations, print out the updated board.
    for i in range(0, numiter):
        newBoard = update(gameBoard)
        printBoard(newBoard)
        gameBoard = newBoard
        print()
        
if __name__ == '__main__':
    main(sys.argv[1])