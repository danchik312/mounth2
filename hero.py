class SuperHero:
    people = 'people'
    def __init__(self, name, nickname, superpower, hp, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.hp = hp
        self.catchphrase = catchphrase
    def hero_name(self):
        return ("Name:", self.name)

    def x2health(self):
        self.hp *= 2
    def __str__(self):
        return (f'\n Hero name: {self.nickname}\n Superpower: {self.superpower}\n Hp: {self.hp}\n Catchphrase: {self.catchphrase}')
    def __len__(self):
        return len(self.catchphrase.replace(" ",""))
class Hero(SuperHero):
    def __init__(self, name, nickname, superpower, hp, catchphrase):
        super().__init__(name, nickname, superpower, hp, catchphrase)
        super().hero_name()
        super().x2health
        super().__str__()
        super().__len__()
class AirHero(SuperHero):
    def __init__(self, name, nickname, superpower, hp, catchphrase, damage):
        super().__init__(name, nickname, superpower, hp, catchphrase)
        self.damage = damage
        self.fly = False

    def x2health(self):
        self.hp **= 2
        self.fly = True

    def true_phrase(self):
        return True in self.catchphrase.split()

    def __str__(self):
        return super().__str__() + f"\n Fly: {self.fly}"

hero1 = AirHero("Clark Kent", "Superman",
                  "Flight, Super Strength", 600, "Up, up and away!" , 590)
hero1.x2health()
class EarthHero(SuperHero):
    def __init__(self, name, nickname, superpower, hp, catchphrase, damage):
        super().__init__(name, nickname, superpower, hp, catchphrase)
        self.damage = damage

    def x2health(self):
        super().x2health()
        self.fly = False

    def true_phrase(self):
        return True in self.catchphrase.split()

    def __str__(self):
        return super().__str__() + f"\n Fly: {self.fly}"
class Villain(AirHero):
    def __init__(self, name, nickname, superpower, hp, catchphrase, damage):
        super().__init__(name, nickname, superpower, hp, catchphrase, damage)
        self.people = "monster"

    def gen_x(self):
        pass

    def crit(self, power):
        return self.damage ** power


villain1 = Villain("Джон", "Хоумлэндер",
                   "Сверхчеловеческая сила, выносливость, летание",
                   600, "Я люблю Америку.", 550)
villain1.x2health()
damage_power = 2
# print(f"Health: {villain1.hp}, Fly: {villain1.fly}")
# print(f"Health: {hero1.hp}, Fly: {hero1.fly}")
# print(f"Critical Damage: {villain1.crit(damage_power)}")
# print(str(villain1))




