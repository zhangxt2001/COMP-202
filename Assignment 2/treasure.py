# Name: Xiaoteng Zhang
# McGill ID: 260895923
MOVEMENT_SYMBOLS = '><v^'
EMPTY_SYMBOL = '.'
TREASURE_SYMBOL = '+'
BREADCRUMB_SYMBOL = 'X'
MOVEMENT_SYMBOLS_3D = '*|'

import random

def generate_treasure_map_row(width, is_3D):
    '''(int,bool)->str
This function returns a string containing characters selecting from certain global
variable defined above with specified probability. If the boolean input is set to
True then one the characters will be replaced with 50 percent probability.
>>> random.seed(9991234)
>>> generate_treasure_map_row(10, True)
'>.>|.v∧..v'
>>> generate_treasure_map_row(10, False)
'∧∧>v∧>∧>..'
>>> generate_treasure_map_row(25, True)
'v<.><v>>v∧v<∧<<>..>∧<∧v<v'
'''
    string = ''
    for i in range(width):
        random_number = random.random()
        if random_number <= 5/6:
            string += MOVEMENT_SYMBOLS[random.randint(0,3)]
        else:
            string += EMPTY_SYMBOL
    if is_3D:
        replaced_string = ''
        random_num_two = random.random()
        random_index = random.randint(0,width-1)
        if random_num_two <= 1/2:
            for i in range(width):
                if i != random_index:
                    replaced_string += string[i]
                elif i == random_index:
                    replaced_string += MOVEMENT_SYMBOLS_3D[random.randint(0,1)]
            return replaced_string
        else:
            return string
    else:
        return string
            

def generate_treasure_map(width,height,is_3D):
    '''(int,int,bool)->str
This function returns a treasure map given width and height. User could also set the bool
value to true to generate a 3D treasure map. This function also makes sure that the first
character to be a right-pointing movement symbol.
>>> random.seed(9991234)
>>>  generate_treasure_map(9, 8, True)
'>.>>.v∧..v<<∧∧>v∧>∧>..<<>>∧..∧∧v>>.>>∧<.>∧<<<vv∧.>v∧<|<∧v∧>>.><<v<∧<.<∧>'
>>>  generate_treasure_map(5, 8, True)
'>∧<<.vv>.v∧vv<<∧>∧<..v∧.∧>v>∧<.<v>>v∧v<∧'
>>>  generate_treasure_map(5, 7, False)
'>>..>∧<∧v<v<<vvv<vv><vv><>.v>∧><v>>'
'''
    total_number = width*height
    treasure_map = generate_treasure_map_row(total_number, is_3D)
    final_map = '>'
    if treasure_map[0] == '>':
        return treasure_map
    else:
        for i in range(1,len(treasure_map)):
            final_map += treasure_map[i]
        return final_map
 
 
def generate_3D_treasure_map(width,height,depth):
    '''(int,int,int)->str
This function takes a positive integer width, height and depth as inputs and returns a 3D
treasure map. This function also makes sure that the first character to be a right-pointing
movement symbol.
>>> random.seed(9991234)
>>>  generate_3D_treasure_map(4, 6, 3)
'>∧v>>.>>∧<.>∧<<<vv∧.>v∧<><∧v∧>>.><<v<∧<.<∧>∧>v<<.vv>.v∧vv<<∧*∧<..v∧.∧>v>'
>>>  generate_3D_treasure_map(3, 6, 3)
'>v>>v∧v<∧<<>..>∧<∧v<v<<vvv<vv><vv><>.v>∧><v>>..∧v>>v<.'
>>>  generate_3D_treasure_map(3, 4, 3)
'>∧.∧<<v><.><<><>v><<<∧>.><∧>.v|.∧∧<<'
'''
    total_number = width*height*depth
    treasure_map = generate_treasure_map_row(total_number,True)
    final_map = '>'
    if treasure_map[0] == '>':
        return treasure_map
    else:
        for i in range(1,len(treasure_map)):
            final_map += treasure_map[i]
        return final_map

def change_char_advanced(s,replace_index,char):
    '''(str,int,str)->str
This function is an adapted version of the fucntion that I wrote under treasure_utils. I
will be using this function later on. It returns a new string with a specified index replaced
by what user inputs. 
>>> change_char_advanced('..vv.<>..',3,'$')
'..v$.<>..'
>>> change_char_advanced('..v>..v.<>..',5,'$')
'..v>.$v.<>..'
>>> change_char_advanced('..v>..v.<>..',2,'!')
'..!>..v.<>..'
'''
    s_new = ''
    for i in range(len(s)):
        if i != replace_index:
            s_new += s[i]
        elif i == replace_index:
            s_new += char
    return s_new



def follow_trail(s,i_row,i_col,i_depth,width,height,depth,num_to_travel):
    '''(str,int,int,int,int,int,int,int,int)-> str
This function 'follows' a string according to the rule specified in the document
and this function will return a string as well as printing two statements.
Note that the starting point will have to be a symbol other than ., because otherwise
nothing will happen.
>>> follow_trail('>.v>..v.<>..',0,0,0,3,2,2,5)
Treasures collected: 0
Symbols visited: 4
'X.X>..v.<>..'
>>> follow_trail('>.v>..+.<>..',0,2,1,3,2,2,6)
Treasures collected: 1
Symbols visited: 3
'>.v>..+.X>..'
>>> follow_trail('>.v>..v.<>.+',0,2,1,3,2,2,6)
Treasures collected: 1
Symbols visited: 6
'>.v>..X.XX.+'
'''
    per_map_number = width*height
    starting_index = i_depth * per_map_number + i_row*width + i_col
    
    counter = 0
    counter_treasure = 0
    current_action = ''
    while s[starting_index] != BREADCRUMB_SYMBOL and counter != num_to_travel:
        if s[starting_index] in MOVEMENT_SYMBOLS or s[starting_index] in MOVEMENT_SYMBOLS_3D:
            current_action = s[starting_index]
            s = change_char_advanced(s,starting_index,BREADCRUMB_SYMBOL)
        if current_action == '>':
            if i_col == width - 1:
                i_col = 0
            else:
                i_col += 1
        elif current_action == '<':
            if i_col == 0:
                i_col = width- 1
            else:
                i_col -= 1
        elif current_action == '∧':
            if i_row == 0:
                i_row = height - 1
            else:
                i_row -= 1
        elif current_action == 'v':
            if i_row == height - 1:
                i_row = 0
            else:
                i_row += 1
        elif current_action == '*':
            if i_depth == depth - 1:
                i_depth = 0
            else:
                i_depth += 1
        elif current_action == '|':
            if i_depth == 0:
                i_depth = depth -1
            else:
                i_depth -= 1
        starting_index = i_depth * per_map_number + i_row*width + i_col
        counter += 1
        if s[starting_index] == TREASURE_SYMBOL:
            counter_treasure += 1
    print('Treasures collected:', counter_treasure)
    print('Symbols visited:', counter)
    return s
    
        
        
        
        
        
        
        
        
        
        
            
    