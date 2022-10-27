# Name: Xiaoteng Zhang
# McGill ID: 260895923

ROOM_NAME = "The room"
AUTHOR = "Xiaoteng Zhang"
PUBLIC = True


def hidden_command(s):
    '''(str) -> ... 
This function will be used later escape_room(). It takes in a string and if that string contains
certain words of interest, a success message will be printed. If the string doesn't contain such
words of interest, then the user will be prompted to input the string again.
>>> hidden_command("key")
Oh no, not successful this time
re-think
Hint:open door or use key to the door:key to the door
Yes ! Successfully escaped ! Freedooooooom !

>>> hidden_command("key to the door")
Yes ! Successfully escaped ! Freedooooooom !

>>> hidden_command("open the door using the key provided")
Yes ! Successfully escaped ! Freedooooooom !
'''
    while not(("key" in s.lower() or "open" in s.lower()) and "door" in s.lower()):
        s = input("Oh no, not successful this time\nre-think\nHint:open door or use key to the door:")
    if ("key" in s.lower() or "open" in s.lower()) and "door" in s.lower():
        print("Yes ! Successfully escaped ! Freedooooooom !")
        
def escape_room():
    '''() -> ...
Calling this function would initiate an interactive escape game.
>>> escape_room()
You were kidnapped by a bunch of strangers. When you woke up, you found yourself in a room.
Now you looked around, you see three objects in the room: an unlocked safe, a note, and a 
book.
To escape the room as well as from your kidnappers, what do you do now:asasas
Invalid input, re-think what do you do now:Examine The BOoK
There is nothing inside the book but one sentence: I have unlocked the door, go open it !
It's quite evident what you should as you walking towards the door :open door
Yes ! Successfully escaped ! Freedooooooom !

>>> escape_room()
You were kidnapped by a bunch of strangers. When you woke up, you found yourself in a room.
Now you looked around, you see three objects in the room: an unlocked safe, a note, and a 
book.
To escape the room as well as from your kidnappers, what do you do now:go to the safe
You approach the safe and see that there is a key lying inside. Now you look around and
discovered that there is only one door in that room and its keyhole ressembles that key
What do you want to do now that you have the possession of a key :use key for the door
Yes ! Successfully escaped ! Freedooooooom !

>>> escape_room()
You were kidnapped by a bunch of strangers. When you woke up, you found yourself in a room.
Now you looked around, you see three objects in the room: an unlocked safe, a note, and a 
book.
To escape the room as well as from your kidnappers, what do you do now:list commands
look into the unlocked safe
examine book
read what's written on the note
To escape the room as well as from your kidnappers, what do you do now:examine the book
There is nothing inside the book but one sentence: I have unlocked the door, go open it !
It's quite evident what you should as you walking towards the door :open the door
Yes ! Successfully escaped ! Freedooooooom !
'''
    print("You were kidnapped by a bunch of strangers. When you woke up, you found yourself in a room.")
    print("Now you looked around, you see three objects in the room: an unlocked safe, a note, and a ")
    print("book.")
    
    command = input("To escape the room as well as from your kidnappers, what do you do now:")
    
    if command.lower() == "list commands":
        print("look into the unlocked safe\nexamine book\nread what's written on the note")
        command = input("To escape the room as well as from your kidnappers, what do you do now:")
    while "safe" not in command.lower() and "note" not in command.lower() and "book" not in command.lower():
        command = input("Invalid input, re-think what do you do now:")
    if "safe" in command.lower(): 
        print("You approach the safe and see that there is a key lying inside. Now you look around and")
        print("discovered that there is only one door in that room and its keyhole ressembles that key")
        interaction = input("What do you want to do now that you have the possession of a key :")
        hidden_command(interaction)
    elif "note" in command.lower():
        print("There is only one line written on the note: I have unlocked the door, go open it !")
        interaction = input("It's quite evident what you should as you walking towards the door :")
        hidden_command(interaction)
    elif "book" in command.lower():
        print("There is nothing inside the book but one sentence: I have unlocked the door, go open it !")
        interaction = input("It's quite evident what you should as you walking towards the door :")
        hidden_command(interaction)
            
    
    