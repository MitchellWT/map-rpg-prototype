
class Player:
    def __init__(self, name, health, stamina, mana, exp, level, base_level_value, factor=1):
        self.name = name
        self.health = health
        self.stamina = stamina
        self.mana = mana
        self.exp = exp
        self.level = level
        self.next_level_cap = base_level_value * (level * factor)
        self.base_level_value = base_level_value
        self.factor = factor

    def gain_exp(self, exp):
        self.exp += exp
        if self.exp >= self.next_level_cap:
            self.level += 1
            self.exp -= self.next_level_cap
            self.next_level_cap = self.base_level_value * (self.level * self.factor)
            # May call a function for a level up screen/interface?
