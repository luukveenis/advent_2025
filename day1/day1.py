class Lock:
    def __init__(self):
        self.position: int = 50

    # Rotates the lock according to the given input
    # Returns a tuple with the number of rotations past 0 and the final position of the lock
    def rotate(self, op: str) -> tuple[int, int]:
        count = int(op[1:])
        adjustment = count if op[0] == "R" else -count

        rot, pos = divmod(self.position + adjustment, 100)
        rotations = abs(rot)

        # Edge cases:
        # - when position + adjustment is exactly a multiple of 100 we double count the last move
        # - when starting from 0 and turning left (negative), we need to ignore the first
        #   rotation because we don't "pass" 0
        if (adjustment > 0 and pos == 0) or (adjustment < 0 and self.position == 0):
            rotations -= 1

        self.position = pos

        return (rotations, self.position)


lock = Lock()

with open("input.txt", "r") as file:
    clicks = 0
    points = 0

    for line in file:
        rotations, position = lock.rotate(line.strip())

        clicks += rotations
        if position == 0:
            points += 1

    print(f"Part one: {points}")
    print(f"Part two: {points + clicks}")
