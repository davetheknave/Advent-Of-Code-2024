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
    for antLocs in antennas.values():  # antLoc: a list of one type of antenna
        for i,antenna1 in enumerate(antLocs):
            for antenna2 in antLocs[i+1:]:
                dx = antenna1[0] - antenna2[0]
                dy = antenna1[1] - antenna2[1]
                anti1 = (antenna1[0]+dx, antenna1[1]+dy)
                anti2 = (antenna2[0]-dx, antenna2[1]-dy)
                if 0 <= anti1[0] < width and 0<= anti1[1] < height:
                    antinodeLocations.add(anti1)
                if 0 <= anti2[0] < width and 0<= anti2[1] < height:
                    antinodeLocations.add(anti2)
    print(antinodeLocations)
    antinodeCount = len(antinodeLocations)
    return (antinodeCount, None)

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