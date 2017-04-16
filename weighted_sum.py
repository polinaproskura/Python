length = input()
while length > 0 :
    a = input()
    s = 0
    sum_ost = 0
    while a > 0 :
        sum_ost = sum_ost + a % 10
        s = s + sum_ost
        a = a // 10
    print(s)
    length = length - 1
