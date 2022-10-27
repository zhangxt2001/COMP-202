# Name: Xiaoteng Zhang
# McGill ID: 260895923
MOVEMENT_SYMBOLS = '><v^'
EMPTY_SYMBOL = '.'
TREASURE_SYMBOL = '+'
BREADCRUMB_SYMBOL = 'X'
MOVEMENT_SYMBOLS_3D = '*|'

def get_nth_row_from_map(s,n,w,h):
    '''(str,int,int,int)->str
This function returns n'th row of the treasure map (string s), with 0th row
representing the first row. If the n'th row is out of bound then we would
return instead an empty string ''. The function also implicitly assumes that
user verifys len(s) = w*h (basic requirement for a 2d treasure map.
>>>  get_nth_row_from_map('..vv.<>..', 1, 3, 3)
'v.<'
>>>  get_nth_row_from_map('..vv.<>..', 3, 3, 3)
''
>>> get_nth_row_from_map('..v>..v.<>..', 2, 3, 4)
'v.<'
'''
    if n > h-1:
        return ''
    else:
        index_upper = (n+1)*w
        index_lower = n*w
        return(s[index_lower:index_upper])
        
def print_treasure_map(s,w,h):
    '''(str,int,int)->...
This function takes a treasure map string s along with width and height to print
out a treasure map with each row on its own line. The function also implicitly assumes
that user verifys len(s) = w*h (basic requirement for a 2d treasure map.

>>>  print_treasure_map('^..>>>..', 2, 4)
^.
.>
>>
..
>>>  print_treasure_map('^..>>>..v', 3, 3)
^..
>>>
..v
>>>  print_treasure_map('....v.', 2, 3)
..
..
v.
'''
    for i in range(0,w*h,w):
        print(s[i:i+w])

def change_char_in_map(s,i_row,i_column,char,width,height):
    '''(str,int,int,str,int,int)-> str
This function returns a treasure map with a specific character replaced by the new
character user inputs. When  either or both of the indices are out of bounds of the
map, return the input string unchanged.
>>>  change_char_in_map('.........', 1, 1, 'X', 4, 3)
'.....X...'
>>>  change_char_in_map('....v.', 1, 1, 'T', 2, 3)
'...Tv.'
>>>  change_char_in_map('....v.', 100, 1, 'T', 2, 3)
'....v.'
'''
    if i_row > height - 1 or i_column > width - 1:
        return s
    else:
        s_new = ''
        replace_index = width * i_row + i_column
        for i in range(len(s)):
            if i != replace_index:
                s_new += s[i]
            elif i == replace_index:
                s_new += char
        return s_new
        
def get_proportion_travelled(s):
    '''(str)->float
This function takes in a string and returns of the proportion of X contained in the string by
first counting its number and then divide that number by the len(s). The returned float is rounded
to two decimal places (between 0 and 1)
>>> get_proportion_travelled('.X.')
0.33
>>> get_proportion_travelled('.X...')
0.2
>>> get_proportion_travelled('.X..X..')
0.29
'''
    i = 0
    counter = 0
    while i <= len(s)-1:
        if s[i] == BREADCRUMB_SYMBOL:
            counter += 1
        i += 1
    proportion = counter / len(s)
    return round(proportion,2)
     
def get_nth_map_from_3D_map(s,n,width,height,depth):
    '''(str,int,int,int,int)->str
This function return n'th map of the 3D treasure map given the user input n, but it returns
an empty string '' when map index is out of bound.
>>>  get_nth_map_from_3D_map('^..>>>..', 1, 2, 2, 2)
'>>..'
>>>  get_nth_map_from_3D_map('..vv.<>..><>', 1, 3, 2, 2)
'>..><>'
>>>  get_nth_map_from_3D_map('..vv.<>..><>', 5, 3, 2, 2)
''
'''
    if n > depth-1:
        return ''
    else:
        num_charac = width * height
        n_th_map = s[n*(num_charac):(n+1)*(num_charac)]
        return n_th_map

def print_3D_treasure_map(s,width,height,depth):
    '''(str,int,int,int)->...
This function takes a 3D treasure map string and then prints out the treasure map with each row its
own line with the neighboring two blocks separated by a blank line. It does not contain a blank line
at the very end.
>>> print_3D_treasure_map('.X.XXX.X..v.vXv.v.', 3, 2, 3)
.X.
XXX

.X.
.v.

vXv
.v.
>>> print_3D_treasure_map('.X.XXX.X..v.vXv.v.', 2, 3, 3)
.X
.X
XX

.X
..
v.

vX
v.
v.
>>> print_3D_treasure_map('..vv.<>..><>', 2, 2, 3)
..
vv

.<
>.

.>
<>

'''
    i = 0
    while i < depth-1:
        i_th_map = get_nth_map_from_3D_map(s,i,width,height,depth)
        print_treasure_map(i_th_map,width,height)
        print()
        i += 1
    last_map = get_nth_map_from_3D_map(s,i,width,height,depth)
    print_treasure_map(last_map,width,height)


def change_char_in_3D_map(s,i_row,i_col,n_depth,char,width,height,depth):
    '''(str,int,int,int,str,int,int,int)->str
Returning a new string with a specified character replaced by the new character
that user specifies. If any one of the parameters is out of bound, the original
string is returned.
>>> change_char_in_3D_map('..vv.<>..><>', 1, 0, 0, '#', 3, 2, 2)
'..v#.<>..><>'
>>> change_char_in_3D_map('..vv.<>..><>', 0, 0, 1, '#', 3, 2, 2)
'..vv.<#..><>'
>>> change_char_in_3D_map('..vv.<>..><>', 2, 1, 1, '#', 3, 2, 2)
'..vv.<>..><>'
'''
    new_s = ''
    if i_row > height - 1 or i_col > width - 1 or n_depth > depth -1:
        return s
    else:
        n_th_map = get_nth_map_from_3D_map(s,n_depth,width,height,depth)
        n_th_map_changed = change_char_in_map(n_th_map,i_row,i_col,char,width,height)
        for n in range(n_depth):
            new_s += get_nth_map_from_3D_map(s,n,width,height,depth)
        new_s += n_th_map_changed
        for n_second in range(n_depth+1,depth):
            new_s += get_nth_map_from_3D_map(s,n_second,width,height,depth)
        return new_s
        