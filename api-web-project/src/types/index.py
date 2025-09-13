class User:
    def __init__(self, id: int, name: str, email: str):
        self.id = id
        self.name = name
        self.email = email

class Item:
    def __init__(self, id: int, title: str, description: str):
        self.id = id
        self.title = title
        self.description = description

class ResponseModel:
    def __init__(self, message: str, data: dict):
        self.message = message
        self.data = data