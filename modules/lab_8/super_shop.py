from lizards.lizards_types import Lizard_post_type
from itertools import chain
from shop import Shop
from typing import List, Dict
import random
import json

class SuperShop(Shop):
    def __init__(self, pack: int = random.randint(1, 5), packs_data_path: str = "modules/lab_8/data/standarts.json"):
        self._pack_count = pack
        self._pack_variation = self._load_packs(packs_data_path)
        self._pack_count_variation = self._generate_pack()

    def shopping(self, user: random.Any) -> List[Lizard_post_type]:
        while True:
            option = input("What do you want to buy?\n(Eggs/Packs/Exit): ")
            if option.lower() == "eggs":
                super().shopping(user)
            elif option.lower() == "packs":


    def _generate_pack(self) -> List[List[Lizard_post_type]]:
        all_packs = []
        for _ in range(self._pack_count):
            pack = random.choice([self._pack_variation.keys()])

            dragons = self._lizardgererator._gererate_dragon(self._pack_variation[pack].get("dragons"))
            dinosaur = self._lizardgererator._gererate_dinosaur(self._pack_variation[pack].get("dinosaur"))
            salamandra = self._lizardgererator._gererate_salamandra(self._pack_variation[pack].get("salamandra"))
            cat = self._lizardgererator._gererate_cat(self._pack_variation[pack].get("cat"))
            
            all_packs.append(list(chain([*dragons, *salamandra, *dinosaur, *cat])))
      
        return all_packs

    def _load_packs(self, path: str) -> Dict[str, Dict[str, int]]:
        with open(path, "r", encoding='utf-8') as f:
            return json.load(f)
        

if __name__ == "__main__":
    super_shop = SuperShop()
    super_shop.shopping("Sigma")
