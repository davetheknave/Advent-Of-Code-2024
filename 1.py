import utils

inExample = """3   4
4   3
2   5
1   3
3   9
3   3
"""

with open('1.txt', 'r') as f:
    inPuzzle = f.read()

def solve(inv: str):
    # turn the input into two sorted lists of integers
    lines = inv.splitlines()
    list1 = []
    list2 = []
    for l in lines:
        matches = utils.regex(r"(\d+)\s+(\d+)", l)
        list1.append(matches[0])
        list2.append(matches[1])
    list1.sort()
    list2.sort()
    list1 = [int(n) for n in list1]
    list2 = [int(n) for n in list2]

    distance = 0
    for i in range(len(list1)):
        distance += abs(list1[i] - list2[i])
    
    similarity = 0
    frequency = {}
    for n in list2:
        if n in frequency:
            frequency[n] += 1
        else:
            frequency[n] = 1
    for n in list1:
        similarity += n * frequency.get(n,0)

    return (distance,similarity)

sol = solve(inPuzzle)
print(sol)