def func(a,b=[]):
    b.append(a)
    return b
print(func(1))
print(func(2))
print(func(3))



list1 = [1, 2, 3]
list2 = list1
list2.append(4)
print(list2)
print(list1)

a = [1, 2, 3, 2, 4, 2]
for i in a:
    if i == 2:
        a.remove(i)
print(a)