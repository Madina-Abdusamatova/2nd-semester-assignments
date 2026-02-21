class CinemaScreen:
    def __init__(self, name, total_chairs, taken_chairs=0):
        self._name = name
        self.total_chairs = total_chairs
        self.taken_chairs = taken_chairs
    @property
    def name(self):
        return self._name
    @property
    def total_chairs(self):
        return self._total_chairs

    @total_chairs.setter
    def total_chairs(self, value):
        if value < 1:
            raise ValueError("Total chairs must be at least 1")
        self._total_chairs = value

    @property
    def taken_chairs(self):
        return self._taken_chairs

    @taken_chairs.setter
    def taken_chairs(self, value):
        if value < 0:
            raise ValueError("Taken chairs cannot be negative")
        if value > self.total_chairs:
            raise ValueError("Taken chairs cannot exceed total chairs")
        self._taken_chairs = value

    @property
    def open_chairs(self):
        return self.total_chairs - self.taken_chairs
    @property
    def fill_rate(self):
        if self.total_chairs == 0:
            return 0.0
        return round((self.taken_chairs * 100) / self.total_chairs, 1)
    def sell(self, tickets):
        if tickets <= 0:
            raise ValueError("Number of tickets must be positive")
        if tickets > self.open_chairs:
            raise ValueError("Not enough open chairs")
        self.taken_chairs += tickets
    def refund(self, tickets):
        if tickets <= 0:
            raise ValueError("Number of tickets must be positive.")
        if tickets > self.taken_chairs:
            raise ValueError("Cannot refunt more than sold.")
        self.taken_chairs -= tickets
    
s = CinemaScreen("Screen 1", 120)
print(s.name, s.open_chairs, s.fill_rate)

s.sell(80)
print(s.taken_chairs, s.fill_rate)

s.refund(20)
print(s.open_chairs)

try:
    s.sell(70)
except ValueError as e:
    print(e)

try:
    s.name = "X"
except AttributeError:
    print("Cannot change screen name")