class Pixel():
    def __init__(
        self,
        x: int,
        y: int,
        owner_id: int,
        repaints: int,
        color: str,
        date_obtained: str,
    ):
        self.x = x
        self.y = y
        self.owner_id = owner_id
        self.repaints = repaints
        self.color = color
        self.date_obtained = date_obtained

    def __str__(self):
        return (
            'Pixel('
                f'\n\tx: {self.x}'
                f'\n\ty: {self.y}'
                f'\n\towner_id: {self.owner_id}'
                f'\n\trepaints: {self.repaints}'
                f'\n\tcolor: {self.color}'
                f'\n\tdate_obtained: {self.date_obtained}'
            '\n)'
        )