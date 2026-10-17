import os

class Config:
    BASE_URL = os.getenv("BASE_URL", "https://jsonplaceholder.typicode.com")
    TIMEOUT = 10


config = Config()