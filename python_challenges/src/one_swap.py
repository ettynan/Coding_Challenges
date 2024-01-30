'''Create a program that swaps the value of two variables'''
def swap(var1, var2):
    print(var1, var2)
    var1, var2 = var2, var1
    print(var1, var2)
var1 = 7
var2 = 2
swap(var1, var2)
