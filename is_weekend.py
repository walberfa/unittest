from datetime import datetime


class Calendario:

    def __init__(self, date):
        self.hoje = date.today()

    def is_weekend(self):
        return self.hoje.weekday() >= 5


calendario = Calendario(datetime)
# assert calendario.is_weekend()