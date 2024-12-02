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

def solve(inv):
    # Turn input into a 2D list of ints
    reports = [[int(ll) for ll in l.split()] for l in inv.splitlines()]
    
    safeCount = 0
    for r in reports:
        safe = True
        inc = False
        dec = False
        prev = None
        for rr in r:
            if prev is not None:
                if rr == prev:
                    safe = False
                elif rr < prev:
                    if inc:
                        safe = False
                    dec = True
                elif rr > prev:
                    if dec:
                        safe = False
                    inc = True
                change = abs(prev - rr)
                if change > 3 or change < 1:
                    safe = False
            prev = rr
        if safe:
            safeCount += 1
    
    return (safeCount, None)

sol = solve(inPuzzle)
print(sol)
