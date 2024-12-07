import utils
import time
import argparse
import os
from operator import add,mul
from functools import reduce

firstOperators = [add,mul]
secondOperators = [add,mul,lambda a,b: int(str(a)+str(b))]

def search(goal, operands, result, operators: list, operatorPool: list) -> list:
    if len(operands) <= 0 or result > goal:
        if result == goal:
            return operators
        else:
            return None
    foundCorrect = None
    for fo in operatorPool:
        nextOperators = operators.copy()
        nextOperators.append(fo)
        nextSearch = search(goal, operands[1:], fo(result,operands[0]),nextOperators, operatorPool)
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

    validResults1 = []
    validResults2 = []
    results1 = []
    results2 = []
    for l in lines:
        result = search(l[0], l[1], 0, [], firstOperators)
        result2 = search(l[0], l[1], 0, [], secondOperators)
        if result is not None:
            validResults1.append(l[0])
        if result2 is not None:
            validResults2.append(l[0])
        results1.append((l[0],result[1:] if result is not None and len(result) > 1 else None))
        results2.append((l[0],result2[1:] if result2 is not None and len(result2) > 1 else None))
            
    # for i in results:
    #     print(i)
    total = reduce(add, validResults1) if validResults1 else 0
    total2 = reduce(add, validResults2) if validResults2 else 0
    return (total, total2)

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