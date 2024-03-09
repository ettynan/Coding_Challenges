'''Write a program to check if a number is positive, negative, or zero'''

def check_num(num):
    if num == 0:
        result = 'zero'
    elif num < 0:
        result = 'negative'
    else:
        result = 'positive'
    return result

if __name__ == "__main__":
    result = print(check_num(-1))
    result = print(check_num(0))
    result = print(check_num(1))
    result = print(check_num(-0.5))

