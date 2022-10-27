# Name: Xiaoteng Zhang
# McGill ID: 260895923
import math
PIZZA_CAKE_COST_PER_CENTIMETRE_CUBED = 4.0
PIZZA_POUTINE_COST_PER_CENTIMETRE_CUBED = 3.0
PECIAL_INGREDIENT = "guacamole"
SPECIAL_INGREDIENT_COST = 19.99
FAIR = True 

def get_pizza_area(diameter):
    ''' (float) -> float
    This function returns pizza's area after taking diameter as an input.
    Note the diameter inputted needs to be positive float for the result to
    make sense.
    >>> get_pizza_area(2)
    3.141592653589793
    >>> get_pizza_area(3.5)
    9.62112750161874
    >>> get_pizza_area(0)
    0.0
    '''
    area = math.pi * pow(diameter/2,2)
    return area


def get_fair_quantity(diameter1, diameter2):
    '''(float, float) -> int
    This function takes in two inputted diameters to calculate the minimum #
    of small pizzas that must be order to get at least the same amount as the
    larger pizza. The calculation method would vary based on if we set FAIR variable
    as True/False. There is no restriction as to which input should be the bigger one
    of the two. 
    Again, we note that in order for the result to make sense, we must keep two inputted
    floats positive. 
    
    First two examples are when FAIR = True
    >>> get_fair_quantity(10.0, 7.0)
    3
    >>> get_fair_quantity(2.5, 15.3)
    38
    Now the next two examples are when FAIR = False
    >>> get_fair_quantity(10.0, 7.0)
    3
    >>> get_fair_quantity(2.5, 15.3)
    56
    '''
    if FAIR: 
        if diameter1 < diameter2:
            amount = get_pizza_area(diameter2)/ get_pizza_area(diameter1)
            if amount == int(amount): # if the amount is integer 
                return amount
            else: 
                rounded_amount = int(amount+1)
                return rounded_amount 
        else:
            amount = get_pizza_area(diameter1)/ get_pizza_area(diameter2)
            if amount == int(amount): # if the amount is integer 
                return amount
            else: 
                rounded_amount = int(amount+1)
                return rounded_amount
    else:
        if diameter1 < diameter2:
            amount = int(1.5* (get_pizza_area(diameter2)/ get_pizza_area(diameter1)))
            return amount
        else:
            amount = int(1.5* (get_pizza_area(diameter1)/ get_pizza_area(diameter2)))
            return amount
    


def pizza_formula(d_large, d_small, c_large, c_small, n_small):
    '''(float, float, float, float, int) -> float
    This function calculates the missing value that is labeled using -1 from
    the other four floats user inputted. This calculated value is then rounded
    2 demical places. Note that of the five inputs, only one of them is allowed
    to be labeled as -1 otherwise error might arise.
    Similar to the other two functions: in order for the output to make sense, we
    must input positive floats and integer.
    
    
    >>> pizza_formula(-1 , 8.0 , 9.55, 12.47, 4)
    14.0
    >>> pizza_formula(14.0 , -1 , 9.55, 12.47, 4)
    8.0
    >>> pizza_formula(14.0 , 8.0 , -1 , 12.47, 4)
    9.55
    >>> pizza_formula(12.0, 6.0, 10.0, 5.0 , -1)
    2.0 
    '''
    if d_large == -1:
        small_area = n_small * get_pizza_area(d_small)
        big_area = (c_large* small_area)/(c_small)
        real_diameter_big = round(2* math.sqrt((big_area)/math.pi),2)
        return real_diameter_big
    elif d_small == -1:
        big_area = get_pizza_area(d_large)
        small_area_per_pizza = ((c_small* big_area)/(c_large))/n_small
        real_diameter_small = round(2* math.sqrt((small_area_per_pizza)/math.pi),2)
        return real_diameter_small
    elif c_large == -1:
        small_area = n_small * get_pizza_area(d_small)
        big_area = get_pizza_area(d_large)
        real_cost_large = round((c_small * big_area)/(small_area),2)
        return real_cost_large
    elif c_small == -1:
        small_area = n_small * get_pizza_area(d_small)
        big_area = get_pizza_area(d_large)
        real_cost_small = round((c_large * small_area)/(big_area),2)
        return real_cost_small
    elif n_small == -1:
        big_area = get_pizza_area(d_large)
        small_unit_area = get_pizza_area(d_small)
        real_n = round(((c_small* big_area)/(c_large))/small_unit_area,2)
        return real_n 



def get_pizza_cake_cost(base_diameter, height_per_level):
    '''(int, float) -> float
    This function will return the cost of a stack of pizza after taking two inputs.
    The output will also vary according to the value of FAIR variable.
    
    The following example is when FAIR is set as True:
    >>> get_pizza_cake_cost(3, 2.0)
    87.96
    >>> get_pizza_cake_cost(5, 1.0)
    172.79
    The following example is when FAIR is set as False:
    >>> get_pizza_cake_cost(3, 2.0)
    131.95
    '''
    total_cost = 0
    for i in range(base_diameter):
        price_per_level= PIZZA_CAKE_COST_PER_CENTIMETRE_CUBED* (get_pizza_area(base_diameter-i)*height_per_level)
        total_cost = total_cost + price_per_level
    total_cost_final_true = round(total_cost,2) 
    total_cost_final_false = round(1.5*total_cost,2)
    if FAIR:
        return total_cost_final_true
    else:
        return total_cost_final_false


def get_pizza_poutine_cost(diameter, height):
    '''(int, float) -> float
    This function will return the cost of a pizze poutine after specifying diameter and height
    The output will vary according to the value of FAIR variable.
    
    The following example is when FAIR is set as True:
    >>> get_pizza_poutine_cost(3, 5.0)
    106.03
    >>> get_pizza_poutine_cost(5, 1.0)
    58.9
    The following example is when FAIR is set as False:
    >>> get_pizza_poutine_cost(3, 5.0)
    159.04
    '''
    total_cost = (get_pizza_area(diameter)*height)*PIZZA_POUTINE_COST_PER_CENTIMETRE_CUBED
    total_cost_final_true = round(total_cost,2) 
    total_cost_final_false = round(1.5*total_cost,2)
    if FAIR:
        return total_cost_final_true
    else:
        return total_cost_final_false
    
    
def display_welcome_menu():
    ''' () -> ...
    This function simply displays a message (The content of the message will be specified below)
    
    >>> display_welcome_menu()
    Welcome to our pizza place. We guarantee 100 percent customer satisfaction !
    Please choos an option
    A. Special Orders
    B. Formula Mode
    C. Quantity Mode
    '''
    print('Welcome to our pizza place. We guarantee 100 percent customer satisfaction !')
    print('Please choos an option')
    print('A. Special Orders')
    print('B. Formula Mode')
    print('C. Quantity Mode')
    

def special_orders():
    '''() -> ... 
    This function asks the user to input several different choices print out a statement
    containing the total cost. Additonally, if the user's input is not either cake or poutine,
    a message will be printed
    
    >>>special_orders()
       Would you like the cake or poutine? cake
       Enter diameter: 3
       Enter height: 2.0
       Do you want the guacamole? yes
       The cost is $107.94999999999999
       
    >>>special_orders()
       Would you like the cake or poutine? poutine
       Enter diameter: 3
       Enter height: 5.0
       Do you want the guacamole? no
       The cost is $106.03
       
    >>>special_orders()
       Would you like the cake or poutine? poutine
       Enter diameter: 3
       Enter height: 5.0
       Do you want the guacamole? yes
       The cost is $126.02
    '''
    type_of_order = input('Would you like the cake or poutine:')
    diameter = int(input('Enter diameter:'))
    height = float(input('Enter height:'))
    guaca = input('Do you want the guacamole ?')
    
    if type_of_order == 'cake':
        if guaca == 'yes' or guaca =='y':
            total_cost = get_pizza_cake_cost(diameter, height) + SPECIAL_INGREDIENT_COST
            print ('The cost is $'+ str(total_cost)) 
        else:
            total_cost = get_pizza_cake_cost(diameter, height)
            print ('The cost is $'+ str(total_cost)) 
    elif type_of_order == 'poutine':
        if guaca == 'yes' or guaca =='y':
            total_cost = get_pizza_poutine_cost(diameter, height) + SPECIAL_INGREDIENT_COST
            print ('The cost is $'+ str(total_cost)) 
        else:
            total_cost = get_pizza_poutine_cost(diameter, height)
            print ('The cost is $'+ str(total_cost)) 
    else :
        print ('You can only select between cake and poutine, sorry !')
        

def quantity_mode():
    '''() -> ...
    This function asks user to enter the diameters of two pizzas and then prints out the amount
    that they need to buy to get the same amount of pizza. 
    
    >>> quantity_mode()
        Enter diameter 1: 10.0
        Enter diameter 2: 7.0
        You should buy 3 pizzas.
        
    >>> quantity_mode()
        Enter diameter 1: 2.5
        Enter diameter 2: 15.3
        You should buy 38 pizzas.
        
    >>> quantity_mode()
        Enter diameter 1: 11.0
        Enter diameter 2: 8.0
        You should buy 2 pizzas.
    '''
    d_1 = float(input('Enter diameter 1:'))
    d_2 = float(input('Enter diameter 2:'))
    result = get_fair_quantity(d_1,d_2)
    print('You should buy', str(result), 'pizzas.')
    

def formula_mode():
    '''() -> ...
    This function prints out the missing value labelled by -1 given the other 4 values that the user
    inputted. 
    
    >>> formula_mode()
        Enter large diameter: 12.0
        Enter small diameter: 6.0
        Enter large price: 10.0
        Enter small price: -1
        Enter small number: 2
        The missing value is: 5.
        
    >>> formula_mode()
        Enter large diameter: 14.0
        Enter small diameter: 8.0
        Enter large price: -1
        Enter small price: 12.47
        Enter small number: 4
        The missing value is: 9.55.
        
    >>> formula_mode()
        Enter large diameter: 12.0
        Enter small diameter: 6.0
        Enter large price: 10.0
        Enter small price: 5.0
        Enter small number: -1
        The missing value is: 2.0.
    '''
    d_large = float(input('Enter large diameter:'))
    d_small = float(input('Enter small diameter:'))
    c_large = float(input('Enter large price:'))
    c_small = float(input('Enter small price:'))
    n_small = int(input('Enter small number:'))
    result = pizza_formula(d_large, d_small, c_large, c_small, n_small)
    print('The missing value is:', str(result))
    
    
def run_pizza_calculator():
    '''() -> ...
    This function displays a welcome message and lets the user choose an option,
    and then calls the appropriate function. If the user inputs an invalid option
    a message will be printed out.
    
    >>>run_pizza_calculator()
       Welcome to our pizza place. We guarantee 100 percent customer satisfaction !
       Please choose an option:
       A. Special Orders
       B. Formula Mode
       C. Quantity Mode    
       Your choice: A
       Would you like the cake or poutine? cake
       Enter diameter: 2
       Enter height: 1.0
       Do you want the guacamole? yes
       The cost is $35.7
       
    >>>run_pizza_calculator()
       Welcome to our pizza place. We guarantee 100 percent customer satisfaction !
       Please choose an option:
       A. Special Orders
       B. Formula Mode
       C. Quantity Mode    
       Your choice: E
       Invalid mode. 
    
    >>>run_pizza_calculator()
       Welcome to our pizza place. We guarantee 100 percent customer satisfaction !
       Please choose an option:
       A. Special Orders
       B. Formula Mode
       C. Quantity Mode
       Your choice: C
       Enter diameter 1:10.0
       Enter diameter 2:7.0
       You should buy 3 pizzas.
    '''
    display_welcome_menu()
    choice = input('Your choice:')
    if choice == 'A':
        special_orders()
    elif choice == 'B':
        formula_mode()
    elif choice == 'C':
        quantity_mode()
    else:
        print('Invalid mode.')
        
