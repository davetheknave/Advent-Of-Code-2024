import utils
from functools import reduce
from operator import add

inExample = """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
"""
inExample2 = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
"""

with open('3.txt', 'r') as f:
    inPuzzle = f.read()

def solve(inv):
    # Get mul operations, and capture each number, or don't and do operations
    matches = utils.regexAll(r"(?:mul\((\d{1,3}),(\d{1,3})\)|don't\(\)|do\(\))",inv)

    products1 = []
    products2 = []
    enabled = True
    for m in matches:
        if m[0] == "do()":
            enabled = True
        elif m[0] == "don't()":
            enabled = False
        else:
            # m[1] and m[2] are the first and second capture group, which must be numbers inside a valid mul() operation
            product = int(m[1]) * int(m[2])
            products1.append(product)
            if enabled:
                products2.append(product)

    sumOfProducts1 = reduce(add, products1)
    sumOfProducts2 = reduce(add, products2)
    return (sumOfProducts1, sumOfProducts2)

sol = solve(inPuzzle)
print(sol)