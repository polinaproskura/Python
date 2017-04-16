length = input()
while length > 0 :
    a = input()
    b = input()
    n = input()
    s = 0
    while n > 0 :
        s = s + a + n * b - b
        n = n - 1
    print(s)
    length = length - 1
