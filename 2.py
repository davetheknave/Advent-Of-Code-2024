import utils

inExample = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""

with open('2.txt', 'r') as f:
    inPuzzle = f.read()

def check_levels(report):
    increasing = False
    decreasing = False
    prev = None
    for r in report:
        if prev is not None:
            change = abs(prev - r)
            if change > 3 or change < 1:
                return False

            if r < prev:
                decreasing = True
                if increasing:
                    return False

            elif r > prev:
                increasing = True
                if decreasing:
                    return False
        prev = r

    return True

def solve(inv):
    # Turn input into a 2D list of ints
    reports = [[int(ll) for ll in l.split()] for l in inv.splitlines()]
    
    safeCount = safeCount2 = 0
    for r in reports:
        # check safety for first solution
        if check_levels(r):
            safeCount += 1
        
        # check safety for second solution
        for i,_ in enumerate(r):
            newList = r[:i] + r[i+1:]  # new list with element at i removed
            if check_levels(newList):
                safeCount2 += 1
                break
    
    return (safeCount, safeCount2)

sol = solve(inPuzzle)
print(sol)
