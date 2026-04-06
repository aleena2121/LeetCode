class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        start = [0, 0]
        dirs = ["north", "east", "south", "west"]
        dir = dirs[0]

        obstacle_set = set(map(tuple, obstacles))

        max_dist = 0

        for i in commands:
            if i == -1:
                dir = dirs[(dirs.index(dir) + 1) % 4]
                continue
            elif i == -2:
                dir = dirs[(dirs.index(dir) - 1) % 4]
                continue
            else:
                while i != 0:
                    next_pos = start.copy()

                    if dir == "north":
                        next_pos[1] += 1
                    elif dir == "south":
                        next_pos[1] -= 1
                    elif dir == "east":
                        next_pos[0] += 1
                    elif dir == "west":
                        next_pos[0] -= 1

                    if tuple(next_pos) in obstacle_set:
                        break

                    start = next_pos
                    i -= 1

                    max_dist = max(max_dist, start[0]**2 + start[1]**2)

        return max_dist