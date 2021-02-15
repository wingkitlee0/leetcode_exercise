from collections import defaultdict

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.counter = defaultdict(int) # key: count
        self.data = dict() # count: {key: value}
        
    def get(self, key: int) -> int:
        if key not in self.counter:
            return -1

        count = self.counter[key]
        value = self.data[count].pop(key)

        # clean up
        if len(self.data[count]) == 0:
            del self.data[count]

        if count+1 in self.data:
            self.data[count+1][key] = value
        else:
            self.data[count+1] = {key: value}
        # update counter
        self.counter[key] += 1
        return value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.counter:
            # no deletion
            count = self.counter[key] # current count
            self.counter[key] += 1

            # pop the old value from the data dict
            self.data[count].pop(key)
            # cleanup
            if len(self.data[count]) == 0:
                del self.data[count]
                
            # put the new value
            if count+1 not in self.data:
                self.data[count+1] = {key: value}
            else:
                self.data[count+1][key] = value

        else:
            if len(self.counter) == self.capacity:
                # counter reaches capacity, needs to delete something
                min_count = min(self.data.keys())
                print(f"min_count: {min_count}")

                # pop the least frequent and least recent key-value pair
                min_key, min_value = next(iter(self.data[min_count].items()))
                # cleanup
                del self.data[min_count][min_key]
                if len(self.data[min_count]) == 0:
                    del self.data[min_count]
                del self.counter[min_key]

            # add new data
            self.counter[key] = 1
            if 1 not in self.data:
                self.data[1] = {key: value}
            else:
                self.data[1][key] = value

    
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
