import utils

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

def findAll(x: int, y: int, grid: list[str]) -> int:
    """Count how many times xmas appears starting from pos x,y in grid in 8 directions"""
    count = 0
    for xDir in [-1,0,1]:
        for yDir in [-1,0,1]:
            if xDir == 0 and yDir == 0:
                continue
            xmas = find(x,y,xDir,yDir,grid)
            if xmas:
                count+=1
    return count

def find(x: int, y: int, xDir: int, yDir: int, grid: list[str]) -> bool:
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


def solve(inv: str):
    grid = inv.splitlines()
    christmasses = 0
    for y,line in enumerate(grid):
        for x,char in enumerate(line):
            if char == 'X':
                found = findAll(x,y,grid)
                if found > 0:
                    christmasses += found


    return (christmasses, None)

sol = solve(inPuzzle)
print(sol)
