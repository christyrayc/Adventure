
 #def game():
    # Room descriptions
rooms = {
        "clearing": "You are standing in a lonely clearing. The Data Medal is hidden somewhere nearby.",
        "tower": "You have reached a tall tower. The mage who knows the magic spell lives here.",
        "forest": "You find yourself in a dense forest. A bear is guarding the path.",
        "beekeeper": "You arrive at a beekeeper's hut. They might have something the bear loves."
}

current_room = "clearing"  # Starting room
honey = False
medal = False

while True:
    print("\n" + rooms[current_room])
    action = input("Where would you like to go? ").lower()

    if current_room == "clearing":
        if action == "tower":
            current_room = "tower"
        elif action == "forest":
            current_room = "forest"
        else:
            print("Invalid input. Choose a valid room.")
    elif current_room == "tower":
        if action == "clearing":
                current_room = "clearing"
        else:
                print("Invalid input. Choose a valid room.")
        
    elif current_room == "forest":
        if honey:
            print('Bear distracted')
        else:
            print('Bear attacks')    
        if action == "clearing":
                current_room = "clearing"
        elif action == "beekeeper":
                current_room = "beekeeper"
        else:
            print("Invalid input. Choose a valid room.")
        
    elif current_room == "beekeeper":
        honey = True
        if action == "forest":
                current_room = "forest"
        else:
            print("Invalid input. Choose a valid room.")
        
        # Check if the player found the medal
    elif current_room == "clearing" and action == "medal":
        print("\nCongratulations! You found the Data Medal and unlocked the Power of Data Analytics!")
        break
    else:
        print("Invalid input. Choose a valid room.")    

#game()
