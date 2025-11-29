import day01

def test_a(day01_text):
    assert day01.a.find_floor(day01_text) == 138
    
def test_b(day01_text):
    assert day01.b.find_basement_entry(day01_text) == 1771
