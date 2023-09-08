from coffee.americano.americano import make


def test_americano():
    assert make() == "americano"
