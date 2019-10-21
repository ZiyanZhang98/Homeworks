class Orc:
    def __init__(self, name, skill, strength, weapon=None):
        self._name = name
        self._skill = skill
        self._strength = strength
        self._weapon = weapon

    def set_name(self, name):
        self._name = name

    def set_skill(self, skill):
        self._skill = skill

    def set_strength(self, strength):
        self._strength = strength

    def set_weapon(self, weapon):
        self._weapon = weapon

    def get_name(self):
        return self._name

    def get_skill(self):
        return self._skill

    def get_strength(self):
        return self._strength

    def get_weapon(self):
        return self._weapon

    def __str__(self):
        return 'name: %s, skill: %d, strength: %d, weapon: %s' % (self._name, self._skill, self._strength, self._weapon)

    def __gt__(self, other):
        winner = 2
        if self._weapon is None:
            if other.get_weapon() is None:
                if self._strength > other.get_strength():
                    winner = 0
                elif self._strength < other.get_strength():
                    winner = 1
            else:
                winner = 1
        else:
            if other.get_weapon() is None:
                winner = 0
            else:
                if other.get_skill() < self._skill:
                    winner = 0
                elif other.get_skill() > self._skill:
                    winner = 1
        return winner

    def attack(self, other):
        winner = self > other
        if winner == 0:
            self._skill *= 1.05
            print('winner is '+self._name)
            return self._name
        elif winner == 1:
            skills = other.get_skill()
            other.set_skill(skills*1.05)
            print('winner is '+other.get_name())
            return other.get_name()
        else:
            print('They both loose.')
            return None

