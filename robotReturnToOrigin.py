# There is a robot starting at position (0, 0), the origin, on a 2D plane. Given a sequence of its moves, judge if this robot ends up at (0, 0) after it completes its moves.
#
# The move sequence is represented by a string, and the character moves[i] represents its ith move. Valid moves are R (right), L (left), U (up), and D (down). If the robot returns to the origin after it finishes all of its moves, return true. Otherwise, return false.
#
# Note: The way that the robot is "facing" is irrelevant. "R" will always make the robot move to the right once, "L" will always make it move left, etc. Also, assume that the magnitude of the robot's movement is the same for each move.

class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        if not moves:
            return True
        i = 0
        j = 0
        for move in moves:
            if move == 'R':
                i += 1
            elif move == 'L':
                i -= 1
            elif move == 'U':
                j += 1
            elif move == 'D':
                j -= 1
            else:
                return 'Invalid Move'

        if i == 0 and j == 0:
            return True
        else:
            return False


print(Solution().judgeCircle('R'))
print(Solution().judgeCircle('UD'))
print(Solution().judgeCircle('LR'))
print(Solution().judgeCircle('RL'))
print(Solution().judgeCircle('RULD'))
print(Solution().judgeCircle('RRDD'))





