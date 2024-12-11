import utils
import time
import argparse
import os
import math
from collections import defaultdict

def digits(value)->int:
    return math.floor(math.log10(value)+1)

def blink_one(stone: int)->[int]:
    if stone == 0:
        return [1]
    d = digits(stone)
    if d % 2 == 0:
        first = stone//(10**(d//2))
        second = stone - (first*(10**(d//2)))
        return [first,second]
    return [stone * 2024]

def blink_all(stones: dict, count=1)->dict:
    for _ in range(count):
        for stone,count in list(stones.items()):
            stones[stone] -= count
            for newStone in blink_one(stone):
                stones[newStone] += count

        # This just saves time
        for stone,count in list(stones.items()):
            if count == 0:
                del stones[stone]
    return stones

def count_stones(stones: dict)->int:
    count = 0
    for s in stones.values():
        count += s
    return count

def solve(inv: str):
    stones = defaultdict(int)
    for s in [int(x) for x in inv.split()]:
        stones[s] += 1
    
    blinks1 = blink_all(stones.copy(),25)
    blinks2 = blink_all(stones.copy(),75)
    
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