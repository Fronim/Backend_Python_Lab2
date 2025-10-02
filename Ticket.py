from datetime import date, datetime, time

class Ticket:
    def __init__(self, film_name, film_date, film_time, duration, kino_room, price):
        self.film_name = str(film_name)
        self.film_date = film_date if isinstance(film_date, date) else datetime.strptime(film_date, "%Y-%m-%d").date()
        self.film_time = film_time if isinstance(film_time, time) else datetime.strptime(film_time, "%H:%M").time()
        self.duration = int(duration)
        self.kino_room = str(kino_room)
        self.price = float(price)

    def get_datetime(self) -> datetime:
        return datetime.combine(self.film_date, self.film_time)

    def get_info(self):
        return (
            f"---Ticket---\n"
            f"Name: {self.film_name} at {self.film_date.strftime('%Y-%m-%d')} "
            f"{self.film_time.strftime('%H:%M')}\n"
            f"Duration: {self.duration} minutes\n"
            f"Cinema hall: {self.kino_room}\n"
            f"Price: {self.price}$"
        )

    @staticmethod
    def parse_time(film_date)-> date:
        if isinstance(film_date, date):
            return film_date
        elif isinstance(film_date, datetime):
            return film_date.date()
        elif isinstance(film_date, str):
            return datetime.strptime(film_date, "%Y-%m-%d").date()
        raise ValueError("film_date must be date/datetime or 'YYYY-MM-DD' string")

    @staticmethod
    def parse_time_str(s: str) -> time:
        parts = s.split(":")
        fmt = "%H:%M:%S" if len(parts) == 3 else "%H:%M"
        return datetime.strptime(s, fmt).time()