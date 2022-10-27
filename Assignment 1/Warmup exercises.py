# Warmup questions for assignment 1

# Question 1:
 # 13 in base 5 would be 23
 # 13 in base 2 would be 1101
 # 11010010 in base 10 would be 210


# Question 2:
# 1. That expression will be evaluated to false by short
# circuit evaluation
# 2. This will always be evaluated to True because b will
# always have to false for the starter, but then the last
# part will not be evaluated to false, which will make the
# entire expression impossible to be false.

# Question 3
def even_and_positive():
    number = input('Please enter a number:')
    print(number, 'is an even number', int(number)%2 == 0)
    print(number, 'is an even number', int(number) > 0)
    print(number, 'is an even number', int(number)%2 == 0 and int(number) > 0 )
    

# Question 4
def hello_bye():
    number = input('Choose a number:')
    if number == '0':   # if two types are different then automatically false 0 == '0'
        print("Bye Bye!")
    elif number == '1':
        print("Hello everyone !")
    else:
        print("Bye Bye!")

# Question 7
def compare_x_y_z(x, y, z):
    return z == 3 or z == x+y
        
# Question 8
def calculation(x, y, op):
    if op == '+':
        return x+y
    elif op == '*':
        return x*y
    else:
        return 0 
