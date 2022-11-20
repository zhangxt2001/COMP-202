# Author: Xiaoteng Zhang
# McGill ID: 260895923

def is_valid_image(n_list):
    '''(list<list<int>>)->bool
This function checks whether a given nested list satisfies the requirement
to be a PGM image matrix. If it satisfies the requirement, then the function
would return True, otherwise it will return false
>>> is_valid_image([[1, 2, 3], [4, 5, 6], [7, 8, 256]])
False
>>> is_valid_image([[3], [4, 5, 6], [7, 8, 9]])
False
>>> is_valid_image([[0,100000], [0, 0]])
False
'''
    for val in n_list:
        for subval in val:
            if type(subval) == str:
                return False
    length = len(n_list[0])
    for val in n_list:
        if len(val) != length:
            return False
        for num in val:
            if not (0<=int(num)<=255):
                return False
    return True

def is_valid_compressed_image(n_list):
    '''(list<list>)->bool
This function checks if a given nested list is a valid compressed image according
to the criteria provided. This function would return False if any of the criteria
isn't satisfied.
>>> is_valid_compressed_image([["0x5", "200x2","254x3"], ["111x5","123x5"]])
True
>>> is_valid_compressed_image([["0x5", "200x2","254x3"], ["111x5","1212312x5"]])
False
>>> is_valid_compressed_image([["0x5", "200x2","254x3"], ["111x5","1212312*5"]])
False
'''
    for value in n_list:
        for subvalue in value:
            if type(subvalue) == int: # if integer than immediately return false
                return False
    b_list = []
    for val in n_list:
        row_sum = 0
        for num in val:
            if type(num) != str or 'x' not in num:
                return False #Checking if the type is string 'x' in the string
            str_list = num.split('x')
            if len(str_list)>2:
                return False
            for char in str_list:
                if not (char.isdecimal()):
                    return False
                if not (0<=int(char)<=255):
                    return False #Checking if A and B's ranges are satisfied
                row_sum += int(str_list[1])
        b_list.append(row_sum)
    for number in b_list:
        if number != b_list[0]:
            return False
    return True
            


def load_regular_image(filename):
    '''<str>->list<list<int>>
This function takes in a string (filename) as input and load the file before converting
it to a image matrix. We will return the nested list representing the image matrix after
validating it is indeed a valid image matrix. Otherwise, an error message would be raised.
>>> load_regular_image("comp.pgm")
[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 51, 51, 51, 51, 51, 0, 119, 119, 119, 119, 119, 0, 187, 187, 187, 187, 187, 0, 255,
255, 255, 255, 0]....... Here omitting the rest to save the space
>>> Error message
Traceback (most recent call last):
AssertionError: This image matrix is not in PGM format
'''
    file = open(filename,'r')
    image_list=[]
    for line in file:
        sub_list=line.split()
        image_list.append(sub_list)
    file.close()
    image_list[:3]=[]
    ult_list = []
    for val in image_list:
        ul_list = []
        for subval in val:
            if not subval.isdecimal():
                raise AssertionError("This image matrix is not in PGM format")
            ul_list.append(int(subval))
        ult_list.append(ul_list)
    if not (is_valid_image(ult_list)):
        raise AssertionError("This image matrix is not in PGM format")
    return ult_list


def load_compressed_image(filename):
    '''<str>->list<list>
This function takes in a string (filename) as input and load the file before converting
it to a image matrix. We will return the nested list representing the image matrix after
validating it is indeed a valid compressed image matrix. Otherwise, an error message
would be raised.
>>> load_regular_image("comp.pgm")
>>> load_compressed_image("comp.pgm.compressed")
[['0x24'], ['0x1', '51x5', '0x1', '119x5', '0x1', '187x5', '0x1', '255x4', '0x1']....
Here omitting the rest to save the space
>>> Error message
Traceback (most recent call last):
AssertionError: This image matrix is not in compressed PGM format
'''
    file = open(filename,'r')
    image_list=[]
    for line in file:
        sub_list=line.split()
        image_list.append(sub_list)
    file.close()
    image_list[:3]=[]
    print(image_list)
    if not (is_valid_compressed_image(image_list)):
        raise AssertionError("This image matrix is not in compressed PGM format")
    return image_list


def load_image(filename):
    '''<str>->list<list>
This function detects whether the inputting file is a regular image or compressed image then returns the corresponding
image matrix accordingly. A AssertionError will also be raised if the inputting image is not one of the two types specified
>>> load_image("comp.pgm.compressed")
[['0x24'], ['0x1', '51x5', '0x1', '119x5', '0x1', '187x5', '0x1', '255x4', '0x1']... Here omit the rest to save space
>>> load_image("comp.pgm")
[['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
.... Here omit the rest to save space
>>> Error message
Traceback (most recent call last):
AssertionError: This image matrix is not in compressed PGM format
'''
    file = open(filename,'r')
    content= file.read()
    my_list = content.split('\n')
    file.close()
    if my_list[0] == 'P2':
        final_list = []
        new_list = load_regular_image(filename)
        for val in new_list:
            f_list = []
            for sub_val in val:
                f_list.append(int(sub_val))
            final_list.append(f_list)
        return final_list
    elif my_list[0] == 'P2C':
        return load_compressed_image(filename)
    else:
        raise AssertionError ("Check the image type and then try again")


def save_regular_image(n_list,filename):
    '''(list<list<int>>,str)->...
This function would take a nested list and save it to a file under the filename specified.
If the inputting nested list is not a valid PGM image, a AssertionError with a message would
be raised.
>>>save_regular_image([[0]*10, [252323]*10, [0]*10], "test.pgm")
Traceback (most recent call last):
AssertionError: Inputted nest list is not a valid regular PGM image
>>> save_regular_image([[0]*10, [25]*10, [0]*10, [232]*10],"test.pgm")
>>> fobj = open("test.pgm", 'r')
>>> fobj.read()
'P2\n10 4\n255\n0 0 0 0 0 0 0 0 0 0\n25 25 25 25 25 25 25 25 25 25\n0 0 0 0 0 0 0 0 0 0\n
232 232 232 232 232 232 232 232 232 232\n'
>>> save_regular_image([[0]*10, [232]*10],"test.pgm")
>>> fobj = open("test.pgm", 'r')
>>> fobj.read()
'P2\n10 2\n255\n0 0 0 0 0 0 0 0 0 0\n232 232 232 232 232 232 232 232 232 232\n'
'''
    if not(is_valid_image(n_list)):
        raise AssertionError("Inputted nest list is not a valid regular PGM image")
    final_string = "P2\n"+str(len(n_list[0]))+' '+str(len(n_list))+"\n"+str(255)+"\n"
    for val in n_list:
        for subval in val:
            final_string += str(subval)
            final_string += ' '
        final_string = final_string[:-1] #removing the last space
        final_string +='\n'
    file = open(filename,'w')
    file.write(final_string)
    file.close()


def save_compressed_image(n_list,filename):
    '''(list<list<str>>,str)->...
This function would take a nested list and save it to a file under the filename specified.
If the inputting nested list is not a valid compressed PGM image, a AssertionError with a message would
be raised.
>>> save_compressed_image([["0x52323", "200x2"], ["111x7"]], "test.pgm.compressed")
Traceback (most recent call last):
AssertionError: Inputted nest list is not a valid compressed PGM image
>>> save_compressed_image([["0x5", "200x2"], ["111x7"],["100x7"]], "test.pgm.compressed")
>>> fobj = open("test.pgm.compressed", 'r')
>>> fobj.read()
'P2C\n7 3\n255\n0x5 200x2\n111x7\n100x7\n'
>>> fobj.close()
>>> save_compressed_image([["0x5", "200x2"], ["100x7"]], "test.pgm.compressed")
>>> fobj = open("test.pgm.compressed", 'r')
>>> fobj.read()
'P2C\n7 3\n255\n0x5 200x2\n100x7\n'
>>> fobj.close()
'''
    if not(is_valid_compressed_image(n_list)):
        raise AssertionError("Inputted nest list is not a valid compressed PGM image")
    width = 0
    for val in n_list[0]:
        val_list = val.split('x')
        width += int(val_list[1])
    final_string = "P2C\n"+str(width)+' '+str(len(n_list))+"\n"+str(255)+"\n"
    for value in n_list:
        for subval in value:
            final_string += str(subval)
            final_string += ' '
        final_string = final_string[:-1] #removing the last space
        final_string +='\n'
    file = open(filename,'w')
    file.write(final_string)
    file.close()
    
def save_image(n_list,filename):
    '''(list<list<str/int>>,str)->...
This function takes a nested list and a filename (string) as input. Checks the type of elements in the
list. And if the element type is str it will save to compressed image, if the element type is int, it will
save to regular image, if not a AssertionError would be raised. Additionally, if the datatype in the nested list
is not consistent, a different AssertionError message would be raised.
>>> save_image([["0x5", "200x2"], [True]], "test.pgm.compressed")
Traceback (most recent call last):
AssertionError: Data types in the nested list are not consistent, check again
>>> save_regular_image([[0]*10, [255]*10, [0]*10], "test.pgm")
>>> fobj = open("test.pgm", 'r')
>>> fobj.read()
'P2\n10 3\n255\n0 0 0 0 0 0 0 0 0 0\n255 255 255 255 255 255 255 255 255 255\n0 0 0 0 0 0 0 0 0 0\n'
>>> fobj.close()
>>> save_image([[True], [False]], "test.pgm.compressed")
Traceback (most recent call last):
AssertionError: Data type is not correct cannot save, check again
'''
    init_type = type(n_list[0][0])#First we would verify whether the types are the same
    for val in n_list:
        for subval in val:
            if type(subval) != init_type:
                raise AssertionError ("Data types in the nested list are not consistent, check again")
    if init_type == int:
        save_regular_image(n_list,filename)
    elif init_type == str:
        save_compressed_image(n_list,filename)
    else:
        raise AssertionError ("Data type is not correct cannot save, check again")

def invert(n_list):
    '''(list<list<int>>)->list<list<int>>
This function takes in a nested list and returns the inverted version of the same
nested list. This function is for non-compressed PGM image matrix. 
>>> invert([[0, 100, 150], [200, 20, 100]])
[[255, 155, 105], [55, 235, 155]]
>>> invert([[0, 100, 100], [20, 20, 100]])
[[255, 155, 155], [235, 235, 155]]
>>> invert([[0, 100, 200], [20, 20, 100]])
[[255, 155, 55], [235, 235, 155]]
>>> invert([[0, 100, 200], [20, 20, 10000]])
Traceback (most recent call last):
AssertionError: The inputted nested list is not a valid PGM image matrix
'''
    if not(is_valid_image(n_list)):
        raise AssertionError("The inputted nested list is not a valid PGM image matrix")
    my_list = []
    for val in n_list:
        sublist=[]
        for subval in val:
            sublist.append(255-subval)
        my_list.append(sublist)
    return my_list

def flip_horizontal(n_list):
    '''(list<list<int>>)->list<list<int>>
This function takes a non-compressed PGM image matrix as input and returns the image
matrix flipped horizontally without modifying the original matrix. And if the inputted
matrix is not a valid input, a AssertionError would be raised.
>>> flip_horizontal([[0, 100, 200], [20, 20, 10000]])
Traceback (most recent call last):
AssertionError: The inputted nested list is not a valid PGM image matrix
>>> flip_horizontal([[0, 100, 200], [20, 200, 10]])
[[200, 100, 0], [10, 200, 20]]
>>> flip_horizontal([[255, 155, 105], [55, 235, 155]])
[[105, 155, 255], [155, 235, 55]]
'''
    if not(is_valid_image(n_list)):
        raise AssertionError("The inputted nested list is not a valid PGM image matrix")
    my_list =[]
    for val in n_list:
        new_l = val[::-1]
        my_list.append(new_l)
    return my_list

def flip_vertical(n_list):
    '''(list<list<int>>)->list<list<int>>
This function takes a non-compressed PGM image matrix as input and returns the image
matrix flipped vertically without modifying the original matrix. And if the inputted
matrix is not a valid input, a AssertionError would be raised.
>>> flip_vertical([[0, 100, 200], [20, 20, 10000]])
Traceback (most recent call last):
AssertionError: The inputted nested list is not a valid PGM image matrix
>>> flip_vertical([[0, 100, 200], [20, 20, 100]])
[[20, 20, 100], [0, 100, 200]]
>>> flip_vertical([[255, 155, 105], [55, 235, 155]])
[[55, 235, 155], [255, 155, 105]]
'''
    if not(is_valid_image(n_list)):
        raise AssertionError("The inputted nested list is not a valid PGM image matrix")
    my_list = n_list[::-1]
    return my_list

def crop(n_list,x1,x2,y1,y2):
    '''(list<list<int>>),int,int,int,int)->list<list<int>>
This function returns cropped PGM image matrix.  And if the inputted matrix is not a
valid input, a AssertionError would be raised.
>>> crop([[0, 100, 200], [20, 20, 10000]],1,1,2,2)
Traceback (most recent call last):
AssertionError: The inputted nested list is not a valid PGM image matrix
>>> crop([[0, 100, 200], [20, 20, 100],[0,1,15]],1,1,2,1)
[[20], [1]]
>>> crop([[0, 100, 200], [20, 20, 100],[0,1,15]],1,0,2,2)
[[20, 20], [0, 1]]
'''
    if not(is_valid_image(n_list)):
        raise AssertionError("The inputted nested list is not a valid PGM image matrix")
    my_list = []
    n_rows = n_list[x1:x1+y1]
    for val in n_rows:
        my_list.append(val[x2:x2+y2])
    return my_list


def find_end_of_repetition(my_list,index,num):
    '''(list,int,int)->int
This function takes in a list and returns the index where the target number discontinues
>>> find_end_of_repetition([1, 2, 3, 4, 5, 6, 7], 4, 5)
4
>>> find_end_of_repetition([1, 1, 1, 1, 1, 1, 1], 0, 1)
6
>>> find_end_of_repetition([1, 2, 3, 3, 4 , 4, 5], 2, 3)
3
'''
    if index == len(my_list)-1 or my_list[index] != my_list[index+1]:
        return index
    for i in range(index+1,len(my_list)):
        if my_list[i] != my_list[i-1]:
            return i-1
    return len(my_list)-1    

def compress(n_list):
    '''list<list<int>>->list<list<int>>
This function returns a compressed image (nested list) If the inputted nested
list is not a valid PGM list, an assertionerror would be raised.
>>> compress([[1, 2, 3, 4, 5], [0, 0, 5, 10, 10], [5, 5, 5, 5, 5]])
[['1x1', '2x1', '3x1', '4x1', '5x1'], ['0x2', '5x1', '10x2'], ['5x5']]
>>> compress([[5, 5, 5], [5, 6, 6], [6, 6, 7]])
[['5x3'], ['5x1', '6x2'], ['6x2', '7x1']]
>>> compress([[1, 2, 3, 4], [4, 5, 6, 7], [8, 9, 10, 11]])
[['1x1', '2x1', '3x1', '4x1'], ['4x1', '5x1', '6x1', '7x1'], ['8x1', '9x1', '10x1', '11x1']]
>>> compress([[1, 2, 3, 4], [4, 5, 6, 7], [8, 9, 10, 11000]])
Traceback (most recent call last):
AssertionError: The inputted nested list is not a valid PGM image matrix
'''
    if not(is_valid_image(n_list)):
        raise AssertionError("The inputted nested list is not a valid PGM image matrix")
    result_list = []
    for val in n_list:
        index = 0
        sub_list =[]
        current_rep = 0
        while index < len(val):
            rep = find_end_of_repetition(val,index,val[index])+1
            char = str(val[index])+'x'+str(rep-current_rep)
            current_rep = rep
            sub_list.append(char)
            index = rep
        result_list.append(sub_list)
    return result_list


def decompress(n_list):
    '''list<list<str>>->list<list<int>>
This function returns a non-compressed image (nested list) from a
a compressed image (nested list) If the inputted nested
list is not a valid compressed PGM list, an assertionerror would be raised.
>>> decompress([["0x5", "200x2"], ["111x7"]])
[[0, 0, 0, 0, 0, 200, 200], [111, 111, 111, 111, 111, 111, 111]]
>>> decompress([['11x5'], ['1x1', '5x3', '7x1'], ['255x3', '0x1', '255x1'],['200x5']])
[[11, 11, 11, 11, 11], [1, 5, 5, 5, 7], [255, 255, 255, 0, 255], [200, 200, 200, 200, 200]]
>>> decompress([['11x5'], ['1x1', '5x3', '7x1'], ['255x3', '0x1', '255x1'],['200x4']])
Traceback (most recent call last):
AssertionError: This image matrix is not in compressed PGM format
'''
    if not (is_valid_compressed_image(n_list)):
        raise AssertionError("This image matrix is not in compressed PGM format")
    my_list = []
    for val in n_list:
        sub_list = []
        for subval in val:
            curr_list = subval.split('x')
            for i in range(int(curr_list[1])):
                sub_list.append(int(curr_list[0]))                   
        my_list.append(sub_list)
    return my_list


def process_command(command_str):
    '''(str)->...
This function is written on the assumption that there will only be one LOAD which
will be at the start and only one SAVE. This function will execute commands in the
command string and save it using the name specified.
>>> process_command("LOAD<comp.pgm> CP ZVV INV INV SAVE<comp2.pgm>")
Traceback (most recent call last):
AssertionError: unrecognized command and try again
>>> process_command("LOAD<comp.pgm> INV INV SAVE<comp2.pgm>")
>>> image = load_image("comp.pgm")
>>> image2 = load_image("comp2.pgm")
>>> image == image2
True
>>> process_command("LOAD<comp.pgm> INV CR<1,2,3,4> SAVE<comp2.pgm>")
>>> image2 = load_image("comp2.pgm")
>>> image2
[[204, 204, 204, 204], [255, 255, 255, 255], [255, 255, 255, 255]]
'''
    command = ['INV', 'FH', 'FV', 'CR', 'CP', 'DC']
    command_list = command_str.split()
    mid_command = command_list[1:len(command_list)-1]
    for comm in mid_command:
        if comm[:2] == 'CR':
            continue
        if comm not in command:
            raise AssertionError("unrecognized command and try again")
    image_list = load_image(command_list[0][5:-1])
    for comms in mid_command:
        if comms == 'INV':
            image_list = invert(image_list)
        elif comms == 'FH':
            image_list = flip_horizontal(image_list)
        elif comms == 'FV':
            image_list = flip_vertical(image_list)
        elif comms == 'CP':
            image_list = compress(image_list)
        elif comms == 'DC':
            image_list = decompress(image_list)
        else:
            image_list = crop(image_list,int(comms[3]),int(comms[5]),int(comms[7]),int(comms[9]))
    save_image(image_list,command_list[-1][5:-1])
    