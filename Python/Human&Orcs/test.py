from Orcs import *
import shelve


def to_file(obj):
    if obj is None:
        return 0
    file_name = obj.__class__.__name__ + obj.get_name
    db = shelve.open(file_name)
    instance = obj
    db[obj.get_name] = instance
    db.close()


a1 = Archer('z', 12, 'Ireland', True)
a2 = Archer('a', 11, 'UK', True)
o1 = Orc('o1', 9, 10)
o2 = Orc('o2', 8, 11, True)
team = [a1, a2]
k1 = Knight('b', 22, 'Ireland', team, True)
k2 = Knight('d', 12, 'UK', team, True)
print(k1)
o1.attack(o2)
winner = k1.attack(o1)
to_file(winner)
k1.attack(k2)
