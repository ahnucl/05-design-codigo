"""
Convenção:
arquivos de teste devem terminar com "_test"
funções de teste devem começar com "test_"

Teste com log e detalhes:
pytest -s -v

mock: elemento controlado para trabalho

"""

from typing import Dict
from pytest import raises
from calculator_1 import Calculator1


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body


def test_calculate():
    mock_request = MockRequest(body={"number": 1})
    calculator1 = Calculator1()
    
    response = calculator1.calculate(request=mock_request)
    
    # Formato da resposta
    assert "data" in response
    assert "Calculator" in response['data']
    assert "result" in response['data']
    
    # Assertividade da resposta
    assert response['data']['result'] == 14.25
    assert response['data']['Calculator'] == 1
    
    
def test_calculate_with_body_error():
    mock_request = MockRequest(body={"something": 1})
    calculator_1 = Calculator1()

    with raises(Exception) as excinfo:
        calculator_1.calculate(mock_request)

    assert str(excinfo.value) == "body mal formatado!"
