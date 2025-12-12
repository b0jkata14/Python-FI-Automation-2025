class Character:
    def __init__(self, name, level, hp, power):
        self.name = name
        self.level = level
        self.hp = hp
        self.power = power

    @classmethod
    def from_string(cls, text):
        ctype, name, level, hp, power = text.split(";")
        level, hp, power = int(level), int(hp), int(power)

        if ctype == "Warrior":
            return Warrior(name, level, hp, power)

        elif ctype == "Mage":
            return Mage(name, level, hp, power)

        elif ctype == "Archer":
            return Archer(name, level, hp, power)

    def attack(self):
        return self.power * self.level

    def __repr__(self):
        return f"Character name={self.name}, level={self.level}, hp={self.hp}, power={self.power}"


class Warrior(Character):
    def attack(self):
        return self.power * self.level * 1.2


class Mage(Character):
    def __init__(self, name, level, hp, power, mana=100):
        super().__init__(name, level, hp, power)
        self.mana = mana

    def attack(self):
        return self.power * self.level * 1.5


class Archer(Character):
    def attack(self):
        return self.power * self.level * 1.1


def battle_round(characters):
    return sorted(
        characters,
        key=lambda ch: (-ch.attack(), ch.name)
    )