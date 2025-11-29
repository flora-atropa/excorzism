import day02

def test_a(day02_text):
    assert day02.a.solve(day02_text) == 1598415

    
def test_b(day02_text):
    assert day02.b.solve(day02_text) == 3812909
