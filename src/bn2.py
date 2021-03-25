import constants


def bn2():
    return """
{0}
```py
def int_to_negabinary(i):
    ds = []
    while i != 0:
        ds.append(i & 1)
        i = -(i >> 1)
    return ''.join(str(d) for d in reversed(ds)) if ds else '0'
```
```py
def int_to_negabinary(i):
    ds = []
    while i != 0:
        ds.append(i & 1)
        i = -(i >> 1)
    return ''.join(str(d) for d in reversed(ds)) if ds else '0'
```
    """.format(constants.bn2.description_bn2)


def int_to_negabinary():
    return """
{0}
```py
def int_to_negabinary(i):
    ds = []
    while i != 0:
        ds.append(i & 1)
        i = -(i >> 1)
    return ''.join(str(d) for d in reversed(ds)) if ds else '0'
```
    """.format(constants.bn2.description_int_to_nb)


def negabinary_to_int():
    return """
{0}
```py
def negabinary_to_int(s):
    i = 0
    for c in s:
        i = -(i << 1) + int(c)
    return i
```
    """.format(constants.bn2.description_nb_to_int)
