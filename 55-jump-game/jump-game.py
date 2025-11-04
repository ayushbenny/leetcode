class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0  # how far we can go

        for i in range(len(nums)):
            # if we reach a point we can’t get to, stop
            if i > farthest:
                return False

            # update how far we can reach from here
            farthest = max(farthest, i + nums[i])

        # if farthest reaches or passes the last index, we can reach the end
        return farthest >= len(nums) - 1