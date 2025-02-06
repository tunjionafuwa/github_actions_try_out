from src.app import hello


def test_hello_works_correctly():
    _hello = hello()

    assert _hello == "Hello"


def test_hello_fails():
    _hello = hello() + "not"

    assert _hello != "Hello"
