def int_to_negabinary(i):
    """
    convert integers numbers to a negative-base binary system
    """
    ds = []
    while i != 0:
        ds.append(i & 1)
        i = -(i >> 1)
    return ''.join(str(d) for d in reversed(ds)) if ds else '0'


def negabinary_to_int(s):
    """
    convert integers numbers from a negative-base binary system
    """
    i = 0
    for c in s:
        i = -(i << 1) + int(c)
    return i
