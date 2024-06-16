import pytest

from engine_class import Engine


@pytest.fixture
def engine():
    """Фикстура возвращает экземпляр класса двигателя."""
    return Engine()


@pytest.fixture
def start_engine(engine):
    """Фикстура запускает двигатель."""
    engine.is_running = True


def test_engine_is_running(engine, start_engine):
    """Тест проверяет, работает ли двигатель."""
    assert engine.is_running
