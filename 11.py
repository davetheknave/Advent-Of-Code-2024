import utils
import time
import argparse
import os

class Link:
    def __init__(self,marking):
        self.value = int(marking)
        self.next = None
    def change(self):
        # print(self.value,' ',end='')
        if self.value == 0:
            # print("0->1")
            self.value = 1
            return self.next
        strVal = str(self.value)
        if len(strVal) % 2 == 0:
            # print("split")
            self.value = int(strVal[0:len(strVal)//2])
            newLink = Link(int(strVal[len(strVal)//2:]))
            newLink.next = self.next
            self.next = newLink
            return self.next.next
        # print("2024")
        self.value *= 2024
        return self.next

class LinkedList:
    def __init__(self,start=None):
        self.start = start
        self.end = None
        if start is None:
            pass
        elif isinstance(start, list):
            self.start = None
            self.end = None
            for i in start:
                self.append(i)
        elif isinstance(start, Link):
            current = self.start
            while current.next is not None:
                current = current.next
            self.end = current
        else:
            self.start = Link(start)
            self.end = self.start

    def foreach(self,func):
        current = self.start
        while current is not None:
            func(current)
            current = current.next
    def append(self,value):
        newLink = Link(value)
        if self.end is None:
            self.start = newLink
            self.end = self.start
            return
        else:
            self.end.next = newLink
            self.end = newLink
    def blink(self):
        current = self.start
        while current is not None:
            current = current.change()
    def count(self):
        count = 0
        current = self.start
        while current is not None:
            count += 1
            current = current.next
        return count
    def print(self):
        def printLink(a):
            print(a.value,end='')
            print(', ',end='')
        self.foreach(printLink)
        print()
        

def solve(inv: str):
    blinks = 25  # 25 in input, 1 in example
    stones = inv.split()
    newStones = LinkedList(stones)
    # newStones.print()
    for _ in range(blinks):
        newStones.blink()
    # newStones.print()
    return (newStones.count(), None)

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