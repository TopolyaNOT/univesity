from generate_lizard import LizardGererator
from lizards.lizards_types import Dragon, Dinsaur, Salamandra
from collections import Counter
from typing import Any, List
import random
import re


LizardTypes = Dragon | Dinsaur | Salamandra

class Shop:
    def __init__(self, size: int = random.randint(1, 50)):
        self._size = size
        self._lizardgererator = LizardGererator()


    def shopping(self, user: Any) -> List[LizardTypes]:
        self._welcome(user)

        user_basket = self._buy()
        for i in user_basket:
            print('\n',i)

        user_basket2 = self._sell(user_basket)

        print(self._advertisement(user_basket))

        return user_basket2


    def _welcome(self, user: Any) -> None:
        print(f"Welcome {user}\n\nToday we have {self._size} eggs")


    def _buy(self) -> List[LizardTypes]:
        number_to_buy = 1
        while True:
            number_to_buy = int(input("How many eggs do you want to duy?\nAmount: "))
            if number_to_buy < 0:
                print("Please enter valide amount!!!!!!!!")
                continue
            if number_to_buy > self._size:
                print("Sorry we don't have sush amount of eggs")
                continue
            
            self._size -= number_to_buy
            break
                
        return [self._lizardgererator.get_random_lizard() for _ in range(number_to_buy)]


    def _advertisement(self, user_basket: List[LizardTypes]) -> str:
        l = Counter([lizard.lizard_type for lizard in user_basket])
        types_result = f"Dragons \t:\t{l['dragons']}\nSalamandras\t:\t{l['salamandra']}\nDinosaurs\t:\t{l['dinosaur']}"
        phrase = None
        l_len = len(user_basket)
        if l_len < 3:
            phrase = "What a nice lizard you have"
        elif l_len >=3 and l_len < 20:
            phrase = "I suppose you are profetional trainer. Well good luck!"
        else:
            phrase = "Men... WTF  ???"
        return f'{types_result}\n{phrase}'
    

    def _sell(self, lizard_list: List[LizardTypes]) -> List[LizardTypes]:
        seccessful = input("Do you want to change some lizards?\n(Yes/No)")
        compensation = 0
        if seccessful.lower() == "yes":
            raw_lizard_to_change = input("Etner lizard's name to change: ")
            clean_lizard_to_change = re.findall(r"\w", raw_lizard_to_change)
            for i in lizard_list:
                if i.name in clean_lizard_to_change:
                    lizard_list.append(self._lizardgererator.get_random_lizard())
                    compensation += int(i.price / 3)
                    lizard_list.remove(i)
            print(f"Compensation is {compensation}")
        return lizard_list
                    

if __name__ == "__main__":
    shop_a = Shop()
    l = shop_a.shopping("Bob")
    print(l)