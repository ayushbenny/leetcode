class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        first_rank = "Gold Medal"
        second_rank = "Silver Medal"
        third_rank = "Bronze Medal"
        new_list = [None] * len(score)
        sorted_rank = sorted(score, reverse=True)

        for i in range(len(sorted_rank)):
            idx = score.index(sorted_rank[i])
            if i == 0:
                new_list[idx] = first_rank
            elif i == 1:
                new_list[idx] = second_rank
            elif i == 2:
                new_list[idx] = third_rank
            else:
                new_list[idx] = str(i+1)
        
        return new_list