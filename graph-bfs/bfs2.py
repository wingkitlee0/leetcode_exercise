from collections import deque
from typing import Dict, List


def bfs(adj: Dict[str, List[str]], start: str):
    """
    Simple
    """
    if adj is None:
        return
    if start not in adj:
        return

    queue = deque()
    queue.append(start)
    seen = set()

    result = []
    while queue:
        print("begin")
        print(f"current queue: {queue}")
        curr = queue.popleft()
        if curr in seen:
            print(f"visited node {curr} already. skipping")
        else:
            result.append(curr)

        seen.add(curr)
        if curr in adj:
            for node in adj[curr]:
                if node not in seen:
                    print(f"adding node {node} to the queue")
                    queue.append(node)
                else:
                    print(f"node {node} seen. do nothing")
    return result


def bfs_keep_level(adj: Dict[str, List[str]], start: str):
    if adj is None:
        return
    if start not in adj:
        return

    queue = deque()
    queue.append((start, 0))
    seen = set()

    result = []
    while queue:
        print("begin")
        print(f"current queue: {queue}")
        curr, level = queue.popleft()
        # curr, level = queue.pop()
        if curr in seen:
            print(f"visited node {curr} already. skipping")
        else:
            result.append((curr, level))

        seen.add(curr)
        if curr in adj:
            for node in adj[curr]:
                if node not in seen:
                    print(f"adding node {node} to the queue")
                    queue.append((node, level + 1))
                else:
                    print(f"node {node} seen. do nothing")
    return result


def main():

    adj = {
        "s": ["a", "x"],
        "a": ["z"],
        "x": ["s", "d", "c"],
        "d": ["x", "c", "f"],
        "c": ["x", "d", "f", "v"],
        "f": ["d", "c", "v"],
        "v": ["c", "f"],
        "z": ["a"],
    }

    for key in adj:
        print("-" * 80)

        result = bfs_keep_level(adj=adj, start=key)
        print(f"starting from {key}:")
        print(result)


if __name__ == "__main__":
    main()
