a = int(input())
b = int(input())
c = int(input())

if c < 0 or (a == 0 and b ** 0.5 != c):
    print('NO SOLUTION')
elif a == 0 and b ** 0.5 == c:
    print('MANY SOLUTIONS')
else:
    x = (c ** 2 - b) / a
    if x == int(x):
        print(int(x))
    else:
        print('NO SOLUTION')


