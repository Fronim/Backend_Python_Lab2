from Person import Person
from Ticket import Ticket
from User import User
from VIPUser import VIPUser

def line(): print("-" * 60)

def main():
    line()
    print("STEP 1. Create Person")
    person = Person("ivan", "petrenko", "1990-05-12")
    print(person.get_info())

    line()
    print("STEP 2. Create Tickets")
    t_future1 = Ticket("Dune 2", "2025-12-01", "19:30", 150, "Hall 1", 12.5)
    t_future2 = Ticket("Avatar 2", "2025-12-01", "21:00", 160, "Hall 2", 14.0)
    t_past   = Ticket("Old Movie", "2020-01-01", "10:00", 90,  "Hall 3", 5.0)

    for t in [t_future1, t_future2, t_past]:
        print(t.get_info())

    line()
    print("STEP 3. User actions")
    user = User("oksana", "shevchenko", "2001-08-22", "oksana@example.com", points=10)
    print("User before:", user.get_info())

    user.buy_ticket(t_future1)
    user.buy_ticket(t_future2)
    user.buy_ticket(t_past)
    print("User after:", user.get_info())
    print("User tickets:")
    user.show_tickets()

    line()
    print("STEP 4. VIP Customer who is also a Shareholder")
    vip = VIPUser("andriy", "koval", "1980-02-10", "andriy@vip.com", points=200, shares=50)
    print("VIP before:", vip.get_info())

    vip.buy_ticket(t_future2)
    print("Vip got " + str(vip.redeem_dividend_to_points(per_share=0.5, convert_rate=2.0)) + " points for his dividend")
    print("VIP after:", vip.get_info())
    print("VIP tickets:")
    vip.show_tickets()

    line()
    print("STEP 5. Polymorphism (get_info on different objects)")
    objects = [person, user, vip, t_future1]
    for obj in objects:
        print(f"[{type(obj).__name__}] -> {obj.get_info()}")

if __name__ == "__main__":
    main()