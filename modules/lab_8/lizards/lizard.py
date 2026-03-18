
class Lizard:
    def __init__(
        self,
        name: str,
        weight: float,
        color: str,
        wings_len: float,
        price: float,):

        self.name = name
        self.weight = weight
        self.color = color
        self.wings_len = wings_len
        self.price = price
    
    def __repr__(self):
        return f"name: {self.name}\nweight: {self.weight}\ncolor: {self.color}\nwings len: {self.wings_len}\nprice: {self.price}"