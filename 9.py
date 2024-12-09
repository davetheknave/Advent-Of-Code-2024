import utils
import time
import argparse
import os

class Block:
    def __init__(self,length:int,id:int,free:bool):
        self.length = length
        self.id = id
        self.free = free
    def __str__(self) -> str:
        return ('.' if self.free else str(self.id % 10)) * self.length

class MetaDrive(type):
    def __iter__(self):
        for i in self.stuff:
            yield i

class Drive(metaclass=MetaDrive):
    def __init__(self):
        self.stuff = []
    def append(self,block: Block):
        self.stuff.append(block)
    def insert(self,index:int,block:Block):
        self.stuff.insert(index,block)
    def pop(self,index:int):
        self.stuff.pop(index)
    def __getitem__(self,item):
        return self.stuff[item]
    def __len__(self):
        return len(self.stuff)
    def size(self):
        size = 0
        for i in self.stuff:
            size += i.length
        return size
    def __str__(self) -> str:
        return ''.join([str(x) for x in self.stuff])
    def get_checksum(self):
        checksum = 0
        position = 0
        for b in self.stuff:
            if not b.free:
                for i in range(position,position+b.length):
                    checksum += i*b.id
            position = position+b.length
        return checksum

def solve(inv: str):
    drive = Drive()
    free = False
    for i,c in enumerate(inv):
        drive.append(Block(int(c),i//2 if not free else -1,free))
        free = not free
    if args.example:
        print(str(drive))

    # rearrange
    drive2 = Drive()
    index = 0
    reverseIndex = len(drive)-1
    remaining2 = drive[reverseIndex].length
    remaining = 0
    while index <= reverseIndex:
        # if the next block is not free, just put it there as is
        if index == reverseIndex and remaining2 > 0:
            toFill = remaining2
            drive2.append(Block(toFill,drive[index].id,drive[index].free))
            break
        if not drive[index].free:
            drive2.append(Block(drive[index].length,drive[index].id,False))
            index += 1
        # if it is free, fill it with stuff from the end
        else:
            remaining = drive[index].length
            while remaining > 0 and index <= reverseIndex:
                if drive[reverseIndex].free:
                    reverseIndex -= 1
                    remaining2 = drive[reverseIndex].length
                    continue
                toFill = min(remaining2,remaining)
                drive2.append(Block(toFill,drive[reverseIndex].id,False))
                remaining -= toFill
                remaining2 -= toFill
                if remaining2 <= 0:
                    reverseIndex -= 1
                    remaining2 = drive[reverseIndex].length
            index += 1
    # fill remainder of free space
    drive2.append(Block(drive.size()-drive2.size(),-1,True))

    # rearrange for part 2
    drive3 = Drive()
    for i in drive:
        drive3.append(i)

    index = 0
    reverseIndex = len(drive3)-1
    attempted = set()
    while reverseIndex > 0:
        file = drive3[reverseIndex]
        if file.id in attempted:
            reverseIndex -= 1
            continue
        if file.id == 2:
            print(2)
        if not file.free:
            attempted.add(file.id)
            for i,b in enumerate(drive3):
                if i >= reverseIndex:
                    break
                if not b.free:
                    continue
                if b.length >= file.length:
                    drive3.pop(i)
                    toFill = file.length
                    drive3.insert(i,Block(toFill,file.id,False))
                    drive3.pop(reverseIndex)
                    drive3.insert(reverseIndex,Block(file.length,-1,True))
                    if toFill < b.length:
                        drive3.insert(i+1,Block(b.length - toFill,-1,True))
                        reverseIndex += 1
                    break
        reverseIndex -= 1

    # if args.example:
    #     print(str(drive2))

    if args.example:
        print(str(drive3))
    
    return (drive2.get_checksum(), drive3.get_checksum())
inExample = """2333133121414131402"""

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