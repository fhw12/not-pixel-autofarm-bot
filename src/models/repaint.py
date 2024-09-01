class Repaint():
    def __init__(
        self,
        balance: float,
    ):
        self.balance = balance

    def __str__(self):
        return (
            'Repaint('
                f'\n\tbalance: {self.balance}'
            '\n)'
        )