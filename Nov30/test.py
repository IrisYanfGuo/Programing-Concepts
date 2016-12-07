from re import *




def colNameToInt( name):
    s = 0
    for i in range(len(name)):
        s += (ord(name[i]) - 65)*pow(26,i)
    return s

# finally right
# 整理，整理进制转换的方法，举一反三
# 任意进制转换的方法
def int_col(num):
    result=[]

    while(num//26>0):
        a = num % 26
        num = num//26-1
        result.append(chr(a+65))
    result.append(chr(num+65))
    tmp =""
    for i in range(len(result)-1,-1,-1):
        tmp+=result[i]
    return tmp






input = "=sum(AA1:BBBB2)"

p1= compile('[A-Z]+[1-9]\:')

p2 = compile('[A-Z]+')

matches1 = p1.finditer(input)
matches2 = p2.finditer(input)


result =[]
for match in list(matches2):
    result.append(input[match.start():match.end()])
print(result)


num =[]
for i in result:
    num.append(colNameToInt(i))

for i in num:
    result.append(int_col(i))
print(result)

print(colNameToInt("A"))


print(int_col(25))
print(int_col(26))
print(int_col(27))
print(int_col(28))
print(int_col(29))




# num is a string
def transtoDecimal(num,j):
    result=0
    for i in range(len(num)):
        result+=int(num[i])*pow(j,i)
    return result

print(transtoDecimal('12234',10))