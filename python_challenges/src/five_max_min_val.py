'''Write a program to find the maximum and minimum values in a list'''

def min_val(list):
    min = list[0]
    for i in list:
        if i < min:
            min = i
    return min

def max_val(list):
    max = list[0]
    for i in list:
        if i > max:
            max = i
    return max

list = [10,28,3,4,5]
print(min_val(list))
print(max_val(list))
