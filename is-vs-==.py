# == tests equality
# is test identity

l1 = [1,2,3,4]
l2 = [1,2,3,4]

print(l1 == l2) # True
print(l1 is l2) # False

l3 = l1
l1[0] = 5

print(l1 == l3) # True
print(l1 is l3) # True
print(l1, id(l1))       # [5, 2, 3, 4] 2391232377608
print(l3, id(l3))       # [5, 2, 3, 4] 2391232377608