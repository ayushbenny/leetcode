class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        new_list = []
        for i in range(numRows):
            if i ==0:
                new_list.append([1])
            else:
                prev = new_list[-1]
                print(prev)
                row = [1]
                for j in range(1, len(prev)):
                    row.append(prev[j-1]+prev[j])
                row.append(1)
                new_list.append(row)
        return new_list