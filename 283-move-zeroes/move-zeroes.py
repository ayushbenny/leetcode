class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_zero = 0

        for i in nums[:]:
            if i == 0:
                count_zero+=1
                nums.remove(i)
        for i in range(count_zero):
            nums.append(0)
        return nums
        