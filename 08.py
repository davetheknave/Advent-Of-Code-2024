import utils
import time
import argparse
import os

def solve(inv: str):
    field = inv.splitlines()
    height = len(field)
    width = len(field[0])
    # Find all antennas and record their location
    antennas = {}
    for y,line in enumerate(field):
        for x,char in enumerate(line):
            if char != '.':
                if char in antennas:
                    antennas[char].append((x,y))
                else:
                    antennas[char] = [(x,y)]
    # Calculate all antinode positions
    antinodes1 = set()
    antinodes2 = set()
    for antLocs in antennas.values():  # antLoc: a list of one type of antenna
        for i,antenna1 in enumerate(antLocs):
            for antenna2 in antLocs[i+1:]:
                dx = antenna1[0] - antenna2[0]
                dy = antenna1[1] - antenna2[1]

                x,y = antenna1
                i = 0
                while 0 <= x < width and 0 <= y < height:
                    if i == 1:
                        antinodes1.add((x,y))
                    antinodes2.add((x,y))
                    x += dx
                    y += dy
                    i += 1

                x,y = antenna2
                i = 0
                while 0 <= x < width and 0 <= y < height:
                    if i == 1:
                        antinodes1.add((x,y))
                    antinodes2.add((x,y))
                    x -= dx
                    y -= dy
                    i += 1

    return (len(antinodes1), len(antinodes2))

inExample = """\
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
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