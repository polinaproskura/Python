length = input()
while length > 0 :
    x1 = input()
    y1 = input()
    x2 = input()
    y2 = input()
    k = (y2 - y1)/(x2 - x1)
    b = y1 - k * x1
    s = '(' + str(k) + ' ' + str(b) + ')'
    print(s)
    length = length - 1
