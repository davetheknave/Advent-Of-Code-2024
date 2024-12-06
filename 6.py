import utils
import time

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
        case _: raise Exception("Direction must be one of: ^,>,<,v")
    
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
        for y,line in enumerate(self.model):
            for x,c in enumerate(line):
                if c in directions.keys():
                    return ((x,y),c)
    
    def get_in_front(self, position: (int,int), direction: chr) -> (int,int):
        newPosition = (position[0]+directions[direction][0], position[1]+directions[direction][1])
        if self.in_bounds(newPosition[0], newPosition[1]):
            return newPosition
        else:
            return None
                
def solve(a: area, obstruct: (int,int) = None) -> (int|None,int):
    """Returns: None if a loop is found. Otherwise: the number of spaces that will be navigated, and the number of loops created with obstructions. It only creates obstructions if an obstruction has not been passed to it"""
    visited = set()  # (int,int)  used to see where the guard has been
    history = set()  # ((int,int),chr)  used to detect loops
    loops = set()  # (int,int)
    position,direction = a.find_guard()
    
    while position is not None:
        if (position,direction) in history:
            # Loop found
            return None
        visited.add(position)
        history.add((position,direction))
        next = a.get_in_front(position,direction)
        if obstruct is None and next is not None:
            canLoop = solve(a,next) is None  # This isn't a recursive algorithm
            if canLoop:
                loops.add(next)
        # Facing an obstacle
        if next is not None and (a.get(next[0],next[1]) == "#" or (next[0],next[1]) == obstruct):
            direction = rotate(direction)
        else:
            position = next
    return len(visited),len(loops)
                
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

start = time.time()
sol = solve(area(inPuzzle))
end = time.time()
print(f"Finished in {end-start:.3f} seconds: ", sol)