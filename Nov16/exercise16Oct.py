from math import *

# 1.list compresion
# 1.1
mylist = [1, -1, 3, -5]

alist = [abs(x) for x in mylist]
blist = [x for x in mylist if x > 0]
print(blist)

mylist2 = [1, 0, 3, 0]
list2 = [x if x != 0 else -1 for x in mylist2]
list22 = [-1 if x==0 else x for x in mylist2]
print(list2)
print(list22)

# 4
mylist3 = ['a', 'b', 'c']
dlist = [x.upper() for x in mylist3]

# 5
elist = [pow(x, 2) for x in range(1, 11)]
print(elist)

# 6
mylist6 = [[], [0, 1, 2], [], [3, 6, 7, 21]]
flist = [x for x in mylist6 if len(x) > 0]
print(flist)

# 7
mylist7 = ['hello', 'me']
list7 = [(x, len(x)) for x in mylist7]
print(list7)

# 8
mylist8 = [10, 1, 2, 100, 200]
list8 = [x if x % 10 != 0 else 0 for x in mylist8]
print(list8)

# 9
mylist91 = ['apple', 'pie']
mylist92 = [6, 7, 8, 9, 10]
list9 = [(x, y) for x in mylist91 for y in mylist92]
print(list9)

# 10
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]


x = list(zip(a,b))
y = [(a[i],b[i]) for i in range(len(a)) ]
print(x)
print(y)
