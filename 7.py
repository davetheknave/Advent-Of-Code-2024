import utils
import time
import argparse
import os
from operator import add,mul
from functools import reduce

firstOperators = [add,mul]

def search(goal, operands, result, operators: list) -> list:
    if len(operands) <= 0:
        if result == goal:
            return operators
        else:
            return None
    foundCorrect = None
    for fo in firstOperators:
        nextOperators = operators.copy()
        nextOperators.append(fo)
        nextSearch = search(goal, operands[1:], fo(result,operands[0]),nextOperators)
        if nextSearch is not None:
            foundCorrect = nextSearch
    if foundCorrect is not None:
        return foundCorrect
    else:
        return None

def solve(inv: str):
    # convert input into format: [(result, [operands])]
    lines = [x.split(':') for x in inPuzzle.splitlines()]
    lines = list(map(lambda a: (int(a[0]),[int(x) for x in a[1].split()]), lines))

    validResults = []
    results = []
    for l in lines:
        result = search(l[0], l[1], 0, [])
        if result is not None:
            validResults.append(l[0])
        results.append((l[0],result[1:] if result is not None and len(result) > 1 else None))
            
    # for i in results:
    #     print(i)
    total = reduce(add, validResults) if validResults else 0
    return (total, None)

inExample = """\
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
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