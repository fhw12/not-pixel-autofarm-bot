class Claim():
    def __init__(
        self,
        claimed: float,
    ):
        self.claimed = claimed

    def __str__(self):
        return (
            'Claim('
                f'\n\tclaimed: {self.claimed}'
            '\n)'
        )