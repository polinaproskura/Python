length = input()
while length > 0 :
    a = input()
    b = input()
    c = input()
    k = 1
    if (a + b < c or a + c < b or c + b < a):
        k = 0
    print(k)
    length = length - 1
