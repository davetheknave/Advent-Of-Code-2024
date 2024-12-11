import utils
import time
import argparse
import os
import math
from collections import defaultdict

def digits(value):
    return math.floor(math.log10(value)+1)
def split(value,splitPoint):
    first = value//(10**splitPoint)
    second = value - (first*(10**splitPoint))
    return [first,second]
def blink(value):
    if value == 0:
        return [1]
    d = digits(value)
    if d % 2 == 0:
        return split(value,d//2)
    return [value * 2024]

def blink_many(stones,count):
    for i in range(count):
        for k,v in list(stones.items()):
            stones[k] -= v
            for i in blink(k):
                stones[i] += v
        for k in list(stones.keys()):
            if stones[k] == 0:
                del stones[k]
    return stones

def count_stones(stones):
    count = 0
    for s in stones.values():
        count += s
    return count

def solve(inv: str):
    inv = [int(x) for x in inv.split()]
    stones = defaultdict(int)
    for s in inv:
        stones[s] += 1
    
    blinks1 = blink_many(stones.copy(),25)
    blinks2 = blink_many(stones.copy(),75)
    
    return (count_stones(blinks1),count_stones(blinks2))

# inExample = """
# 0 1 10 99 999
# """
inExample = """
125 17
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