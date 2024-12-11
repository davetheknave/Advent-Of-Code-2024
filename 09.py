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
    def replace(self,index:int,block:Block):
        self.stuff[index] = block
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
    drive0 = Drive()
    free = False
    for lIndex,c in enumerate(inv):
        drive0.append(Block(int(c),lIndex//2 if not free else -1,free))
        free = not free

    # rearrange for part 1
    drive1 = Drive()
    lIndex = 0
    rIndex = len(drive0)-1
    nextFillSize = drive0[rIndex].length
    while lIndex <= rIndex:
        # Sometimes needed at the end if the last thing to move can only be partly moved
        if lIndex == rIndex:
            drive1.append(Block(nextFillSize,drive0[lIndex].id,drive0[lIndex].free))
            break

        # if the next block is a file, just put it there as is
        if not drive0[lIndex].free:
            drive1.append(Block(drive0[lIndex].length,drive0[lIndex].id,False))
            lIndex += 1
        # if it is free, fill it with stuff from the end
        else:
            dataToMove = drive0[rIndex]
            remaining = drive0[lIndex].length
            while remaining > 0 and lIndex <= rIndex:
                if dataToMove.free:
                    rIndex -= 1
                    nextFillSize = dataToMove.length
                    continue
                toFill = min(nextFillSize,remaining)
                drive1.append(Block(toFill,dataToMove.id,False))
                remaining -= toFill
                nextFillSize -= toFill
                if nextFillSize <= 0:
                    rIndex -= 1
                    nextFillSize = dataToMove.length
            lIndex += 1
    # fill remainder of free space
    drive1.append(Block(drive0.size()-drive1.size(),-1,True))

    # rearrange for part 2
    drive2 = Drive()
    drive2.stuff = drive0[:]
    rIndex = len(drive2)-1
    while rIndex > 0:
        file = drive2[rIndex]
        if not file.free:
            for lIndex in range(len(drive2)):
                space = drive2.stuff[lIndex]
                if lIndex >= rIndex:
                    break
                if not space.free:
                    continue
                if space.length >= file.length:
                    # replace destination with file
                    toFill = file.length
                    drive2.replace(lIndex,Block(toFill,file.id,False))
                    if toFill < space.length:
                        drive2.insert(lIndex+1,Block(space.length - toFill,-1,True))
                        rIndex += 1
                    # replace source with free space
                    drive2.replace(rIndex,Block(file.length,-1,True))
                    break
        rIndex -= 1

    return (drive1.get_checksum(), drive2.get_checksum())

inExample = """12345"""
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