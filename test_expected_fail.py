import pytest


@pytest.mark.xfail(reason='Пусть пока падает, завтра починю.')
def test_false():
    assert False


@pytest.mark.xfail(
    "sys.version_info < (2, 1)",
    reason='Это старая версия Python, чего же вы ждали!'
)
def test_for_new_python():
    ...
