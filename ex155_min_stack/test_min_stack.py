import sol1

def test_push_pop_1():
    sol = sol1.MinStack()
    sol.push(1)
    assert sol.pop() == 1

def test_push_pop_2():
    sol = sol1.MinStack()
    sol.push(1)
    sol.push(2)
    assert sol.pop() == 2

def test_getmin():
    sol = sol1.MinStack()
    sol.push(1)
    sol.push(2)
    assert sol.getMin() == 1