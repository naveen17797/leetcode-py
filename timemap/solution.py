from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.timestamp_prev = None
        self.data = defaultdict(lambda: [])

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((timestamp, value))


    def get(self, key: str, timestamp: int) -> str:
        values = self.data[key]
        res = None
        start, end = 0, len(values)-1
        while start <= end:
            mid = start + ((end-start) // 2)
            if values[mid][0] <= timestamp:
                res =  values[mid][1]
                start = mid + 1
            else:
                end = mid - 1
        return res if res is not None else ""
