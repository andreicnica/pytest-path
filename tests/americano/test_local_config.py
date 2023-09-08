from coffee.americano.local_config import make_settings


def test_make_settings():
    assert make_settings() == "americano"
