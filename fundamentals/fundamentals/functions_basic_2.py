# 1 Countdown
def countdown (num):
    temp = []
    for count in range(num, -1, -1):
        temp.append(count)
    return temp

print(countdown(8))

# 2 Print and Return
def print_return(list):
    print(list[0])
    return list[1]

print(print_return([10,20]))


# 3 First Plus Length
def first_plus_length(list):
    return list[0] + len(list)

print(first_plus_length([2,5,4,3,7,8]))


# 4 Values greater than second
def values_greater(list):
    temp = []
    for i in list:
        if(i > list[1]):
            temp.append(i)
    return temp

print(values_greater([5,2,7,8,5,9,3,4,2]))

# 5 This length, that value
def length_value(size, value):
    list = []
    for x in range(1, size+1):
        list.append(value)
    return list

print(length_value(7, 4))