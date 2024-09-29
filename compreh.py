import random

l1: list[int] = []
for i in range (11):
    l1.append(i)
print (f"l1: {l1}")

l2: list [int] = [i for i in range (11)]
print (f"l2: {l2}")

l3: list [int] = [i**2 for i in range (11)]
print (f"l3: {l3}")

l4: list [int] = [i for i in range (2,21,2)]
print (f"l4: {l4}")

l5: list [int] = [i for i in range (99,59, -3)]
print (f"l5: {l5}")

l6: list [int] = [random.randint (1,101)for _ in range(10)]
print (f"l6: {l6}")

l7: list [int] = [int(input("enter a number: ")) for _ in range (3)]
print (f"l7: {l7}")

sentinel: int = int(input("enter a number: "))
l8: list [int] = [i for i in range (21) if i != sentinel]
print (f"l8: {l8}")

#exc.a
l9: list [int] = [random.randint(-50,+50) for _ in range (10)]
print (f"l9: {l9}") # -- to check
#exc. b
l10: list [int] = [i for i in l9 if i%2==0 ]
print (f"l10: {l10}") # -- to check
#exc.c
l11: list[int] = [i for i in l9 if i%2 !=0]
print (f"l11: {l11}") # -- to check

