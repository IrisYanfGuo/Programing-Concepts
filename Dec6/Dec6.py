from functools import reduce
# lambda, map(), filter(), reduce().
# 1.a
b = list(map((lambda x: x ** 2), range(1, 11)))
bb = list(map((lambda x: x ** 2), range(1, 21)))
print(b)
print(bb)


# 2
def even(num):
    if num % 2 == 0:
        return True
    else:
        return False


c = list(filter(even, range(1, 11)))
cc = list(filter(even, range(1, 21)))
print(c)

# 3
d = list(map(lambda x: x ** 2, list(filter(even, range(1, 11)))))
dd = list(map(lambda x: x ** 2, range(1, 21)))
print(d)
print(dd)


# 4
def fing_longest_word(llist):
    t = len(llist[0])
    for i in range(len(llist) - 1):
        if t < len(llist[i + 1]):
            t = len(llist[i + 1])
    return t


print(fing_longest_word(["fdfgfd", "dfd", "fsfsfdfdsfdf", "d"]))


# 5

def fliter_long_words(mylist,n):
    a=filter(lambda x:len(x)<n,mylist)
    return list(a)

print(fliter_long_words(["fdjfkdjfkd","fdf","d"],2))

#6
'''
Represent a small bilingual lexicon as a Python dictionary in the following fashion {"merry":"god", "christmas":"jul",
"and":"och", "happy":gott", "new":"nytt", "year":"år"} and use it to translate your Christmas cards from English into Swedish.
Use the higher order function map() to write a function translate() that takes a list of English words and returns a
list of Swedish words.

'''
g ={"merry":"god","christmas":"jul",
"and":"och", "happy":"gott", "new":"nytt", "year":"år"}
def translate(dict,a):
    result =''

    result=list(map(lambda x:dict[x],a))
    return result


print(translate(g,["merry","christmas"]))
#c = list(map(lambda x:dict[x],g))


#7
llist=["merry","christmas"]
def length(a):
    result=[]
    for i in a:
        result.append(len(i))
    return result

print(length(llist))

leng=list(map(lambda x:len(x),llist))
print(leng)

print([len(i) for i in llist])

#8
#write a function max_in_list() that takes a list of numbers and returns the largest one.
def max(a,b):
    if a>b:
        return a
    else:
        return b
c=reduce(max,[1,2,3,4,5,2,79,8])
print(c)

# way 2 , directly
c = reduce(lambda x,y: x if x>y else y,[1,2,3,4,5,2,79,8])
print(c)