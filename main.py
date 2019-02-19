import numpy as np
from random import randint


def montyhall():
    _w = 0
    _l = 0
    _sw = 0

    for _i in range(50000):
        _doors = np.array([1, 0, 0])
        np.random.shuffle(_doors)
        _choice = randint(0, 2)
        _switch = randint(0, 1)

        for _d in range(len(_doors)):
            if _doors[_d] != 1 and _choice != _d:
                _opendoor = _d
                break

        if _switch == 1:
            _sw += 1
            for _s in range(len(_doors)):
                if _opendoor != _s and _choice != _s:
                    _choice = _s
                    break

        if _doors[_choice] == 1:
            _w += 1
        else:
            _l += 1

    print('Switch->',_sw)
    print("Number of win->", _w)
    print('Number of loses->', _l)


if __name__ == '__main__':

    montyhall()

    exit()