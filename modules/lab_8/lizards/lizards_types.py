from .lizard import Lizard


class Salamandra(Lizard):
    def __init__(
            self,
            name: str,
            weight: float,
            color: str,
            wings_len: float,
            price: float
            ):
        
        super().__init__(name, weight, color, wings_len, price)
        self.special = "Resistance"
        self.lizard_type = "salamandra"


    def __repr__(self):
        stats = super().__repr__()
        return f"type: {self.lizard_type}\n{stats}\nspecial: {self.special}"


class Dragon(Lizard):
    def __init__(
            self,
            name: str,
            weight: float,
            color: str,
            wings_len: float,
            price: float
            ):
        
        super().__init__(name, weight, color, wings_len, price)
        self.special = "Flying"
        self.lizard_type = "dragon"


    def __repr__(self):
        stats = super().__repr__()
        return f"type: {self.lizard_type}\n{stats}\nspecial: {self.special}"



class Dinosaur(Lizard):
    def __init__(
            self,
            name: str,
            weight: float,
            color: str,
            wings_len: float,
            price: float
            ):
        
        super().__init__(name, weight, color, wings_len, price)
        self.special = "Fast_Running"
        self.lizard_type = "dinosaur"


    def __repr__(self):
        stats = super().__repr__()
        return f"type: {self.lizard_type}\n{stats}\nspecial: {self.special}"
    

class Cat(Lizard):
    def __init__(
            self, 
            name: str,
            weight: float,
            color: str,
            wings_len: float,
            price: float
    ):
        super().__init__(name, weight, color, wings_len, price)
        self.special = "Kawaii"
        self.lizard_type = "cat"

    def __repr__(self):
            stats = super().__repr__()
            return f"type: {self.lizard_type}\n{stats}\nspecial: {self.special}"



Lizard_type = Salamandra | Dragon | Dinosaur
Lizard_post_type = Lizard_type | Cat