def change_char_advanced(s,replace_index,char):
    s_new = ''
    for i in range(len(s)):
        if i != replace_index:
            s_new += s[i]
        elif i == replace_index:
            s_new += char
    return s_new



def follow_trail_2D(s,i_row,i_col,width,height,num_to_travel):
    starting_index = i_row*width + i_col
    for i in range(num_to_travel):
        if s[starting_index] == '>':
            s = change_char_advanced(s,starting_index,'X')
            starting_index += 1
            if starting_index % width > width-1:
                starting_index = (starting_index // width)*width
        elif s[starting_index] == '<':
            s = change_char_advanced(s,starting_index,'X')
            starting_index -= 1
            if starting_index % width <= 0:
                starting_index = (starting_index // width)*width + width+1
        elif s[starting_index] == '∧':
            s = change_char_advanced(s,starting_index,'X')
            starting_index -= width
            if starting_index < 0:
                starting_index = starting_index + height*width
        elif s[starting_index] == 'v':
            s = change_char_advanced(s,starting_index,'X')
            starting_index += width
            if starting_index > width*height-1:
                starting_index = starting_index - height*width
    return s
        
        