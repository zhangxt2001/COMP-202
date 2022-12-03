# Author: Xiaoteng Zhang
#McGill ID: 260895923

import musicalbeeps
import note

class Melody:
    
    def __init__(self,filename):
        '''(str)->Melody
This constructor takes a filename and create three instance attributes.
*title(str)
*author(str)
*notes(Note)
>>> hot_cross_buns = Melody("hotcrossbuns.txt")
>>> print(hot_cross_buns.notes[9])
0.25 G 4 natural
>>> print(hot_cross_buns.title)
Hot Cross Buns
>>> print(hot_cross_buns.author)
Traditional
'''
        if type(filename) != str:
            raise AssertionError ("filename needs to be a string")
        obj = open(filename,'r')
        file_content = obj.read()
        content_list = file_content.split('\n')
        start = -1
        end = -1
        temp_list = []
        for i, item in enumerate(content_list):
            if item[-4:] == "true":
                if start == -1:
                    start = i
                else:
                    end = i
                    temp = []
                    for j in range(start,end+1):
                        curr = content_list[j].split()
                        curr[0] = str(float(curr[0]))
                        temp.append(' '.join(curr[:-1]))
                    temp_list += temp * 2
                    start = -1
                    end = -1
            elif item[-5:] == "false" and start == -1:
                curr = item.split()
                curr[0] = str(float(curr[0]))
                temp_list.append(' '.join(curr[:-1]))
        print(temp_list)
        
        final_list = []
        for value in temp_list:
            value_list = value.split()
            if value_list[1] == 'R':
                note_value = note.Note(float(value_list[0]),value_list[1])
            else:
                note_value = note.Note(float(value_list[0]),value_list[1],int(value_list[2]),value_list[3])
            final_list.append(note_value)
        self.notes = final_list           
        self.title = content_list[0]
        self.author = content_list[1]
    
    def play(self,player_object):
        '''(Player)-> Nonetype
This instance method takes a music player object, and play it.
Example is the followingL
>>> player = musicalbeeps.Player()
>>> happy_birthday = Melody("birthday.txt")
>>> happy_birthday.play(player)
'''
        for value in self.notes:
            value.play(player_object) # This is the play method on the Note class
        
    def get_total_duration(self):
        '''()->float
This function takes no explicit input and returns the total duration of a song as a float.
>>> happy_birthday = Melody("birthday.txt")
>>> happy_birthday.get_total_duration()
13.0
>>> hot_cross_buns = Melody("hotcrossbuns.txt")
>>> hot_cross_buns.get_total_duration()
8.0
'''
        total_time = 0 
        for value in self.notes:
            total_time += value.duration
        return total_time
    
    def lower_octave(self):
        '''()->Boolean
This method reduces the octaves of all notes by 1, if the original octave note is already 1, then it returns
an error.
>>> happy_birthday = Melody("birthday.txt")
>>> happy_birthday.lower_octave()
True
>>> happy_birthday.notes[4].octave
3
>>> hot_cross_buns = Melody("hotcrossbuns.txt")
>>> hot_cross_buns.lower_octave()
True
>>> hot_cross_buns.notes[4].octave
3
>>> hot_cross_buns = Melody("hotcrossbuns.txt")
>>> hot_cross_buns.lower_octave()
False
This is done by artifically changing an octave for hotcrossbuns file.
0.5 B 4 NATURAL false -> 0.5 B 1 NATURAL false
'''
        for value in self.notes:
            if value.octave == 1:
                return False
            value.octave = value.octave - 1
        return True
    
    
    def upper_octave(self):
        '''()->Boolean
This method increases the octaves of all notes by 1, if the original octave note is already 1, then it returns
an error.
>>> happy_birthday = Melody("birthday.txt")
>>> happy_birthday.upper_octave()
True
>>> happy_birthday.notes[4].octave
5
>>> hot_cross_buns = Melody("hotcrossbuns.txt")
>>> hot_cross_buns.upper_octave()
True
>>> hot_cross_buns.notes[4].octave
5
>>> hot_cross_buns = Melody("hotcrossbuns.txt")
>>> hot_cross_buns.upper_octave()
False
This is done by artifically changing an octave for hotcrossbuns file.
0.5 B 4 NATURAL false -> 0.5 B 7 NATURAL false
'''
        for value in self.notes:
            if value.octave == 7:
                return False
            value.octave = value.octave + 1
        return True
    
    def change_tempo(self,time):
        '''(float)->...
This method changes the total duration by changing the duration of each notes by multiplying by the float
inputted by the user. 
>>> hot_cross_buns = Melody("hotcrossbuns.txt")
>>> hot_cross_buns.change_tempo(0.5)
>>> hot_cross_buns.get_total_duration()
4.0
>>> hot_cross_buns = Melody("hotcrossbuns.txt")
>>> hot_cross_buns.change_tempo(2.0)
>>> hot_cross_buns.get_total_duration()
16.0
>>> hot_cross_buns = Melody("hotcrossbuns.txt")
>>> hot_cross_buns.change_tempo(3.0)
>>> hot_cross_buns.get_total_duration()
24.0
'''
        if type(time) != float:
            raise AssertionError("Type of time needs to be a float")
        for value in self.notes:
            value.duration = value.duration * time