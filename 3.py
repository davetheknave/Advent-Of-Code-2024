import utils
from functools import reduce

inExample = """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
"""

with open('3.txt', 'r') as f:
    inPuzzle = f.read()

def solve(inv):
    matches = utils.regexAll(r"mul\((\d{1,3}),(\d{1,3})\)",inv)
    products = []
    for m in matches:
        products.append(int(m[1])*int(m[2]))
    sumOfProducts = reduce(lambda a,b: a + b, products)
    return (sumOfProducts, None)

sol = solve(inPuzzle)
print(sol)