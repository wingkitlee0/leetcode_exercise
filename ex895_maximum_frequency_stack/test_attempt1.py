from attempt1 import Node, FreqStack


def test_push_0001():

    freqstack = FreqStack()

    freqstack.push(7)

    assert freqstack.head.count == 1
    assert freqstack.d[7] == Node(count=1, key=7)

    freqstack.push(5)
    assert freqstack.head.count == 1
    assert set(freqstack.head.keys.keys()) == {5, 7}

    freqstack.push(7)
    assert freqstack.head == Node(count=1, key=5)
    assert freqstack.head.next_node == Node(count=2, key=7)
    assert freqstack.tail == Node(count=2, key=7)

    freqstack.push(5)
    assert freqstack.head.count == 2
    assert set(freqstack.head.keys.keys()) == {5, 7}
    assert freqstack.tail.count == 2
    assert set(freqstack.tail.keys.keys()) == {5, 7}

    freqstack.push(6)
    assert freqstack.head == Node(count=1, key=6)
    assert freqstack.tail.count == 2
    assert set(freqstack.tail.keys.keys()) == {5, 7}
    assert len(freqstack.d) == 3

    freqstack.push(7)
    assert freqstack.tail == Node(count=3, key=7)
    assert freqstack.tail.prev_node == Node(count=2, key=5)
    assert freqstack.head == Node(count=1, key=6)

    value = freqstack.pop()
    assert value == 7
    assert freqstack.tail.count == 2
    assert set(freqstack.tail.keys.keys()) == {5, 7}
    assert freqstack.tail.prev_node == Node(count=1, key=6)
    assert len(freqstack.d) == 3

    value = freqstack.pop()
    assert value == 5
    assert freqstack.tail.count == 2
    assert set(freqstack.tail.keys.keys()) == {
        7,
    }

def test_0002():
    """
    ["FreqStack","push","push","push","push","push","push","pop","push","pop","push","pop","push","pop","push","pop","pop","pop","pop","pop","pop"]
[[],[4],[0],[9],[3],[4],[2],[],[6],[],[1],[],[1],[],[4],[],[],[],[],[],[]]
    """
    freqstack = FreqStack()
    freqstack.push(4)
    freqstack.push(0)
    freqstack.push(9)
    freqstack.push(3)
    freqstack.push(4)
    freqstack.push(2)

    assert freqstack.tail.count == 2

    value = freqstack.pop()
    assert value == 4
    assert freqstack.tail.count == 1

    freqstack.push(6)
    assert freqstack.tail.count == 1

    value = freqstack.pop()
    assert value == 6