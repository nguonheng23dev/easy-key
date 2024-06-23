from datetime import datetime


class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
    

class TokenCache(metaclass=Singleton):
    
    def __init__(self) -> None:
        self.access_token: str = None
        self.expiration_time: datetime = None

    @property
    def access_token(self) -> str:
        return self._access_token
    
    @property
    def expiration_time(self) -> datetime:
        return self._expiration_time
    
    @access_token.setter
    def access_token(self, value: str) -> None:
        self._access_token = value

    @expiration_time.setter
    def expiration_time(self, value: datetime) -> None:
        self._expiration_time = value
