from typing import Dict, List
from .calculator_3 import Calculator3
from src.drivers.numpy_handler import NumpyHandler
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body


class MockDriverHandler(DriverHandlerInterface):
    def standard_deviation(self, numbers):
        return super().standard_deviation(numbers)
    
    def variance(self, data: List[float]) -> float:
        return 20


# Integração entre NumpyHandler e Calculator2
def test_calculate_integration():
    mock_request = MockRequest({"numbers": [2.12, 4.62, 1.32]})

    driver = NumpyHandler()
    calculator_3 = Calculator3(driver)
    formated_response = calculator_3.calculate(mock_request)

    assert isinstance(formated_response, dict)
    assert formated_response == {"data": {"Calculator": 3, "result": 'sucesso'}}


def test_calculate():
    mock_request = MockRequest({"numbers": [2.12, 4.62, 1.32]})

    driver = MockDriverHandler()
    calculator_3 = Calculator3(driver)
    formated_response = calculator_3.calculate(mock_request)

    assert isinstance(formated_response, dict)
    assert formated_response == {"data": {"Calculator": 3, "result": 'falha'}}
