import utils

def fix(update: list[int], rules: dict) -> list[int]:
    # this is similar to the code I used to check updates, but if an error is found, it removes all rule breaking pages, adds the next page, and then adds the rule breaking pages after. It iterates multiple times until it's correct, in case something is readded that breaks a different rule
    # this could run infinitely if there are any contradictory rules, such as 1|2 and 2|1 both being present.
    correct = False
    while not correct:
        newUpdate = []
        correct = True
        for page in update:
            if page in rules and not rules[page].isdisjoint(newUpdate):
                # found a page that comes after something it should come before
                correct = False
                ruleBreakers = rules[page].intersection(newUpdate)
                for i in ruleBreakers:
                    newUpdate.remove(i)
                newUpdate.append(page)
                newUpdate.extend(ruleBreakers)
            else:
                newUpdate.append(page)
        update = newUpdate  # we're going to check it again until it's correct
    return newUpdate

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
    # it it's found to be incorrect, fix it
    middles1 = []
    middles2 = []
    for update in input2:
        seen = set()
        correct = True
        for page in update:
            if page in rules and not seen.isdisjoint(rules[page]):
                correct = False
                fixedUpdate = fix(update, rules)
                middles2.append(fixedUpdate[int(len(update)/2)])
                break
            seen.add(page)
        if correct:
            middles1.append(update[int(len(update)/2)])

    sumOfMiddles1 = 0
    for m in middles1:
        sumOfMiddles1 += m
    sumOfMiddles2 = 0
    for m in middles2:
        sumOfMiddles2 += m

    return (sumOfMiddles1, sumOfMiddles2)

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