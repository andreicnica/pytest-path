from coffee.americano.local_settings import make_settings


def test_make_settings():
    assert make_settings() == "americano"
