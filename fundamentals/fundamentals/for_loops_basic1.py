# 1 Basic
for basic in range(0,150):
    print(basic)

# 2 Multiples of Five
for mult5 in range(0, 1001, 5):
    print(mult5)

for mult5 in range(0,1001):
    if(mult5%5 == 0):
        print(mult5)

# 3 Count, the Dojo Way
for mult in range(1, 101):
    if(mult%10 == 0):
        print("Coding Dojo")
    elif (mult%5 == 0):
        print("Coding")
    else:
        print(mult)

# 4 Whoa, that sucker's huge
    sum = 0
for count in range(0, 500000):
    if(count%2 == 1):
        sum += count
print(sum)

# 5 Countdown by fours
for countdown in range(2018, 0, -4):
    print(countdown)

# 6 Flexible Counter
lowNum = 2
highNum = 9
mult = 3
for counter in range(lowNum, highNum+1):
    if(counter%mult == 0):
        print(counter)
