import pytest

def test_a1():
    assert 5 + 5 == 10
    assert 5 - 5 == 0
    assert 5 * 5 == 25
    assert 5 / 5 == 1

def test_a2():
    assert 9/5 == 1.5, "failed test intentionally"

def test_a3():
    assert 9//5 == 1

def test_a4():
    assert 19.5 + 19.5 == 39


@pytest.mark.parametrize("a, b, result", [(1, 3, 4), (100, 200, 300), (1000, 1000, 2000)])
def test_soma(a, b, result):
    assert a + b == result, f"Erro na soma: {a} + {b} deveria ser {result}, mas obteve {a + b}"

@pytest.mark.parametrize("a, b, result", [(10, 2, 5), (100, 5, 20), (1000, 500, 2)])
def test_divisao(a, b, result):
    assert a / b == result, f"Erro na soma: {a} + {b} deveria ser {result}, mas obteve {a + b}"

@pytest.mark.parametrize("a, b, result", [(5, 5, 25), (2, 1, 2), (100, 11, 1100)])
def test_multiplicacao(a, b, result):
    assert a * b == result, f"Erro na soma: {a} + {b} deveria ser {result}, mas obteve {a + b}"

@pytest.mark.parametrize("a, b, result", [(10, 5, 5), (100, 50, 50), (5000, 2000, 3000)])
def test_subtracao(a, b, result):
    assert a - b == result, f"Erro na soma: {a} + {b} deveria ser {result}, mas obteve {a + b}"