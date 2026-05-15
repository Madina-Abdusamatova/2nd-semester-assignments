from abc import ABC, abstractmethod
from dataclasses import dataclass, field

class Room(ABC):
    def __init__(self, guest):
        self.guest = guest

    @abstractmethod
    def nightly_rate(self):
        pass

class Single(Room):
    def nightly_rate(self):
        return 300000
    
class Double(Room):
    def nightly_rate(self):
        return 500000
    
class Suite(Room):
    def nightly_rate(self):
        return 1200000

@dataclass  
class HotelManager:
    bookings:list = field(default_factory = list)

    def book(self, room: Room):
        self.bookings.append(room)

    def run(self, exporter, messenger):
        exporter.export(self.bookings)
        messenger.notify(self.bookings)

class Exporter(ABC):
    @abstractmethod
    def export(self, bookings):
        pass

class CsvExporter(Exporter):
    def export(self, bookings):
        for booking in bookings:
            print(f"{booking.guest},{booking.nightly_rate()}")

class Messenger(ABC):
    @abstractmethod
    def notify(self,bookings):
        pass

class SmsMessenger(Messenger):
    def notify(self,bookings):
        for booking in bookings:
            print(    f"[SMS → {booking.guest}] Your room is booked at {booking.nightly_rate()} €/night")


hotel = HotelManager()
hotel.book(Single("Luke"))
hotel.book(Double("Leia"))
hotel.book(Suite("Han"))

hotel.run(CsvExporter(), SmsMessenger())
