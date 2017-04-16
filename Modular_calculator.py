c = "#"
number = input()
s = number
while c != "%" :
    c = input()
    number = input()
    if c == "*" :
        s = s * number
    if c == "+" :
        s = s + number
s = s % number
print(s)
