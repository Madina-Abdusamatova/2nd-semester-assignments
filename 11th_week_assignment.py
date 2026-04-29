from dataclasses import dataclass, field
from contextlib import contextmanager


class TicketError(Exception):
    pass

@dataclass
class Ticket:
    title: str
    genre: str
    price: float
    _status: str = field(init = False, default = "Pending")

    def __post_init__(self):
        if self.price <= 0:
            raise TicketError(f"Invalid price for {self.title}")
        
    @property
    def is_premium(self):
        return self.price > 15.0
    
    def __str__(self):
        return f"{self.title} ({self.genre}, ${self.price}) [{self._status}]"
    
    def __gt__(self, other):
        return self.price > other.price
    

class ShowScanner:
    def __init__(self, tickets, genres):
        self.tickets = tickets
        self.genres = genres
        self.index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.tickets):
            raise StopIteration
        
        ticket = self.tickets[self.index]
        self.index += 1

        if ticket.genre in self.genres:
            ticket._status = "ON SALE"
        else:
            ticket._status = "SOLD OUT"

        return ticket
    
def show_report(scanner):
        on_sale = 0
        sold_out = 0
        
        for ticket in scanner:
            if ticket._status == "ON SALE":
                on_sale += 1
            else:
                sold_out += 1

            yield str(ticket)

        yield f"Report: {on_sale} on sale, {sold_out} sold out"


@contextmanager
def box_office(name):
    tickets =[]
    print(f">>> Showing: {name}")
    try:
        yield tickets

    except TicketError as e:
        print(f"!!! Error: {e}")

    finally:
        print(f"<<< Ended: {name} ({len(tickets)} tickets)") 

with box_office("Friday Night") as tickets:
    tickets.append(Ticket("Inception", "Sci-Fi", 12.5))
    tickets.append(Ticket("The Godfather", "Drama", 15.0))
    tickets.append(Ticket("Barbie", "Comedy", 9.99))

    for line in show_report(ShowScanner(tickets, ("Sci-Fi", "Drama"))):
        print(line)

    print(tickets[1] > tickets[0])

print()

with box_office("Saturday Night") as tickets:
    tickets.append(Ticket("Avatar", "Sci-Fi", -5.0))
