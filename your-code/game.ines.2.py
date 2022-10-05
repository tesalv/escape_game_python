def game_to_open_dresser():
    """ Game that has to be solved in order to open the dresser. There are 10 games and opens the
    dresser when the player cracks 3 of them"""
    
    total_wins = 0

    print("In order to open the dresser you have to give 3 correct answers. Good luck! The clock is ticking!")

    result1 = input("Solve 5 + 88: ")
    if int(result1) == 93:
        total_wins += 1
        print("Very good! Let's see you crack the next one")
        pass
    else:
        print("No... Better luck next time!")
        pass

    result2 = input("Which sea creature has three hearts?: ")
    if result2.lower() == "octopus":
        total_wins += 1
        print("You are rocking!")
    else:
        print("Ups... Let's try again!")
    
    result3 = input("I have 20 stones. How many stones I get if I share them equally with my sister?")
    if int(result3) == 10:
        total_wins += 1
        print('You are on fire! Great!')
        if total_wins == 3:
            print("Yeah! You've just solved 3 challenges! Now you have the access to the key of the door D")
            pass
    else:
        print("Nop...")

        "if you freeze water what you get?"
     


game_to_open_dresser()
    






# def open_dresser():
#     """open the dresser to release the key"""