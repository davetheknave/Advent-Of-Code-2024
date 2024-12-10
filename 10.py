import utils
import time
import argparse
import os
from collections import defaultdict

class Pos:
    def __init__(self,x:int,y:int):
        self.x = x
        self.y = y
    def __key(self):
        return tuple(v for k,v in self.__dict__.items())

def Search(field, position, value, ends, count):
    x,y = position
    if field[y][x] == "9":
        ends.add((x,y))
        return (ends,count+1)
    counts = 0
    if y > 0 and field[y-1][x] == str(value+1):
        _,count1 = Search(field,(x,y-1),value+1,ends,count)
        counts += count1
    if y < (len(field)-1) and field[y+1][x] == str(value+1):
        _,count1 = Search(field,(x,y+1),value+1,ends,count)
        counts += count1
    if x > 0 and field[y][x-1] == str(value+1):
        _,count1 = Search(field,(x-1,y),value+1,ends,count)
        counts += count1
    if x < (len(field[0])-1) and field[y][x+1] == str(value+1):
        _,count1 = Search(field,(x+1,y),value+1,ends,count)
        counts += count1
    return (ends,counts)

def solve(inv: str):
    topoMap = inv.splitlines()
    height = len(topoMap)
    width = len(topoMap[0])

    trails = dict()
    for y,line in enumerate(topoMap):
        for x,char in enumerate(line):
            if char == '0':
                trails[(x,y)] = 1
    
    score = 0
    score2 = 0
    for k,v in trails.items():
        a,b = Search(topoMap,(k[0],k[1]),0,set(),0)
        print((k[0],k[1]),len(a),b)
        score += len(a)
        score2 += b

    print(trails)

    return (score, score2)

inExample2 = """\
0123
1234
8765
9876
"""
"""5, 6, 5, 3, 1, 3, 5, 3, 5"""
inExample = """\
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
"""

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", default="input/"+ os.path.basename(__file__).split('.')[0] +".txt", help="The file to run. If not specified, will look for a default file with the same name as this in input/")
parser.add_argument("-e","--example", action="store_true", help="Run the example instead of reading a file")
args = parser.parse_args()

if not args.example:
    with open(args.input, 'r') as f:
        inPuzzle = f.read()
else:
    inPuzzle = inExample
start = time.time()
sol = solve(inPuzzle)
end = time.time()
print(f"Finished in {end-start:.3f} seconds: ", sol)