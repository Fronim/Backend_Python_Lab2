from User import User
from Shareholder import Shareholder

class VIPUser(User, Shareholder):
    def __init__(self, first_name, last_name, birth_date, email, points: int = 0, shares: int = 0):
        User.__init__(self, first_name, last_name, birth_date, email, points)
        Shareholder.__init__(self, shares)

    def get_info(self) -> str:
        return f"VIP {self.get_fname()}, Points: {self.points}, Shares: {self.shares}"

    def redeem_dividend_to_points(self, per_share: float, convert_rate: float = 1.0) -> int:
        dividend = self.get_dividend(per_share)
        added_points = int(dividend * float(convert_rate))
        self.points += int(added_points)
        return int(added_points)

    def vip_level_by_shares(shares: int) -> str:
        shares = int(shares)
        if shares >= 100:
            return "Platinum"
        if shares >= 50:
            return "Gold"
        if shares >= 10:
            return "Silver"
        return "Bronze"