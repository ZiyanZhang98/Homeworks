class Orc:
    def __init__(self, name, skill, strength, weapon=None):
        if skill < 0:
            print('Skill should be a positive number!')
            exit()
        if strength < 0:
            print('Strength should be a positive number')
            exit()
        self._name = name
        self._skill = skill
        self._strength = strength
        self._weapon = weapon

    def set_name(self, name):
        self._name = name

    def set_skill(self, skill):
        if skill < 0:
            print('Skill should be a positive number!')
            exit()
        self._skill = skill

    def set_strength(self, strength):
        if strength < 0:
            print('Strength should be a positive number')
            exit()
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

    def get_name(self):
        return self.__class__.__name__

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
        elif winner == 3:
            return 0
        else:
            print('They both loose.')


class Archer(Orc):
    def __init__(self, name, skill, weapon, belong):
        Orc.__init__(self, name, skill, weapon)
        self._weapon = weapon
        self._belong = belong
        if self._weapon is None:
            print('We need a weapon!')

    def get_belong(self):
        return self._belong

    def set_belong(self, belong):
        self._belong = belong

    def __str__(self):
        return 'name: %s, skill: %d, weapon: %s, belongs to: %s' % (self._name, self._skill, self._weapon, self._belong)

    def __gt__(self, other):
        winner = 2
        if other.get_name() != 'Orc':
            print('Error! You should fight against an orc.')
            return 3
        
        if other.get_weapon() is None:
            winner = 2
        else:
            if self._skill > other.get_skill():
                winner = 0
            if self._skill < other.get_skill():
                winner = 1
        return winner


class Knight(Archer):
    def __init__(self, name, skill, weapon, belong, group=None):
        Orc.__init__(self, name, skill, weapon)
        self._weapon = weapon
        self._belong = belong
        self._group = group
        if self._weapon is None:
            print('We need a weapon!')
    
    def get_belong(self):
        return self._belong

    def set_belong(self, belong):
        self._belong = belong

    def get_group(self):
        return self._group

    def set_group(self, group):
        self._group = group

    def __str__(self):
        return 'name: %s, skill: %d, weapon: %s, belongs to: %s' % (self._name, self._skill, self._weapon, self._belong)

    def __gt__(self, other):
        winner = 2
        if other.get_name() != 'Orc':
            print('Error! You should fight against an orc.')
            return 3

        if other.get_weapon() is None:
            winner = 2
        else:
            if self._skill > other.get_skill():
                winner = 0
            if self._skill < other.get_skill():
                winner = 1
        return winner


    




