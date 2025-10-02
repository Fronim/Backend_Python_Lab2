from datetime import date, datetime, time
class Person:
    def __init__ (self, first_name, last_name, birth_date):
        self.__first_name = str(first_name).capitalize()
        self.__last_name = str(last_name).capitalize()
        self.__birth_date = birth_date if isinstance(birth_date, date) else datetime.strptime(birth_date, "%Y-%m-%d")

    @property
    def first_name(self) -> str:
        return self.__first_name

    @property
    def last_name(self) -> str:
        return self.__last_name

    @property
    def birth_date(self) -> date:
        return self.__birth_date

    def get_fname(self) -> str:
        return f"{self.__last_name} {self.__first_name}"

    def get_age(self) -> int:
        today = date.today()
        return (today.year - self.__birth_date.year) if today.month > self.__birth_date.month or (today.month == self.__birth_date.month and today.day > self.__birth_date.day) else (today.year - self.__birth_date.year - 1)

    def get_info(self) -> str:
        return f"Name: {self.get_fname()}\nAge: {self.get_age()}"
