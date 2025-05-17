class DatabaseError(Exception):
    def __init__(self, message: str = "Ошибка при работе с базой данных"):
        self.message = message
        super().__init__(self.message)


class NotFoundError(DatabaseError):
    def __init__(self, entity_name: str = "Объект"):
        message = f"{entity_name} не найден"
        super().__init__(message)
