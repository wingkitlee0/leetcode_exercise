from typing import Any, Dict, DefaultDict, Optional, Tuple
from collections import defaultdict
from dataclasses import dataclass, field


@dataclass
class LFUCache:
    capacity: int
    counter: DefaultDict[int, int] = field(init=False, default_factory=defaultdict)
    data: Dict[int, Dict[int, Any]] = field(init=False, default_factory=dict)

    def pop_data(self, count: int, key=None) -> Any:
        """
        Pop data from the right
        """
        value = self.data[count].pop(key)
        if len(self.data[count]) == 0:
            del self.data[count]
        return value

    def popleft_data(self, count: int) -> Tuple[Optional[int], Optional[Any]]:
        """
        Pop data from the left
        """
        if count in self.data:
            key, value = next(iter(self.data[count].items()))
            del self.data[count][key]
            return key, value
        else:
            return None, None

    def _add_data(self, count: int, key: int, value: Any):
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
        self._add_data(count + 1, key, value)
        return value

    def put(self, key: int, value: Any) -> None:
        if self.capacity == 0:
            return
        if key in self.counter:
            # no deletion
            count = self.counter[key]  # current count
            self.counter[key] += 1

            _ = self.pop_data(count, key)  # pop the old value from the data dict
            self._add_data(count + 1, key, value)  # put the new value

        else:
            if len(self.counter) == self.capacity:
                # counter reaches capacity, needs to delete something
                min_count = min(self.data.keys())
                print(f"min_count: {min_count}")

                # pop the least frequent and least recent key-value pair
                min_key, _ = self.popleft_data(min_count)
                del self.counter[min_key]

            # add new data
            self.counter[key] = 1
            self._add_data(1, key, value)


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
