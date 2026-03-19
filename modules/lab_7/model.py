from typing import List, Tuple
import random



class Mammals:
    def __init__(
        self,
        height: float,          
        weight: float,
        limbs_count: int,
        mammal_type: str,
        sex: str
    ):
        self.sex = sex
        self.height = height         
        self.weight = weight
        self.limbs_count = limbs_count
        self.mammal_type = mammal_type
        self.is_alive = True
        self._energy = 50.0
        self.start_mass = weight
    
    
    @property
    def volume(self) -> float:
        return self.height * self.weight


    def sleep(self) -> float:
        if self._check_death():
            return 0

        self._energy = round(self.height - self.weight / self.height * 50, 2)
        weight = round(self.weight - self._energy ** 0.3, 2)
        if self.start_mass // 2 >= weight:
            self.is_alive = False
            self._dead_stats()
            print("Animal dead")
            return 0
        self.weight = weight
        print("Sleep")
        return self._energy
    

    def eat(self, amount: float) -> float:
        if self._check_death():
            return 0
        elif self.weight >= self.start_mass * 3:
            self.is_alive = False
            self._dead_stats()
            print("Animal dead")
            return 0

        if amount <= self.weight // 20 and amount >= self.volume ** 0.3:
            self._energy += amount / self.weight * 20
            self.weight += amount
            print("Eat")
            return self._energy
        elif amount >= self.weight // 20:
            print("Eat max")
            self._energy += self.weight // 20 / self.weight * 20
            self.weight += self.weight // 20
            return self._energy

        print("Not enough energy")
        return 0
    

    def go(self, energy: float) -> float:
        if self._check_death():
            return 0
        
        if energy > self._energy:
            print("Animal die")
            self.is_alive = False
            return 0
        
        km = round(energy * self.volume ** 0.5 + energy * self.limbs_count, 2)
        self._energy = round(self._energy - energy, 2)
        self.weight -= round(energy ** 2, 2)

        print(f"Covered the distance: {km}")
        return km
    
    @property
    def _is_weight_ok(self) -> bool:
        return self.start_mass * 3 < self.weight


    def _check_death(self) -> bool:
        if self.is_alive and self._is_weight_ok:
            self._dead_stats()
            print("It's dead")
            return False
        return True
    

    def _dead_stats(self) -> None:
        if self.is_alive:
            return

        self.mammal_type = 'compost'
        self.is_alive = False
        self._energy = 0


class Money:
    _balance: float = 0
    _history: List[Tuple[str, str, float]] = []     # order_type, odject, amount

    def my_balance(self) -> float:
        print(f"Balance: {self._balance} грн")
        return self._balance

    def top_up(self, amount: float, product: str) -> bool:
        if amount > 0:
            self._balance += amount
            self._history.append(("earning", product, amount))
            print("Successful add")
            return True
        return False
    
    def payment(self, amount: float, product) -> bool:
        if amount > 0:
            if self._balance - amount >= 0:
                self._balance -= amount 
                self._history.append(("spending", product, amount))
                print("Successful payment")
                return True
            print("Not enuouh balance")
            return False
        print("Not valide amount")
        return False


class Human_V6(Mammals, Money):
    def __init__(self, name: str, sex: str, mood: str, height: float, weight: float, limbs_count: int, mammal_type: str):
        super().__init__(height, weight, limbs_count, mammal_type, sex)
        self.name = name
        self.mood = mood
        self._stocks = 0


    def eat(self, amount: float) -> float:
        if not self.is_alive:
            self._dead_stats()
            print("It's dead")
            return 0
        elif self.weight >= self.start_mass * 3:
            self.is_alive = False
            self._dead_stats()
            print("Animal dead")
            return 0
        
        if amount <= self.weight // 20 and amount >= self.volume ** 0.3:
            self._energy += round(amount / self.weight * 20, 2)
            self.weight += amount
            self._mood_analyzer()
            print("Eat")
            return self._energy
        elif amount >= self.weight // 20:
            self._energy += round(self.weight // 20, 2)

            self._stocks += round(amount - self.weight // 20, 2)
            self.weight += self.weight // 20
            self._mood_analyzer()
            print("Eat max")
            return self._energy
        
        elif amount + self._stocks >= self.volume ** 0.3:
            nes = round(self.volume ** 0.3 - amount, 2)
            self._energy = amount + nes
            self._stocks -= nes
            print("Eat min")
            return self._energy
        

        print("Not enough energy")
        return 0


    def sleep(self) -> float:
        if not self.is_alive:
            self._dead_stats()
            print("It's dead")
            return 0
        
        if self._energy <= 50:
            r = super().sleep()
            self._mood_analyzer()
            return r

        energy_drink = (1, 2)
        factor = random.randint(1, 10)
    
        if factor in energy_drink:
            self._energy += 3 + factor * 2
            self._mood_analyzer()
            print("drink an energy drink")

        weight = round(self.weight - self._energy ** 0.3, 2)
        if self.start_mass // 2 >= self.weight:
            self.is_alive = False
            print("Animal dead")
            return 0
        self.weight = weight
        
        return self._energy


    def go(self, energy: float) -> float:
        r = super().go(energy=energy)
        if not self.is_alive:
            self._dead_stats()
            return 0
        self._mood_analyzer()
        return r


    def param(self) -> None:
        print(f"name: {self.name}\nsex: {self.sex}\nmammal_type: {self.mammal_type}\nheight: {self.height}"
              f"\nweight: {self.weight}\nenergy: {self._energy}\nmood: {self.mood}\nalive: {self.is_alive}")

    def top_up(self, amount: float, product: str) -> bool:
        super().top_up(amount, product)
        energy_cof = amount / self._balance * 5 
        self._energy += energy_cof
        self._mood_analyzer()

        return True


    def payment(self, amount: float, product: str) -> bool:
        super().payment(amount, product)
        if self._balance > 0:
            energy_cof = amount / self._balance * 5
            self._energy -= energy_cof
        self._mood_analyzer()
        return True


    def _dead_stats(self) -> None:
        self.mood = "Fatal"
        return super()._dead_stats()

    def _mood_analyzer(self) -> str:
        if self._energy <= 0:
            self.is_alive = False
            return "It's dead"
        elif self._energy > 0 and self._energy <= 20:
            self.mood = "very bad"
            return self.mood
        elif self._energy > 20 and self._energy <= 50:
            self.mood = "bad"
            return self.mood
        elif self._energy > 50 and self._energy <= 75:
            self.mood = "good"
            return self.mood
        else:
            self.mood = "very good"
            return self.mood


class MegaHuman(Human_V6):
    def __init__(
            self, 
            name:str, 
            sex: str, 
            job: str, 
            mood: str, 
            favorite_food: str, 
            height: float, 
            weight: float, 
            limbs_count: int, 
            mammal_type: str):
        super().__init__(name, sex, mood, height, weight, limbs_count, mammal_type)
        self.job = job
        self.favorite_food = favorite_food

    def eat(self, amount: float, food: str = 'kebab') -> float:
        super().eat(amount)
        if food == self.favorite_food:
            self._energy += 20
            print("I like this")
        return self._energy
    
    
    def heart_attack(self) -> bool:
        attack = random.randint(1, 1000)
        factor = random.randint(1, 1000)
        if attack == factor:
            self.is_alive = False
            self._dead_stats()
            print("Die from heart_attack")
            return True
        return False