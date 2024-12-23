from typing import Dict, List
from flask import request as FlaskRequest
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from src.errors.http_unprocessable_entity import HttpUnprocessableEntity
from src.errors.http_bad_request import HttpBadRequest



class Calculator3:
    def __init__(self, driver_handler: DriverHandlerInterface):
        self.__driver_handler = driver_handler

    
    def calculate(self, request: FlaskRequest) -> Dict: # type: ignore
        body = request.json
        input_data = self.__validate_body(body)

        variance = self.__calculate_variance(input_data)
        multiplication = self.__calculate_multiplication(input_data)
        self.__verify_result(variance, multiplication)

        # calc_result = self.__process_data(input_data)

        formated_response = self.__format_response(variance)
        return formated_response


    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise HttpUnprocessableEntity("body mal formatado!")
        
        input_data = body["numbers"]
        return input_data

    
    def __calculate_variance(self, numbers: List[float]) -> float:
        return self.__driver_handler.variance(numbers)


    def __calculate_multiplication(self, numbers: List[float]) -> float:
        multiplication_result = 1
        for num in numbers: multiplication_result *= num
        return multiplication_result


    def __verify_result(self, variance: float, multiplication: float) -> None:
        if variance < multiplication:
            raise HttpBadRequest('Falha no processo: Variância menor que multiplicação')


    def __format_response(self, variance: float) -> Dict:
        return {
            "data": {
                "Calculator": 3,
                "value": variance,
                "success": True,
            }
        }