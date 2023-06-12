#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2 or len(tuple_b) < 2:
        if len(tuple_a) == 0:
            tuple_a = (0, 0)
        elif len(tuple_a) == 1:
            tuple_a = (tuple_a[0], 0)

        if len(tuple_b) == 0:
            tuple_b = (0, 0)
        elif len(tuple_b) == 1:
            tuple_b = (tuple_b[0], 0)

    a0, a1 = tuple_a[0], tuple_a[1]
    b0, b1 = tuple_b[0], tuple_b[1]

    t1 = a0 + b0
    t2 = a1 + b1

    return (t1, t2)
