import sys

# Conways' Game of Life: Ke Deng
# Input sets the global variables width and height, which are width and height of the game board respectively.
# Coordinates start at 0,0 so if width and height are 5, then the bottom right cell has coordinates 4,4.

# When given a cell, find the neighbors of the cell. Since the grid wraps around, look for the left and right columns that are adjacent.
# Also look for the rows above and below. If they wrap, change it. Return the coordinates of the neighbors in a list.
def neighbors(cell):
    r, c = cell;
    neighborset = set()
    neighbordist = range(-1,2)
    i = 0
    for rdiff in neighbordist:
        for cdiff in neighbordist:
            if not (rdiff == cdiff and cdiff == 0):
                newr = r + rdiff
                newc = c + cdiff
            
                # Account for edge cases because the grid wraps around
                if newr < 0:
                    newr = numrows - 1
                elif newr>= numrows:
                    newr = 0
                if newc < 0:
                    newc = numcols - 1
                if newc >= numcols:
                    newc = 0

                neighborset.add((newr,newc))
                i = i + 1
    return neighborset


# For each iteration, update the gameboard. Look at each live cell, count its neighbors. If there are exactly 2 or 3 live neighbors, it stays alive.
# For each neighbor of a live cell, count its neighbors and if there are 3 neighboring live cells, it is alive too.
# Any cell that has fewer than 2 or more than 3 live neighbors does not make it to the next gameBoard.
def update(gameBoard):
    newBoard = set()
    for cell in gameBoard:
        cellNeighbors = neighbors(cell)
        

        if (len(cellNeighbors & gameBoard) == 2 or len(cellNeighbors & gameBoard) == 3) and cell not in newBoard:
            newBoard.add(cell)

        for neighbor in cellNeighbors:
            if (len(gameBoard & neighbors(neighbor)) == 3) and neighbor not in newBoard:
                newBoard.add(neighbor)

    return newBoard

# Print the board for each iteration. First have an empty gameboard, matrix, with 0's.
# For each live cell, put a 1 in that cell's spot. Lastly, print them all.
def printBoard(gameBoard):
    # Initialize matrix with dead cells
    matrix = [[0 for c in range(numcols)] for r in range(numrows)]
    
    for cell in gameBoard:
        r, c = cell
        matrix[r][c] = 1

    for i in range(0, numrows):
        for j in range(0, numcols):
            print(matrix[i][j], end='')
        print()

# Main function that takes in a txt file in the appropriate format, and prints out the board for each iteration.
def main(fname):
    with open(fname) as f:
        content = f.readlines()
    content = [x.strip() for x in content]

    # Set global variables
    numiter = int(content[0])
    global numcols
    numcols = int(content[1].split(' ')[0])
    global numrows
    numrows = int(content[1].split(' ')[1])
    # Done setting globals

    # Initalize the board
    gameBoard = set()

    # Populate the board with cells living at time 0
    for i in range(0, numrows):
        row = list(map(int, content[i + 2].split(' ')))
        for j in range(0,numcols):
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
