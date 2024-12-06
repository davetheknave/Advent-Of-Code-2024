import utils

directions = {
    "^":(0,-1),
    ">":(1,0),
    "<":(-1,0),
    "v":(0,1),
}

def rotate(char: str) -> str:
    match char:
        case "^": return ">"
        case ">": return "v"
        case "v": return "<"
        case "<": return "^"
        case _: return print("Error")

def in_bounds(x,y,width,height):
    return 0 <= x < width and 0 <= y < height
        
    
def solve(inv: str):
    area = inv.splitlines()
    width = len(area[0])
    height = len(area)
    visited = set()
    position = None
    direction = ""
    # Find the guard's starting position
    for y,line in enumerate(area):
        for x,c in enumerate(line):
            if c in ['^','>','<','v']:
                position = (x,y)
                direction = c
                break
        if len(visited) > 0:
            break
    # navigate
    while in_bounds(position[0],position[1],width,height):
        visited.add(position)
        next = (position[0]+(directions[direction][0]), position[1]+directions[direction][1])
        # facing an obstacle
        if in_bounds(next[0],next[1],width,height) and area[next[1]][next[0]] == "#":
            direction = rotate(direction)
        else:
            position = next
    return (len(visited), None)

inExample = """\
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""

with open('6.txt', 'r') as f:
    inPuzzle = f.read()

sol = solve(inExample)
print(sol)