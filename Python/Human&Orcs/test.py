from Orcs import Orc, Archer, Knight
import shelve


def to_file(obj):
    if obj is None:
        return 0
    file_name = obj.get_class_name() + obj.get_name()
    db = shelve.open(file_name)
    instance = obj
    db[obj.get_name()] = instance
    db.close()


a = Orc('Ziyan', 2, 3)
b = Orc("ZhongQi", 2, 3)
result = a.attack(b)
to_file(result)
