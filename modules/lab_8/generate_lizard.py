import random
from typing import List, Optional, Dict, Any
from lizards.lizards_types import Dragon, Dinsaur, Salamandra
import json


class LizardGererator():
    def __init__(self, standards: str = "modules/lab_8/standarts.json", colors: Optional[List[str]] = None):
        self.colors: List[str] = ['Red', 'Golden', 'Brown'] if colors is None else colors
        self.standards: Dict[str, Dict[str, Any]] = self._load_standarts(standards)
        self.drangon_count = self.salamandra_count = self.dinosaur_count = 0


    def get_random_lizard(self) -> Dragon | Dinsaur | Salamandra:

        weigth = random.randint(100, 5_000)
        if weigth <= 300:
            color = random.choice(self.colors[1:])
            wings_len = random.randint(30, 50)
            self.drangon_count += 1
            return Dragon(
                name=f'Dragon_{self.drangon_count}',
                weight=weigth,
                color=color,
                wings_len=wings_len,
                price=self._form_price(weigth, color, wings_len, 'dragon')
            )


        color = random.choice(self.colors)
        if color == "Red" or weigth < 1500:
            wings_len = random.randint(10, 30)
            self.salamandra_count += 1
            return Salamandra(
                name=f'Salamandra_{self.salamandra_count}',
                weight=weigth,
                color=color,
                wings_len=wings_len,
                price=self._form_price(weigth, color, wings_len, 'salamandra')
            )


        wings_len = random.randint(0, 5)
        self.dinosaur_count += 1
        return Dinsaur(
            name=f"Dinosaur_{self.dinosaur_count}",
            weight=weigth,
            color=color,
            wings_len=wings_len,
            price=self._form_price(weigth, color, wings_len, "dinosaur")
        )
    

    def _load_standarts(self, file_path: str = "modules/lab_8/standarts.json"):
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)


    def _form_price(self, weight: float, color: str, wings_len: int, ltype: str) -> float:
        for lizard_type in self.standards.keys():
            if lizard_type == ltype:
                delta_weight = weight / self.standards[ltype]["weight"] if weight / self.standards[ltype]["weight"] < 1 else  self.standards[ltype]["weight"] / weight 
                delta_color = int(color != self.standards[ltype]["color"])
                delta_wings = wings_len / self.standards[ltype]["wings_len"] if wings_len / self.standards[ltype]["wings_len"] < 1 else  self.standards[ltype]["wings_len"] / wings_len 
                return int((3 - delta_weight - delta_color - delta_wings) / 3 * self.standards[ltype]["base_price"])
        return 0
    



if __name__ == "__main__":
    L = LizardGererator()
    for _ in range(10000):
        L.get_random_lizard()

    print(L.drangon_count,"\n",L.salamandra_count,"\n", L.dinosaur_count)