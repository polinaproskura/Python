length = input()
while length > 0 :
    day_1 = input()
    hour_1 = input()
    minutes_1 = input()
    seconds_1 = input()
    day_2 = input()
    hour_2 = input()
    minutes_2 = input()
    seconds_2 = input()
    number_1 = ((day_1 * 24 + hour_1) * 60 + minutes_1) * 60 +seconds_1
    number_2 = ((day_2 * 24 + hour_2) * 60 + minutes_2) * 60 +seconds_2
    number = number_2 - number_1
    seconds = number % 60
    number = number // 60
    minutes = number % 60
    number = number // 60
    hours = number % 24
    number = number // 24
    s = '(' + str(number) + ' ' + str(hours) + ' ' + str(minutes) + ' ' + str(seconds) + ')'
    print(s)
    length = length - 1
