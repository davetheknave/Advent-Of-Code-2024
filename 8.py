import utils
import time
import argparse
import os

def solve(inv: str):
    field = inv.splitlines()
    antennas = {}
    height = len(field)
    width = len(field[0])
    # Find all antennas and track their location
    for y,line in enumerate(field):
        for x,char in enumerate(line):
            if char != '.':
                if char in antennas:
                    antennas[char].append((x,y))
                else:
                    antennas[char] = [(x,y)]
    # Calculate all antinode positions
    antinodeLocations = set()
    antinodeLocations2 = set()
    for antLocs in antennas.values():  # antLoc: a list of one type of antenna
        for i,antenna1 in enumerate(antLocs):
            for antenna2 in antLocs[i+1:]:
                dx = antenna1[0] - antenna2[0]
                dy = antenna1[1] - antenna2[1]
                set1 = set()
                set2 = set()
                x = antenna1[0]
                y = antenna1[1]
                i = 0
                while 0 <= x < width and 0 <= y < height:
                    if i == 1:
                        antinodeLocations.add((x,y))
                    set1.add((x,y))
                    x += dx
                    y += dy
                    i += 1
                x = antenna2[0]
                y = antenna2[1]
                i = 0
                while 0 <= x < width and 0 <= y < height:
                    if i == 1:
                        antinodeLocations.add((x,y))
                    set2.add((x,y))
                    x -= dx
                    y -= dy
                    i += 1
                antinodeLocations2 = antinodeLocations2.union(set1).union(set2)
    print(antinodeLocations)
    return (len(antinodeLocations), len(antinodeLocations2))

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