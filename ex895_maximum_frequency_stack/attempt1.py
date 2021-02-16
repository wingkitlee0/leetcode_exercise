"""
# 895 Maximum frequency stack
"""
from __future__ import annotations
from typing import Dict, Optional
import copy


class Node:
    """
    Doubly linked list
    """

    def __init__(self, count: int, key: int):
        self.count = count
        self.keys = {key: None}
        self.prev_node: Node = None
        self.next_node: Node = None

    @classmethod
    def remove_key(cls, node: Node, key: int) -> bool:
        """
        return true if the node removed
        """
        print(f"removing key {key} from count={node.count}")
        if node is None:
            return False
        if key not in node.keys:
            return False
        del node.keys[key]
        if len(node.keys) == 0:
            prev_node = node.prev_node
            next_node = node.next_node
            if prev_node:
                prev_node.next_node = next_node
            if next_node:
                next_node.prev_node = prev_node
            return True
        return False

    def __eq__(self, other: Node) -> bool:
        return (self.count == other.count) and (self.keys == other.keys)


class FreqStack:
    def __init__(self):
        self.d: Dict[int, Node] = {}  # key, Node
        self.head = None  # Node
        self.tail = None  # Node

    def push(self, x: int) -> None:
        print(f"push({x})")
        if len(self.d) == 0:
            node = Node(count=1, key=x)
            self.head = node
            self.tail = node
            self.d[x] = node
            # node.prev_node = self.head
            return

        if x in self.d:
            node = self.d[x]
            if x in node.keys:
                print(f"{x} in node.keys")
                if node.next_node is not None:
                    print(f"next node is not None")
                    if node.next_node.count == node.count + 1:
                        # when next node has the correct count
                        print(f"next node has the correct count ({node.count+1})")
                        next_node = node.next_node
                        next_node.keys[x] = None
                        node_removed = Node.remove_key(node=node, key=x)
                        if node_removed and node.count == 1:
                            self.head = next_node
                        self.d[x] = next_node
                        return
                    else:
                        new_node = Node(count=node.count + 1, key=x)
                        new_node.next_node = node.next_node
                        new_node.prev_node = node
                        node.next_node = new_node
                        Node.remove_key(node=node, key=x)
                        self.d[x] = new_node
                        # update tail
                        if self.tail.count < new_node.count:
                            print("update tail")
                            self.tail = new_node
                        return
                else:
                    print(f"next node is None")
                    if len(node.keys) == 1:  # only key
                        print(f"{x} is the only key")
                        node.count += 1
                    else:
                        new_node = Node(count=node.count + 1, key=x)
                        new_node.prev_node = node
                        node.next_node = new_node
                        Node.remove_key(node, key=x)
                        self.d[x] = new_node
                        self.tail = new_node

                return
            raise ValueError("x not in d[x].keys")
        else:
            if self.head.count == 1:
                self.head.keys[x] = None
                self.d[x] = self.head
            else:
                old_head = self.head
                node = Node(count=1, key=x)
                node.next_node = old_head
                old_head.prev_node = node
                self.head = node
                self.tail = old_head
                self.d[x] = node

            return

    def pop(self) -> int:
        x = next(iter(self.tail.keys))  # first element of the (ordered) dictionary
        print(f"pop() -> {x}")
        # x = self.tail.keys.popitem()

        tail_node = self.d[x]  # tail node (max frequency)

        # check if node is the head as well
        if tail_node.count > self.head.count:
            assert tail_node.prev_node
            print(f"tail node is not the head")
            if tail_node.prev_node.count == tail_node.count - 1:
                print(f"prev_node has the correct count")
                # move x to prev_node
                prev_node = tail_node.prev_node
                prev_node.keys[x] = None

                if len(tail_node.keys) == 1:
                    prev_node.next_node = None
                    self.tail = prev_node
                else:
                    del tail_node.keys[x]

                # update self.d[x]
                self.d[x] = prev_node
            else:
                # insert a node with node.count - 1
                new_node = Node(count=tail_node.count - 1, key=x)
                new_node.next_node = tail_node
                new_node.prev_node = tail_node.prev_node
                tail_node.prev_node = new_node
                tail_node.next_node = None
                Node.remove_key(tail_node, key=x)
                # update self.d[x]
                self.d[x] = new_node
        else:
            print(f"tail node is the head as well")
            # node is the head
            if len(tail_node.keys) == 1:
                # decrease node.count by 1
                tail_node.count -= 1
            else:
                # insert a node with node.count - 1
                new_node = Node(count=tail_node.count - 1, key=x)
                new_node.next_node = tail_node
                new_node.prev_node = tail_node.prev_node
                tail_node.prev_node = new_node
                tail_node.next_node = None
                self.head = new_node
                # update self.d[x]
                self.d[x] = new_node
        return x


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
