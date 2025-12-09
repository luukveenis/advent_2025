import sys
import copy

input =  []

def count_splits(input: list[list[str]]) -> int:
    splits = 0
    beams = copy.deepcopy(input)

    for i in range(1, len(beams)):
        for j in range(len(beams[i])):
            if (beams[i - 1][j] == "S"):
                beams[i][j] = "|"
            elif (beams[i][j] == "^" and beams[i - 1][j] == "|"):
                splits += 1
                beams[i][j - 1] = "|"
                beams[i][j + 1] = "|"
            elif (beams[i][j] == "." and beams[i - 1][j] == "|"):
                beams[i][j] = "|"

    return splits






with open(sys.argv[1], "r") as file:
    input = [list(line.strip()) for line in file]

    splits = count_splits(input)


    print()
    print(f"Part 1: {splits}")

