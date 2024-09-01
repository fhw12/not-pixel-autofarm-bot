class UserStatus():
    def __init__(
        self,
        coins: float,
        claimed: float,
        total_user_pixels: int,
        user_balance: float,
        charges: int,
        max_charges: int,
    ):
        self.coins = coins
        self.claimed = claimed
        self.total_user_pixels = total_user_pixels
        self.user_balance = user_balance
        self.charges = charges
        self.max_charges = max_charges

    def __str__(self):
        return (
            'UserStatus('
                f'\n\tcoins: {self.coins}'
                f'\n\tclaimed: {self.claimed}'
                f'\n\ttotal_user_pixels: {self.total_user_pixels}'
                f'\n\tuser_balance: {self.user_balance}'
                f'\n\tcharges: {self.charges}'
                f'\n\tmax_charges: {self.max_charges}'
            '\n)'
        )