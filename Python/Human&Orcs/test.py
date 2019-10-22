from Orcs import Orc
import shelve


def to_file(orc):
    if orc is None:
        return 0
    file_name = 'Orc: ' + orc.get_name()
    db = shelve.open(file_name)
    instance = orc
    db[orc.get_name()] = instance
    db.close()


a = Orc('Ziyan', 2, 3)
b = Orc("ZhongQi", 2, 3)
result = a.attack(b)
to_file(result)
