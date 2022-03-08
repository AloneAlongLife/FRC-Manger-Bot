from discord import Client
from models import json

class Custom_Client(Client):
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)

    def run(self, *args, **kwargs) -> None:
        return super().run(*args, **kwargs)