class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        start =[0, 0]
        pos = [0, 0]
        facing = 'N'
        for i in instructions:
            if i == 'G':
                if facing == 'N':
                    pos[1] += 1
                elif facing == 'S':
                    pos[1] -= 1
                elif facing == 'E':
                    pos[0] += 1
                else:
                    pos[0] -= 1
            elif i == 'L':
                if facing == 'N':
                    facing = 'W'
                elif facing == 'W':
                    facing = 'S'
                elif facing == 'S':
                    facing = 'E'
                else:
                    facing = 'N'
            else:
                if facing == 'N':
                    facing = 'E'
                elif facing == 'E':
                    facing = 'S'
                elif facing == 'S':
                    facing = 'W'
                else:
                    facing = 'N'
        if start == pos or facing != 'N':
            return True
        else:
            return False

    # more concise solution
    def isRobotBounded2(self, instructions: str) -> bool:
        x, y, dx, dy = 0, 0, 0, 1
        for i in instructions:
            if i == 'G':
                x, y = x + dx, y + dy
            elif i == 'L':
                dx, dy = -dy, dx
            else:
                dx, dy = dy, -dx

        return (x, y) == (0, 0) or (dx, dy) != (0, 1)



if __name__ == '__main__':
    sol = Solution()
    print(sol.isRobotBounded("GGLLGG"))
    print(sol.isRobotBounded("GG"))
    print(sol.isRobotBounded("GL"))

    print(sol.isRobotBounded2("GGLLGG"))
    print(sol.isRobotBounded2("GG"))
    print(sol.isRobotBounded2("GL"))
