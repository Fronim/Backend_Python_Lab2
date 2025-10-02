class Shareholder:
    def __init__(self, shares: int = 0):
        self.__shares = int(shares)

    @property
    def shares(self) -> int:
        return self.__shares

    def add_shares(self, n: int):
        if n < 0:
            raise ValueError("n must be non-negative")
        self.__shares += int(n)

    def remove_shares(self, n: int):
        n = int(n)
        if n < 0 or n > self.shares:
            raise ValueError("invalid number of shares to remove")
        self.__shares -= n

    def get_dividend(self, per_share: float) -> float:
        return self.calc_dividend_for(self.shares, float(per_share))

    def get_info_shares(self) -> str:
        return f"Shares: {self.shares}"

    @staticmethod
    def calc_dividend_for(shares: int, per_share: float) -> float:
        return int(shares) * float(per_share)
