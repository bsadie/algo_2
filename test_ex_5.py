
from ex_5 import GenerateBBSTArray

def test_1():
    a = [1, 2, 3]
    b = GenerateBBSTArray(a)
    print(b)
    assert b[0] == 2
    assert b[1] == 1
    assert b[2] == 3


def test_2():
    a = [0, 1, 2, 3, 4, 5]
    b = GenerateBBSTArray(a)
    print(b)
    assert b[0] == 3
    assert b[1] == 1
    assert b[2] == 5
    assert b[3] == 0
    assert b[4] == 2
    assert b[5] == 4

def test_3():
    a = []
    b = GenerateBBSTArray(a)
    assert b == []

def test_4():
    a = [1]
    b = GenerateBBSTArray(a)
    assert b == [1]

def test_5():
    a = [1,10]
    b = GenerateBBSTArray(a)
    assert b == [10, 1, None]

def test_6():
    # a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    a = [1, 2, 3, 4, 5, 6, 7]
    b = GenerateBBSTArray(a)
    print(b)
    assert b == [4, 2, 6, 1, 3, 5, 7]

def test_7():
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    b = GenerateBBSTArray(a)
    print(b)
    assert b == [5, 2, 8, 1, 4, 7, 10, 0, None, 3, None, 6, None, 9, None]




