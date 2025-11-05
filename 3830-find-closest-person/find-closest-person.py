class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        same_position = 0
        first_pos = 1
        second_pos = 2
        a = x-z
        b = y-z
        if abs(a) == abs(b):
            return same_position
        elif abs(a) < abs(b):
            return first_pos
        else:
            return second_pos