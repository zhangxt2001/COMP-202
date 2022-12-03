# Author: Xiaoteng Zhang
#McGill ID: 260895923

import musicalbeeps

avalue_list = ['sharp','flat','natural']
p_list = ['A','B','C','D','E','F','G','R']
oc_list = [1,2,3,4,5,6,7]

class Note:
    OCTAVE_MIN = 1
    OCTAVE_MAX = 7
    
    def __init__(self,duration,pitch,octave=1,accidental='natural'):
        '''(float,str,int,str)->Note
This constructor assigns values into the objects being created.
And when the argument values don't satisfy the requirements, four different
AssertionErrors would be raised.
*duration(float)
*pitch(str)
*octave(int)
*accidental(str)
>>> note = Note(2.0, "B", 5)
>>> note.accidental
'natural'
>>> note = Note('2.0', "B", 5)
Traceback (most recent call last):
AssertionError: duration should be a positive float
>>> note = Note(2.0, "B", 4, "thanks")
Traceback (most recent call last):
AssertionError: accidental should be an str and be the values specified
>>> note = Note(2.0, "B", 400, "natural")
Traceback (most recent call last):
AssertionError: Octave should be an integer and be the values specified
>>> note = Note(2.0, "Z", 4, "natural")
Traceback (most recent call last):
AssertionError: Pitch should be a string and be the letters specified
'''
        if (type(duration)!= float or duration <= 0):
            raise AssertionError('duration should be a positive float')
        if ((type(pitch)!=str) or (pitch not in p_list)):
            raise AssertionError('Pitch should be a string and be the letters specified')
        if ((type(octave)!=int) or (octave not in oc_list)):
            raise AssertionError('Octave should be an integer and be the values specified')
        if ((type(accidental.lower())!=str) or (accidental.lower() not in avalue_list)):
            raise AssertionError('accidental should be an str and be the values specified')
        self.duration = duration
        self.pitch = pitch
        self.octave = octave
        self.accidental = accidental.lower()
    
    def __str__(self):
        '''()->str
This method that returns a string of the format DURATION PITCH OCTAVE ACCIDENTAL
>>> note = Note(2.0, "B", 4, "flat")
>>> print(note)
2.0 B 4 flat
>>> note = Note(2.0, "B", 7, "flat")
>>> print(note)
2.0 B 7 flat
>>> note = Note(2.0, "A", 7, "flat")
>>> print(note)
2.0 A 7 flat
'''
        return str(self.duration)+' '+self.pitch+' '+str(self.octave)+' '+self.accidental.lower()
    
    def play(self,player_object):
        '''(Player) -> NoneType
This instance method takes in a player object and plays the corresponding note
through the speaker. 
>>> note = Note(2.0, "R", 4, "natural")
>>> note.play(player)
Pausing for 2.0s
>>> note = Note(2.0, "B", 4, "natural")
>>> note.play(player)
Playing B4 (493.88 Hz) for 2.0s
'''
        if self.pitch == 'R':
            note_str = 'pause'
        else:
            note_str = self.pitch + str(self.octave)
        player_object.play_note(note_str, self.duration)
        
        
        