'''
This file contains the Simulator class which handles the simulation logic.
'''
import secrets

class Simulator:
    def __init__(self):
        self.age = 5
        self.money = 1000
    def go_on(self):
        n = secrets.SystemRandom().randint(1, 10)
        self.age += n
        event = secrets.choice(["earn_money", "yes", "good", "lose_money", "death"])
        if event in ("earn_money", "yes", "good"):
            earned_money = secrets.SystemRandom().randint(1, 100000)
            self.money += earned_money
        elif event == "lose_money":
            lost_money = secrets.SystemRandom().randint(1, 100000)
            # if lost_money > self.money:
            #     lost_money = self.money
            self.money -= lost_money
        elif event == "death":
            restart = secrets.SystemRandom().randint(-1, 10)
            if restart > 0:
                self.money -= secrets.SystemRandom().randint(1, 100000)
                event = "sick"
            # self.money = 0
        return self.age, self.money, event
