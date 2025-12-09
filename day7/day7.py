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

def follow_timeline(input: list[list[str]], i: int, j: int, memo: dict[tuple[int, int], int]) -> int:
    if (i == len(input) - 1):
        return 1
    elif ((i, j) in memo):
        return memo[(i, j)]
    elif (input[i][j] == "."):
        paths = follow_timeline(input, i + 1, j, memo)
        memo[(i, j)] = paths
        return paths
    elif (input[i][j] == "^"):
        paths = follow_timeline(input, i, j - 1, memo) + follow_timeline(input, i, j + 1, memo)
        memo[(i, j)] = paths
        return paths
    else:
        return 0

# Part 2 is just path counting, we do a DFS using the #follow_timeline method
# to count the total number of paths a tachyon can follow to the bottom
def quantum(input: list[list[str]]) -> int:
    start = input[0].index("S")
    return follow_timeline(input, 1, start, {})


with open(sys.argv[1], "r") as file:
    input = [list(line.strip()) for line in file]

    splits = count_splits(input)
    timelines = quantum(input)


    print()
    print(f"Part 1: {splits}")
    print(f"Part 2: {timelines}")

