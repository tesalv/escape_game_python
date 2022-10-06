import tkinter as tk
import os, time
from threading import Thread

# define rooms and items

gate_a = {
    "name": "gate a",
    "type": "gate",
}

gate_b = {
    "name": "gate b",
    "type": "gate",
}

gate_c = {
    "name": "gate c",
    "type": "gate",
}

gate_d = {
    "name": "gate d",
    "type": "gate",
}

boarding_ticket_a = {
    "name": "boarding ticket for gate a",
    "type": "key",
    "target": gate_a,
}

boarding_ticket_b = {
    "name": "boarding ticket for gate b",
    "type": "key",
    "target": gate_b,
}

boarding_ticket_c = {
    "name": "boarding ticket for gate c",
    "type": "key",
    "target": gate_c,
}

boarding_ticket_d = {
    "name": "boarding ticket for gate d",
    "type": "key",
    "target": gate_d,
}

piano = {
    "name": "piano",
    "type": "monument",
}

st_stephens_cathedral = {
    "name": "cathedral",
    "type": "monument",
}

chichen_itza = {
    "name": "chichen itza",
    "type": "monument",
}

ganges = {
    "name": "ganges",
    "type": "monument",
}

taj_mahal = {
    "name": "taj mahal",
    "type": "monument",
}

great_wall = {
    "name": "great wall",
    "type": "monument",
}

musical_painting = {
    "name": "musical painting",
    "type": "monument",
}

austria = {
    "name": "Austria",
    "type": "room",
}

mexico = {
    "name": "Mexico",
    "type": "room",
}

india = {
    "name": "India",
    "type": "room",
}

china = {
    "name": "China",
    "type": "room",
}


maldives = {
  "name": "Maldives"
}

all_rooms = [austria, mexico,india,china,maldives]

all_gates = [gate_a,gate_b,gate_c,gate_d]

# define which items/rooms are related

object_relations = {
    "Austria": [st_stephens_cathedral, piano, gate_a,musical_painting],
    "Mexico": [chichen_itza,gate_a, gate_b, gate_c],
    "India": [ganges,taj_mahal, gate_b],
    "China": [great_wall,gate_d, gate_c],
    "Maldives": [gate_d],
    "piano": [boarding_ticket_a],
    "chichen itza":[boarding_ticket_b],
    "ganges":[boarding_ticket_c],
    "taj mahal":[boarding_ticket_d],
    "gate a": [austria, mexico],
    "gate b": [india, mexico],
    "gate c": [china, mexico],
    "gate d": [maldives, china]
}

# define game state. Do not directly change this dict. 
# Instead, when a new game starts, make a copy of this
# dict and use the copy to store gameplay state. This 
# way you can replay the game multiple times.

INIT_GAME_STATE = {
    "current_room": austria,
    "keys_collected": [],
    "target_room": maldives
}
def linebreak():
    """
    Print a line break
    """
    print("\n")

def start_game():
    """
    Start the game
    """
    print("\n You finally finished your Ironhack bootcamp and decided to take a break. Your holidays were booked in the Maldives but something went wrong. You wake up on a St. Stephen's Cathedral, in Austria. Oh noooo! You want to get out of here and reach your destination. Find your way to paradise. NOW!!")
    play_room(game_state["current_room"])

def play_room(room):
    """
    Play a room. First check if the room being played is the target room.
    If it is, the game will end with success. Otherwise, let player either 
    explore (list all items in this room) or examine an item found here.
    """
    game_state["current_room"] = room
    if(game_state["current_room"] == game_state["target_room"]):
        print("Congrats! You arrived in the Maldives! Get yourself and drink and relax in the sun now!")
    else:
        print("You are now in " + room["name"])
        intended_action = input("What would you like to do? Type 'a' to explore the country or 'b' to examine the landmarks/objects?").strip()
        linebreak()
        if intended_action.lower() == "a":
            explore_room(room)
            play_room(room)
        elif intended_action.lower() == "b":
            examine_item((input("What landmark/object would you like to examine?").strip()))
            linebreak()
        else:
            print("Not sure what you mean. Type 'a' to explore the country or 'b' to examine the landmarks/objectshe room or 'b' to examine the objects in the room?")
            play_room(room)
        #linebreak()

def explore_room(room):
    """
    Explore a country. List all items belonging to this countries.
    """
    items = [i["name"] for i in object_relations[room["name"]]]
    print("You explore the country. This is " + room["name"] + ". You find " + ", ".join(items))

def get_next_room_of_gate(gate, current_room):
    """
    From object_relations, find the two rooms connected to the given gate.
    Return the room that is not the current_room.
    """
    connected_rooms = object_relations[gate["name"]]
    for room in connected_rooms:
        if(not current_room == room):
            return room

def examine_item(item_name):
    """
    Examine an item which can be a gate or monument.
    First make sure the intended item belongs to the current room.
    Then check if the item is a gate. Tell player if boarding ticket hasn't been 
    collected yet. Otherwise ask player if they want to go to the next
    room. If the item is not a gate, then check if it contains keys.
    Collect the boarding ticket if found and update the game state. At the end,
    play either the current or the next room depending on the game state
    to keep playing.
    """
    current_room = game_state["current_room"]
    next_room = ""
    output = None
    
    for item in object_relations[current_room["name"]]:
        if (item["name"] == item_name.lower()):
            output = "You examine " + item_name + ". "
            if(item["type"] == "gate"):
                have_boarding_ticket = False
                for boarding_ticket in game_state["keys_collected"]:
                    if(boarding_ticket["target"] == item):
                        have_boarding_ticket = True
                if(have_boarding_ticket):
                    output += "You can go throught the gate with the boarding ticket you have."
                    next_room = get_next_room_of_gate(item, current_room)
                else:
                    output += "It is a boarding gate but you don't have a ticket."
            elif item["name"] == "musical painting":
                print("You're looking at the musical painting. Pay attention! It has 6 objects portraited: Giant, Aligator, Ant, Dice, Car, Fan")
                output=output.replace("You examine " + item_name + ". ","")
                #output=None
            
            elif item["name"] == "piano":
                playtime= True
                while playtime== True:
                    print("You're facing the piano, please sit and play something.")
                    song_played=input("Can you play a 6 note song? ").replace(" ","")
                    linebreak()
                    if song_played.upper()=="GAADCF":
                        print("You're a musical genius! Wait, something was revealed.")
                        item_found = object_relations[item["name"]].pop()
                        game_state["keys_collected"].append(item_found)
                        print("You find boarding ticket foor gate a.")
                        output=output.replace("You examine " + item_name + ". ","")
                        #output=None
                        playtime= False
                    else:
                        print("That is not a great song, please try again. Remember the musical notes are: A B C D E F G. Maybe explore the room for inspiration \n")
                        another_try=input("Do you want to try again? Yes or No?")
                        linebreak()
                        output=output.replace("You examine " + item_name + ". ","")
                        #output=None
                        if another_try.upper()== "NO":
                            playtime=False
                        else: 
                            continue

            elif item["name"] == "taj mahal":
                game_to_open_taj_mahal() 
                item_found = object_relations[item["name"]].pop()
                game_state["keys_collected"].append(item_found)               
            
            else:
                if(item["name"] in object_relations and len(object_relations[item["name"]])>0):
                    item_found = object_relations[item["name"]].pop()
                    game_state["keys_collected"].append(item_found)
                    output += "You find " + item_found["name"] + "."
                else:
                    output += "There isn't anything interesting about it."
            if output!= "":
                print(output)
                break

    if(output is None):
        print("The item you requested is not found in the current room.")
    
    if(next_room and input("Do you want to go through the boarding gate? Enter 'yes' or 'no'").strip() == 'yes'):
        linebreak()
        play_room(next_room)
    else:
        play_room(current_room)




def game_to_open_taj_mahal():
    """ 3 games that has to be solved in order to enter the taj mahal. """
    
    total_wins = 0

    print("In order to enter the taj mahal you have to give 3 correct answers. Good luck! The clock is ticking!")

    Flag = True
    while Flag == True:
        result1 = input("Solve 5 + 88: ")
        linebreak()
        if (result1.isdigit() == True) and (int(result1) == 93):
            total_wins += 1
            print("Very good! Let's see if you crack the next one")
            Flag = False
        elif result1.isdigit() == False:
            print("You have to give me numbers. Try Again")
            Flag = True
        else:
            print("No... Better luck next time! Let's try again!" )
            Flag = True
    
    Flag = True
    while Flag == True:
        result2 = input("Which sea creature has three hearts?: ")
        linebreak()
        if result2.lower() == "octopus":
            total_wins += 1
            print("You are rocking!")
            Flag = False
        else:
            print("Ups... Let's try again!")
            Flag = True
    
    Flag = True
    while Flag == True:
        result3 = input("if you freeze water what you get?: ")
        linebreak()
        if result3.lower() == "ice":
            total_wins += 1
            print('You are amazing! Great!')
            Flag = False
            if total_wins == 3:
                print("Yeah! You've just solved 3 challenges! Now you have found the boarding ticket of the gate D")
                break
        else:
            print("Nop... Try again!")
            Flag = True

game_state = INIT_GAME_STATE.copy()

root = tk.Tk()
# set window size
root.geometry("500x200")

def start_timer(count):
    label = tk.Label(root)
    label.place(x=32, y=35)
    label.config(font=("Courier", 20))

    # change text in label   
    total_mins = count//60 # minutes left
    total_sec = count-(60*(total_mins)) #seconds left  
    if total_sec < 10:
        total_sec = f"0{total_sec}"
     
    label['text'] = '{min}:{sec}'.format(min=total_mins, sec=total_sec)

    if count > 0:
        # call countdown again after 1000ms (1s)
        root.after(1000, start_timer, count-1)
    if count == 0:
        label['text'] = 'GAME OVER'
        root.after(1000, start_timer, count-1)
    if count < 0:
        label['text'] = 'GAME OVER'
        time.sleep(2)
        root.destroy()
        return False



if __name__ == '__main__':
    game = Thread(target= start_game)
    game.start()

    timer = Thread(target= start_timer, args=(210,))
    timer.start()
    root.mainloop()

    timer.join()
    if timer.is_alive() == False:
        print("\n you are too slow and missed your flight! game over!")
        os._exit(0)
