import random


class RandomizedSet:

    def __init__(self):
        self.map = {}
        self.list = []

    def insert(self, val: int) -> bool:
        if val not in self.map:
            self.list.append(val)
            self.map[val] = len(self.list) - 1
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False
        else:
            val_1 = self.list[-1]
            index_1 = self.map[val_1]

            index_2 = self.map[val]
            val_2 = self.list[index_2]

            # swap value to be removed with last value
            self.list[index_2] = val_1
            self.list[index_1] = val_2
            # now that we swapped, remove the last item
            self.list.pop()
            # also update the swapped index.
            self.map[val_1] = index_2
            # also remove the entry from the map
            self.map.pop(val)

            return True


    def getRandom(self) -> int:
        return random.choice(self.list)


if __name__ == '__main__':
    s = RandomizedSet()
    s.remove(0)
    s.remove(0)
    s.insert(0)
    s.getRandom()
    s.remove(0)
    s.insert(0)
