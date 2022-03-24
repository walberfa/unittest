from datetime import datetime
import requests
import json


class Calendario:

    def __init__(self, date):
        self.hoje = date.today()

    def is_weekend(self):
        return self.hoje.weekday() >= 5
