import main

def test_divison_good():
    assert main.divison(10, 2) == 5.0

def test_divison_2alpha():
    assert main.divison(10, 5) == 2.0

def test_divison_3beta():
    assert main.divison(20, 2) == 10.0

def test_divison_4negative():
    assert main.divison(10,-2) == -5.0