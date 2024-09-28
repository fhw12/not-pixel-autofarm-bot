class UserStatus():
    def __init__(
        self,
        coins: float,
        claimed: float,
        repaints_total: int,
        user_balance: float,
        charges: int,
        max_charges: int,
    ):
        self.coins = coins
        self.claimed = claimed
        self.repaints_total = repaints_total
        self.user_balance = user_balance
        self.charges = charges
        self.max_charges = max_charges

    def __str__(self):
        return (
            'UserStatus('
                f'\n\tcoins: {self.coins}'
                f'\n\tclaimed: {self.claimed}'
                f'\n\repaints_total: {self.repaints_total}'
                f'\n\tuser_balance: {self.user_balance}'
                f'\n\tcharges: {self.charges}'
                f'\n\tmax_charges: {self.max_charges}'
            '\n)'
        )