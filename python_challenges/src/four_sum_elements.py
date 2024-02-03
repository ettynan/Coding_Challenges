'''Write a program to find the sum of all elements in a list'''

num_list = [1, 3, 5, 7, 9]
def sum_list(num_list):
    sum = 0
    for i in range(len(num_list)):
        sum = sum + num_list[i]
    return sum

print(sum_list(num_list))
