class HttpUnprocessableEntityError(Exception):
    def __init__(self, message: str) -> None:
        self.message = message
        self.name = 'Unprocessable Entity'
        self.status_code = 422