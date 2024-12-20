from typing import Dict, List
from flask import request as FlaskRequest
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface

class Calculator3:
    def __init__(self, driver_handler: DriverHandlerInterface):
        self.__driver_handler = driver_handler
    
    def calculate(self, request: FlaskRequest) -> Dict: # type: ignore
        body = request.json
        input_data = self.__validate_body(body)
        calc_result = self.__process_data(input_data)

        formated_response = self.__format_response(calc_result)
        return formated_response

    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise Exception("body mal formatado!")
        
        input_data = body["numbers"]
        return input_data
    
    def __process_data(self, input_data: List[float]) -> str:
        variance_result = self.__driver_handler.variance(input_data)
        
        multiplication_result = 1
        for num in input_data:
            multiplication_result *= num
        
        result = 'sucesso' if variance_result < multiplication_result else 'falha'
        return result

    def __format_response(self, calc_result: str) -> Dict:
        return {
            "data": {
                "Calculator": 3,
                "result": calc_result
            }
        }