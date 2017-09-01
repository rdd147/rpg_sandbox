

class Monster(object):
    def __init__(self, level):
        self.level = level
        self.attack_stat
        self.defense_stat
        print 'Genric Pokemon construction completed!'

    def attack(self):
        print 'Monster attacked!'

    def talk(self):
        raise NotImplementedError

class Water_monster(Monster):
    def __init__(self, level):
        self.attack_stat = level*1.1
        self.defense_stat = level*1.2

    def talk(self):
        print 'Water_monster!!!'

class Fire_monster(Monster):
    def __init__(self, level):
        self.attack_stat = level*1.2
        self.defense_stat = level*1.1

    def blurb(self):
        print 'Fire!!!'