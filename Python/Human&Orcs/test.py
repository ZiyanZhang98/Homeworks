from Orcs import Orc, Human, Archer, Knight
import shelve


def to_file(obj):
    if obj is None:
        return 0
    file_name = obj.get_class_name() + obj.get_name()
    db = shelve.open(file_name)
    instance = obj
    db[obj.get_name()] = instance
    db.close()


a1 = Archer('z', 12, 'Ireland', True)
a2 = Archer('a', 11, 'UK', True)
o1 = Orc('o1', 9, 10)
o2 = Orc('o2', 8, 11, True)
team = [a1, a2]
k1 = Knight('b', 22, 'Ireland', team, True)
k2 = Knight('d', 12, 'UK', team)
o1.attack(o2)
a1.attack(o1)
k1.attack(o2)
k1.attack(a1)
