L1=[i for i in range(1,7)]
print(L1)
print(L1[-4])
print(L1[2:])
print(L1[2:4])

L2=[element for element in L1 if element%2==0]
print(L2)




list1 = [2,4,6,8,10,12,14,16,18,20]

print (list1[0:1],list1[5:7])

s=''.join(['x' for x in range(101)])
print(s)


list = [ [ ] ] * 5
print(list)
list[0].append(10)
print(list)
list[1].append(20)
print(list)
list.append(30)
print(list)


s={1,2,3,4,5}
print(type(s))

s=[1,2,3,4,5]
print(type(s))

s="123"
print(type(s))

s=123
print(type(s))


myList = [1, 5, 5, 5, 5, 1]
max = myList[0]
indexOfMax = 0
for i in range(1, len(myList)):
    if myList[i] > max:
        max = myList[i]
        indexOfMax = i
print(indexOfMax)


k=[1,2,3,4,5]
v=[1,2,3,4,5]
d=dict()
for i in range(len(k)):
    d[k[i]]=v[i]

print(d)

a=[1,2,3,4]
b=[1,2,3,4]
print((a==b))
print(a is b)



for i in range(-11,10,1):
    print(i,end="")

print("")
a=[1,2,3,4,5,6,7,8,9]
l=[i for i in a if{(i%2)==0}]
print(l)


l=tuple(l)
for i in l:
    print(i,end="")

print("")
print(i)


a=(1,2,3,4,5)

for i,a in enumerate(l):
    print((i,a))


d['abc']='def'
print(d)