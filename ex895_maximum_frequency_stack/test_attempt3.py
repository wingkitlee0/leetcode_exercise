from collections import deque
from attempt3 import FreqStack

def test_push_v3_0001():

    stack = FreqStack()
    for x in [5, 7, 5, 7, 4, 5]:
        stack.push(x)

    assert stack.counter == {5:3, 4:1, 7:2}
    assert stack.data[1] == deque([5, 7, 4])
    assert stack.data[2] == deque([5, 7])
    assert stack.data[3] == deque([5])

def test_push_v3_0002():

    stack = FreqStack()
    for x in [5, 7, 5, 7, 4, 5]:
        stack.push(x)

    assert stack.counter == {5:3, 4:1, 7:2}
    assert stack.data[1] == deque([5, 7, 4])
    assert stack.data[2] == deque([5, 7])
    assert stack.data[3] == deque([5])
    # assert stack.max_count == 3
    assert len(stack.data) == 3

    assert stack.pop() == 5
    # assert stack.max_count == 2
    assert len(stack.data) == 2

    assert stack.pop() == 7
    assert len(stack.data) == 2
    # assert stack.max_count == 2

    assert stack.pop() == 5
    assert len(stack.data) == 1
    
    assert stack.pop() == 4
    assert len(stack.data) == 1
    assert stack.data[1] == deque([5, 7])
    

