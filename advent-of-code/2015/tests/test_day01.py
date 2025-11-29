import day01

def test_a(day01_text):
    assert day01.a.solve(day01_text) == 138
    
def test_b(day01_text):
    assert day01.b.solve(day01_text) == 1771
