from typing import Dict, List
from pytest import raises
from .calculator_3 import Calculator3
from src.drivers.numpy_handler import NumpyHandler


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body


class MockDriverHandlerError:
    def variance(self, data: List[float]) -> float:
        return 3


class MockDriverHandler:
    def variance(self, data: List[float]) -> float:
        return 1000000


# Integração entre NumpyHandler e Calculator3
def test_calculate_integration_with_variance_lower_than_multiplication():
    mock_request = MockRequest({"numbers": [1, 2, 3, 4, 5]})
    calculator_3 = Calculator3(MockDriverHandlerError())

    with raises(Exception) as excinfo:
        calculator_3.calculate(mock_request)

    assert str(excinfo.value) == 'Falha no processo: Variância menor que multiplicação'


def test_calculate_integration_with_variance_higher_than_multiplication():
    mock_request = MockRequest({"numbers": [1, 1, 1, 1, 100]})
    calculator_3 = Calculator3(MockDriverHandler())

    response = calculator_3.calculate(mock_request)

    assert isinstance(response, dict)
    assert response == {'data': {'Calculator': 3, 'value': 1000000, 'success': True}}
