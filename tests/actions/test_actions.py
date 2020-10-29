from actions.actions import add


def test_add():
    assert add(1, 2, 3) == 6
