from collections import defaultdict


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.counter = defaultdict(int)  # key: count
        self.data = dict()  # count: {key: value}

    def pop_data(self, count, key=None, left=False):
        """
        If left is True, pop the first entry in the dictionary (key is ignored)
        """
        value = self.data[count].pop(key)
        if len(self.data[count]) == 0:
            del self.data[count]
        return value

    def popleft_data(self, count):
        key, value = next(iter(self.data[count].items()))
        del self.data[count][key]
        return key, value

    def add_data(self, count, key, value):
        if count in self.data:
            self.data[count][key] = value
        else:
            self.data[count] = {key: value}

    def get(self, key: int) -> int:
        if key not in self.counter:
            return -1

        count = self.counter[key]
        value = self.pop_data(count, key)

        self.counter[key] += 1  # update counter
        self.add_data(count + 1, key, value)
        return value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.counter:
            # no deletion
            count = self.counter[key]  # current count
            self.counter[key] += 1

            _ = self.pop_data(count, key)  # pop the old value from the data dict
            self.add_data(count + 1, key, value)  # put the new value

        else:
            if len(self.counter) == self.capacity:
                # counter reaches capacity, needs to delete something
                min_count = min(self.data.keys())
                print(f"min_count: {min_count}")

                # pop the least frequent and least recent key-value pair
                min_key, min_value = self.popleft_data(min_count)
                del self.counter[min_key]

            # add new data
            self.counter[key] = 1
            self.add_data(1, key, value)


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


def example1():
    lfu = LFUCache(2)

    lfu.data = {}
    lfu.put(1, 1)
    print(lfu)


if __name__ == "__main__":
    example1()
