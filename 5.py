import utils

def solve(inv: str):
    # parse input
    input1 = []
    input2 = []
    readingFirst = True
    for l in inv.splitlines():
        if l == "":
            readingFirst = False
            continue
        if readingFirst:
            input1.append([int(x) for x in l.split("|")])
        else:
            input2.append([int(x) for x in l.split(",")])

    # first, let's get the rules and put them into a useful data structure
    # one before can have multiple afters
    # dict: key is BEFORE, value is set(AFTER). one before can have multiple afters
    rules = {}
    for r in input1:
        if r[0] not in rules:
            rules[r[0]] = set()
        rules[r[0]].add(r[1])
    
    # go through each update keeping track of what's been seen, and for each page, check if any rules say that a page that should come after has already been seen
    middles = []
    for update in input2:
        seen = set()
        correct = True
        for page in update:
            if page in rules and not seen.isdisjoint(rules[page]):
                correct = False
                break
            seen.add(page)
        if correct:
            middles.append(update[int(len(update)/2)])

    sumOfMiddles = 0
    for m in middles:
        sumOfMiddles += m

    return (sumOfMiddles, None)

inExample = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""

with open('5.txt', 'r') as f:
    inPuzzle = f.read()

sol = solve(inPuzzle)
print(sol)