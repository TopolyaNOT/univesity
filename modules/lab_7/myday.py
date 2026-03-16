import random 
from model import MegaHuman

class MyDay():
    def __init__(self, human: MegaHuman):
        self.human = human
        self.age = random.randint(0, 100)
        self.work_hours = 6
        self.energy_to_work = random.randint(1, 10)
        if self.age > 16 and self.age < 60:
            self.work_hours = random.randint(4, 16)
    
    
    def run_day(self) -> None:
        if not self.human.is_alive:
            print(self.human.param())

        print("Day start")

        food = ['apple', 'pizza', 'soup', 'vafel', 'kebab', 'meat', 'milk', 'water']

        self.human.eat(random.randint(1, 20), random.choice(food))

        self.human.go(self.energy_to_work)

        self.human.eat(random.randint(1, 20), random.choice(food))

        self.human.top_up(200, 'work')

        self.human.go(self.energy_to_work)

        if random.randint(1, 10) < 3:
            self.human.payment(random.randint(1, 30), random.choice(food))
            self.human.go(self.energy_to_work // 2)

        self.human.eat(random.randint(1, 20), random.choice(food))

        self.human.sleep()

        print("Day end\n")
        print(self.human.param())