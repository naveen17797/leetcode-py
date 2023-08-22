import heapq


class MedianFinder:

    def __init__(self):
        self.large = []
        self.small = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)
        # now that we added the element to heap we need to compare
        # when the both heap have elements and transfer elements
        # to make sure we have two parts of array lying in two heaps


        if self.small and self.large and -1 * self.small[0] > self.large[0]:
            heapq.heappush(self.large, -1 * heapq.heappop(self.small))

        # check for uneven size
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -1 * heapq.heappop(self.small))

        if len(self.large) > len(self.small) + 1:
            heapq.heappush(self.small, -1 * heapq.heappop(self.large))


    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]

        return ((-1 * self.small[0]) + self.large[0]) / 2


if __name__ == '__main__':
    s = Solution()
