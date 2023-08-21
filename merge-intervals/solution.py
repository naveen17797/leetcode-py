from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda i : i[0])
        output = [intervals[0]] # 1-5

        for start, end in intervals[1:]:
            last_end = output[-1][1]
            # 2 - 6
            if start <= last_end:
                output[-1][1] = max(last_end, end)
            else:
                output.append([start, end])

        return output



if __name__ == '__main__':
    s = Solution()
