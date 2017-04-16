length = input()
while length > 0 :
    a = input()
    b = input()
    c = input()
    c = c + a * b
    s = 0
    while c > 0 :
        s = s + (c % 10)
        c = c // 10
    print(s)
    length = length - 1
