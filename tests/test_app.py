# test_app.py

from app import add   # import the function you want to test

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
