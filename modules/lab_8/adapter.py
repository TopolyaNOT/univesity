from .shop import Shop
from .lizards.lizards_types import Lizard_type, Lizard_post_type, Cat
from typing import List
import random


class Adapter:
    def __init__(self):
        self.cats = 0


    def mas_adapt(self, lizard_list: List[Lizard_type]) -> List[Lizard_post_type]:
        for idx, lizard in enumerate(lizard_list):
            if not self._is_safe(lizard):
                lizard_list[idx] = self._generate_cat() # type: ignore
        return lizard_list # type: ignore


    def adapt(self, lizard: Lizard_type) -> Lizard_post_type:
        if self._is_safe(lizard):
            return lizard
        
        cat = self._generate_cat()
        return cat


    def _is_safe(self, lizard: Lizard_post_type) -> bool:
        return lizard.weight > 600 and lizard.weight < 200 or lizard.wings_len > 40 and lizard.wings_len < 20
        

    def _generate_cat(self) -> Cat:
        self.cats += 1
        weigth = random.randint(5, 12)
        color = random.choice(["Red", "Golden", "Brown"]) 
        wings_len = 0.5
        price = 5000
        return Cat(
            name=f"Cat_{self.cats}",
            weight=weigth,
            color=color,
            wings_len=wings_len,
            price=price
        )



if __name__ == "__main__":
    shop = Shop()
    adapt = Adapter()

    lizards = shop.shopping("Bob")
    res = adapt.mas_adapt(lizards)