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
    
class area:
    def __init__(self, inv: str):
        if type(inv) == str:
            inv = inv.splitlines()
        self.model = inv
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

def get_front(a: area, position: (int,int), direction: chr) -> (int,int):
    newPosition = (position[0]+directions[direction][0], position[1]+directions[direction][1])
    if a.in_bounds(newPosition[0], newPosition[1]):
        return newPosition
    else:
        return None
                
def navigate(a: area, obstruct: (int,int)) -> (int|None,int):
    """Will return the number of spaces that will be navigated or None if a loop is found"""
    visited = set()  # (int,int)  used to see where the guard has been
    history = set()  # ((int,int),chr)  used to detect loops
    position,direction = a.find_guard()
    loops = set()  # sometimes the same loop can be detected twice
    
    while position is not None:
        if (position,direction) in history:
            # Loop found
            return None
        visited.add(position)
        history.add((position,direction))
        next = get_front(a,position,direction)
        if obstruct is None and next is not None:
            canLoop = navigate(area(a.model),next) is None
            if canLoop:
                loops.add(next)
        # Facing and obstacle
        if next is not None and (a.get(next[0],next[1]) == "#" or (next[0],next[1]) == obstruct):
            direction = rotate(direction)
        else:
            position = next
    return len(visited),len(loops)
                
def solve(inv: str):
    a = area(inv)
    sol = navigate(a,None)

    # loops at 7,9,
    # 41/4939, 6/?
    return (sol[0], sol[1])

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

sol = solve(inPuzzle)
print(sol)