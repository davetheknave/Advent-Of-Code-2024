import utils

class area:
    def __init__(self, inv: str):
        self.model = inv.splitlines()
        self.width = len(self.model[0])
        self.height = len(self.model)

    def in_bounds(self,x,y):
        return 0<=x<self.width and 0<=y<self.height
    
    def get(self, x:int, y:int) -> str:
        return self.model[y][x]
    
    def find_guard(self) -> ((int,int),str):
        found = False
        for y,line in enumerate(self.model):
            for x,c in enumerate(line):
                if c in directions.keys():
                    return ((x,y),c)

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
    
def solve(inv: str):
    a = area(inv)
    visited = set()
    position,direction = a.find_guard()

    # navigate
    while a.in_bounds(position[0],position[1]):
        visited.add(position)
        next = (position[0]+(directions[direction][0]), position[1]+directions[direction][1])
        # facing an obstacle
        if a.in_bounds(next[0],next[1]) and a.get(next[0],next[1]) == "#":
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