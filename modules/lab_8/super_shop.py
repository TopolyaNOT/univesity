from lizards.lizards_types import Lizard_post_type, Lizard_type
from generate_lizard import LizardGererator
from itertools import chain
from shop import Shop
from typing import List, Dict, Any
import random
import json

class SuperShop(Shop):
    def __init__(self, pack: int = random.randint(1, 5), packs_data_path: str = "modules/lab_8/data/packs.json"):
        super().__init__()
        self._pack_count = pack
        self._pack_variation = self._load_packs(packs_data_path)
        self._lizardgererator = LizardGererator()


    def shopping(self, user: Any) -> List[Lizard_type]:
        packs_distirbution = self._packs_distirbution()
        packs = self._form_pack(packs_distirbution)
        shopping_basket = []


        self._print_welcome(user, self._size)
        while True:
            
            option = input("What do you want to buy?\n(Eggs/Packs/Exit): ")
            if option.lower() == "eggs":
                user_basket = self._buy()
                self._prinnt_all_lizards(user_basket)
                user_basket = self._sell(user_basket)
                
                shopping_basket.append(user_basket)

                continue

            elif option.lower() == "packs":
                pack = self.buy_pack(packs_distirbution, packs)
                shopping_basket.append(pack)

                self._prinnt_all_lizards(shopping_basket)
                continue
            break

        self._print_bay()
        res = list(chain.from_iterable(shopping_basket))
        print(res)
        print(self._advertisement(res))
        return res



    def buy_pack(self, packs_distirbution, packs):
        pack: list

        for key in packs_distirbution.keys():
            print(f"Pack ({key}) \t : \t Amount ({packs[key]["amount"]})")
            pack_to_buy = input("Enter which pack you want to buy: ")

            if pack_to_buy not in packs_distirbution.keys():
                print("Sorry, we dont have sach pack")
                continue
            
            pack_list = packs[pack_to_buy].get("packs")
            if not isinstance(pack_list, list):
                print("We dont have packs")
                continue

            pack_id = random.randint(0, len(pack_list)-1)
            pack_to_sell = packs[pack_to_buy].get("packs")[pack_id] # type: ignore
            pack = pack_to_sell

            self._print_new_lizards()
            for i in pack_to_sell:
                print(i, '\n')

            del pack_to_sell
            packs[pack_to_buy]["amount"] -= 1 # type: ignore

            return pack


    def _form_pack(self, packs_distirbution: Dict[str, int]) -> Dict[str, Dict[str, int | Lizard_post_type]]:
        all_packs = {
            key:{
                "amount" : values, 
                "packs" : self._generate_pack(key, values)
                } 
            for key, values in packs_distirbution.items()
            }
        return all_packs


    def _packs_distirbution(self) -> Dict[str, int]:
        packs_distirbution = {}

        for key in self._pack_variation.keys():
            if self._pack_count <= 0:
                break
            pack_amount = random.randint(1, self._pack_count)
            self._pack_count -= pack_amount
            packs_distirbution[key] = pack_amount
        
        return packs_distirbution


    def _generate_pack(self, pack_type: str, amount: int) -> List[Lizard_post_type]:
        all_packs = []
        for _ in range(amount):
            dragons = self._lizardgererator._gererate_dragon(self._pack_variation[pack_type].get("dragon", 0))
            dinosaur = self._lizardgererator._gererate_dinosaur(self._pack_variation[pack_type].get("dinosaur", 0))
            salamandra = self._lizardgererator._gererate_salamandra(self._pack_variation[pack_type].get("salamandra", 0))
            cat = self._lizardgererator._gererate_cat(self._pack_variation[pack_type].get("cat", 0))
            
            p  = [dragons, salamandra, dinosaur, cat]
            c = list(chain.from_iterable(p))
            all_packs.append(c)
            
        return all_packs


    def _load_packs(self, path: str) -> Dict[str, Dict[str, int]]:
        with open(path, "r", encoding='utf-8') as f:
            return json.load(f)
        

if __name__ == "__main__":
    super_shop = SuperShop()
    a = super_shop.shopping("Sigma")
