a = int(input())
b = int(input())
c = int(input())
if (a>b and a>c):
    if (b>c):
        print(b)
    else:
        print(c)
if (b>a and b>c):
    if (a>c):
        print(a)
    else:
        print(c)
if (c>a and c>b):
    if (a>b):
        print(a)
    else:
        print(b)
