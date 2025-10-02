from datetime import date, datetime, time
from Person import Person
class User(Person):
    def __init__(self, first_name, last_name, birth_date, email, points: int = 0):
        super().__init__(first_name, last_name, birth_date)
        self.__email = str(email)
        self.__points = int(points)
        self.__tickets = []

    @property
    def email(self) -> str:
        return self.__email

    @property
    def points(self) -> int:
        return self.__points

    @points.setter
    def points(self, val: int):
        self.__points = int(val)

    @property
    def tickets(self):
        return list(self.__tickets)

    def add_ticket(self, ticket) -> bool:
        if ticket.get_datetime() > datetime.today():
            self.__tickets.append(ticket)
            return True
        return False

    def buy_ticket(self, ticket):
        if self.add_ticket(ticket):
            self.__points += int(ticket.price//10)
            print(f"{self.get_fname()} bought a ticket at {ticket.film_name} for {ticket.price}$!")
        else:
            print(f"Ticket for  {ticket.film_name} is outdated!")

    def show_tickets(self):
        if not self.tickets:
            print(f"{self.get_fname()} has no tickets.")
            return
        for ticket in self.__tickets:
            print(ticket.get_info())
            print("---")

    def get_info(self) -> str:
        return f"User: {self.get_fname()}, Email: {self.__email}, Points: {self.__points}"