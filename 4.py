import utils

def findAllXmas(x: int, y: int, grid: list[str]) -> int:
    """Count how many times xmas appears starting from pos x,y in grid in 8 directions"""
    count = 0
    for xDir in [-1,0,1]:
        for yDir in [-1,0,1]:
            if xDir == 0 and yDir == 0:
                continue
            if findXmas(x,y,xDir,yDir,grid):
                count+=1
    return count

def findXmas(x: int, y: int, xDir: int, yDir: int, grid: list[str]) -> bool:
    """Takes a start position, direction (-1 to 1 for x and y and a grid). Returns whether xmas is present in that direction"""
    for i,c in enumerate(['X','M','A','S']):
        newY = y + yDir * i
        newX = x + xDir * i
        # first check if going out of bounds
        if newY >= len(grid) or newX >= len(grid[0]) or newY < 0 or newX < 0:
            return False
        # then check if the next letter is the next letter of xmas
        if grid[newY][newX] != c:
            return False
    return True

def checkCross(x: int, y: int, grid: list[str]) -> bool:
    # check if A is on edge, if so it can't be an X
    if x <= 0 or x >= len(grid[0])-1 or y <= 0 or y >= len(grid)-1:
        return False
    # check all the possible xmases
    posDiag = False  # looks like /
    negDiag = False  # looks like \
    if grid[y-1][x-1] == 'M' and grid[y+1][x+1] == 'S':
        negDiag = True
    elif grid[y-1][x-1] == 'S' and grid[y+1][x+1] == 'M':
        negDiag = True
    if grid[y+1][x-1] == 'M' and grid [y-1][x+1] == 'S':
        posDiag = True
    elif grid[y+1][x-1] == 'S' and grid [y-1][x+1] == 'M':
        posDiag = True
    return posDiag and negDiag

def solve(inv: str):
    grid = inv.splitlines()
    xmases1 = 0
    xmases2 = 0
    for y,line in enumerate(grid):
        for x,char in enumerate(line):
            if char == 'X':
                found = findAllXmas(x,y,grid)
                xmases1 += found
            if char == 'A':
                if checkCross(x,y,grid):
                    xmases2 += 1

    # 18, 9 in example
    return (xmases1, xmases2)

inExample = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""

with open('4.txt', 'r') as f:
    inPuzzle = f.read()

sol = solve(inPuzzle)
print(sol)
