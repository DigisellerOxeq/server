

class DatabaseError(Exception):
    def __init__(self, message: str = "Ошибка при работе с базой данных"):
        self.message = message
        super().__init__(self.message)