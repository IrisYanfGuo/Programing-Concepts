def smallest2(alist):
    smalllest = 10000000
    smallestPos = -1
    i = 0
    for value in alist:
        if value<smalllest:
            smalllest = value
            smallestPos = i
        i = i + 1
    return smalllest,smallestPos


def smallest3(alist):
    smalllest = 10000000
    smallestPos = -1
    i = 0
    for pos,value in enumerate(alist):
        if value<smalllest:
            smalllest = value
            smallestPos = pos
    return smalllest,smallestPos

print(smallest3([2,4,5,7,9,1]))