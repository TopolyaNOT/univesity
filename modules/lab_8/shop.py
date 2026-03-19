from generate_lizard import LizardGererator
from lizards.lizards_types import Lizard_type
from collections import Counter
from typing import Any, List
import random
import re


class Shop:
    def __init__(self, size: int = random.randint(1, 50)):
        self._size = size
        self._lizardgererator = LizardGererator()


    def shopping(self, user: Any) -> List[Lizard_type]:
        self._welcome(user)

        user_basket = self._buy()
        self._prinnt_all_lizards(user_basket)

        user_basket = self._sell(user_basket)


        print(self._advertisement(user_basket))

        return user_basket


    def _welcome(self, user: Any) -> None:
        print(
            "\n======================================================="
            f"\n                 WELCOME {user.upper()}               "
            f"\n               TODAY WE HAVE {self._size} EGGS        "
            "\n=======================================================")


    def _buy(self) -> List[Lizard_type]:
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


    def _advertisement(self, user_basket: List[Lizard_type]) -> str:
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

        print(
            "\n==================================================="
            "\n||          THANK YOU FOR PURCHASE               ||"
            "\n===================================================")
        return f'\n{types_result}\n\n{phrase}'
    

    def _sell(self,  lizard_list: List[Lizard_type]) -> List[Lizard_type]:
        successful = input("Do you want to change some lizards?\n(Yes/No): ")
        compensation = 0

        if successful.lower() != 'yes':
            self._prinnt_all_lizards(lizard_list)
            return lizard_list

        raw_lizard_to_change = input("\nEnter lizard's name to change: ")
        clean_lizard_to_change = re.findall(r"[a-zA-Z]+_\d+", raw_lizard_to_change)
        print(
            "\n==================================================="
            "\n||                  NEW LIZARDS                  ||"
            "\n===================================================")
        for i, v in enumerate(lizard_list):
            if v.name in clean_lizard_to_change:
                compensation += v.price // 3

                new_lizard = self._lizardgererator.get_random_lizard()
                print('\n',new_lizard)
                lizard_list[i] = new_lizard
                    

        print(f"\nCompensation is {compensation}")
        self._prinnt_all_lizards(lizard_list)

        return self._sell(lizard_list)     


    def _prinnt_all_lizards(self, lizard_list: List[Lizard_type]) -> None:
        print(
            "\n==================================================="
            "\n||                  ALL LIZARDS                  ||"
            "\n===================================================")
        for i in lizard_list:
            print('\n',i)




if __name__ == "__main__":
    shop_a = Shop()
    l = shop_a.shopping("Bob")