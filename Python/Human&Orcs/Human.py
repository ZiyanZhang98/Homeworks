class Human:
    def __init__(self, name, skill, belong, weapon=None):
        if skill < 0:
            print('Skill should be a positive number!')
            exit()
        if weapon is not True:
            print('We need a weapon!')
            exit()
        self._name = name
        self._skill = skill
        self._belong = belong
        self._weapon = weapon
        self._belong = belong

    @property
    def get_name(self):
        return self._name

    @property
    def get_skill(self):
        return self._skill

    @property
    def get_belong(self):
        return self._belong

    @property
    def get_weapon(self):
        return self._weapon

    @get_name.setter
    def set_name(self, name):
        self._name = name

    @get_skill.setter
    def set_skill(self, skill):
        if skill < 0:
            print('Skill should be a positive number!')
            exit()
        self._skill = skill

    @get_belong.setter
    def set_belong(self, belong):
        self._belong = belong

    @get_weapon.setter
    def set_weapon(self, weapon):
        self._weapon = weapon

    def __str__(self):
        return 'name: %s, skill: %d, weapon: %s, belongs to: %s' % (self._name, self._skill, self._weapon, self._belong)

    def __gt__(self, other):
        winner = 2
        if other.__class__.__name__ != 'Orc':
            print('Error! You should fight against an orc.')
            exit()
        if other.get_weapon is not True:
            winner = 0
        else:
            if self._skill > other.get_skill:
                winner = 0
            if self._skill < other.get_skill:
                winner = 1
        return winner

    def attack(self, other):
        result = self > other
        if result == 0:
            print('winner is %s' % self._name)
            self._skill = self._skill*1.05
            return self
        elif result == 1:
            print('winner is %s' % other.get_name)
            other._skill = 1.05 * other.get_skill
            return other
        else:
            print('They both loose')
            return None


class Archer(Human):
    def __init__(self, name, skill, belong, weapon=None):
        Human.__init__(self, name, skill, belong, weapon)


class Knight(Human):
    def __init__(self, name, skill, belong, t=None, weapon=None):
        Human.__init__(self, name, skill, belong, weapon)
        self._team = t

    @property
    def get_team(self):
        return_str = ''
        if self._team is not None:
            for member in self._team:
                return_str += (' '+member.get_name)
        return return_str

    @get_team.setter
    def set_team(self, sets):
        if sets is None:
            self._team = []
        self._team = sets

    def dismiss(self, archer):
        if archer in self._team:
            self._team.remove(archer)
        else:
            print('No such archer in the team!')

    def append_to_team(self, archer):
        self._team.append(archer)

    def __str__(self):
        team = 'Team member:'
        if len(self._team) == 0:
            team += 'None'
        else:
            for member in self._team:
                team += (' '+member.get_name)
        return 'name: %s, skill: %d, belong: %s, weapon: %s, %s' % (self._name, self._skill, self._belong, self._weapon, team)