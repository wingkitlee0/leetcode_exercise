import copy
from attempt2 import LFUCache


def test_attempt1_0001():
    lfu = LFUCache(2)
    lfu.counter = {1: 1}
    lfu.data = {1: {1: 1}}

    assert lfu.get(1) == 1
    assert lfu.get(2) == -1
    assert lfu.counter == {1: 2}
    assert lfu.data == {2: {1: 1}}


def test_attempt1_0002():
    lfu = LFUCache(2)
    lfu.counter = {1: 1, 2: 1}
    lfu.data = {1: {1: 1, 2: 2}}

    assert lfu.get(1) == 1
    assert lfu.get(2) == 2
    assert lfu.counter == {1: 2, 2: 2}
    assert 1 not in lfu.data


def test_attempt1_put_0001():
    lfu = LFUCache(2)
    lfu.put(1, 3)

    assert lfu.counter == {1: 1}
    assert lfu.data == {1: {1: 3}}
    assert lfu.get(1) == 3


def test_attempt1_put_0002():
    lfu = LFUCache(2)
    lfu.put(1, 3)
    lfu.put(2, 4)

    assert lfu.counter == {1: 1, 2: 1}
    assert lfu.data == {1: {1: 3, 2: 4}}
    assert lfu.get(1) == 3
    assert lfu.get(2) == 4
    assert lfu.counter == {1: 2, 2: 2}
    assert 1 not in lfu.data


def test_attempt1_put_0003():
    lfu = LFUCache(2)
    lfu.put(1, 3)
    lfu.put(2, 4)
    lfu.put(1, 5)

    assert lfu.counter == {1: 2, 2: 1}
    assert lfu.data == {1: {2: 4}, 2: {1: 5}}
    assert lfu.get(1) == 5
    assert lfu.get(2) == 4
    assert lfu.counter == {1: 3, 2: 2}
    assert 1 not in lfu.data
    assert len(lfu.data[min(lfu.data.keys())]) > 0


def test_attempt1_put_0004():
    lfu = LFUCache(2)
    lfu.put(1, 3)
    lfu.put(2, 4)
    lfu.put(1, 5)
    lfu.put(3, 6)

    assert lfu.counter == {1: 2, 3: 1}
    assert lfu.data == {1: {3: 6}, 2: {1: 5}}
    assert lfu.get(1) == 5
    assert lfu.get(2) == -1
    assert lfu.get(3) == 6
    assert lfu.counter == {1: 3, 3: 2}
    assert 1 not in lfu.data
    assert len(lfu.data[min(lfu.data.keys())]) > 0


def test_attempt1_full_0001():
    lfu = LFUCache(2)
    lfu.put(1, 1)
    lfu.put(2, 2)
    assert lfu.get(1) == 1
    assert set(lfu.counter.keys()) == {1, 2}

    lfu.put(3, 3)
    assert set(lfu.counter.keys()) == {1, 3}

    assert lfu.get(2) == -1
    assert lfu.get(3) == 3
    assert lfu.counter == {1: 2, 3: 2}
    assert lfu.data == {2: {1: 1, 3: 3}}
    data_copy = copy.deepcopy(lfu.data)
    k, v = next(iter(data_copy[2].items()))
    assert (k, v) == (1, 1)

    lfu.put(4, 4)
    assert set(lfu.counter.keys()) == {3, 4}


def test_attempt1_full_0002():
    lfu = LFUCache(1)
    lfu.put(1, 1)
    lfu.put(1, 1)
    lfu.put(2, 2)

    assert lfu.get(1) == -1


def test_min_count_0001():
    lfu = LFUCache(2)
    lfu.put(1, 1)
    lfu.put(1, 2)

    assert lfu.min_count == 2
    lfu.put(2, 2)
    assert lfu.min_count == 1
