#Downloadable Alarm Sound Effects 
#https://www.fesliyanstudios.com/royalty-free-sound-effects-download/alarm-203

from playsound import playsound
import time 
import keyboard

#ANSI escape sequences to manipulate the terminal
#CLEAR Clears entire terminal screen
#CLEAR_AND_RETURN Clears terminal and returns cursor to home position
CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"




def display_choices():
    print(CLEAR)
    print("Menu")
    #List of choices for the user
    choices = [
        "1. Set an Alarm",
        "2. Use Stopwatch",
        "3. Set Timer"
    ]
    print("Please choose one from the following options:")
    for choice in choices:
        print(choice)





def user_choice():
    #Display the available choices
    display_choices()

    #Take input from the user
    choice = (input("Enter the number of your choice(1, 2, or 3): "))

    if choice == '1':
        print("You chose to set an Alarm.")
    elif choice == '2':
        print("You chose to use the Stopwatch.")
    elif choice == '3':
        print("You chose to use the Timer.")
        set_timer()
    else:
        print("Invalid choice. Please try again")
        user_choice() #Recursive call to ask again if the input is invlid
    




#Takes in user input as an integer in minutes and seconds 
#Total_seconds determines how many seconds are in the minutes inputed + seoncds input
def set_timer():

    print(CLEAR)
    print("--Press 'm' to return to menu--")
    
    """user_inputs = []"""


    hours = int(input("How many hours to wait: "))
    minutes = int(input("How many minutes to wait: "))
    seconds = int(input("How many seconds to wait: "))
    alert_name = (input("What do you want to name this alert? "))

    """for input in (user_inputs):
        user_inputs.append(input)

        if user_inputs != int:
            print("Not valid input")
            set_timer()"""
        

    total_seconds = (hours * 3600) + (minutes * 60) + seconds

    
    #Call the timer function
    timer(total_seconds, alert_name)




#Defines the alarm function to take in time in seconds and elapse until 0
def timer(total_seconds, alert_name):
    time_elapsed = 0
    reset_flag =False

    print(CLEAR)
    while time_elapsed < total_seconds:
        if keyboard.is_pressed('m'):
            print("Returning to menu...")
            user_choice()   
            return # Retun to menu and stops the timer function

        if keyboard.is_pressed('r') and not reset_flag:
            print(f"{CLEAR_AND_RETURN}Timer reset!")
            time_elapsed = 0
            reset_flag = True
                    
        if not keyboard.is_pressed('r'):
            reset_flag = False

            time.sleep(1)
            time_elapsed += 1

            time_left = total_seconds - time_elapsed

            # Converts remaining seconds to hours, minutes and seconds
            hours_left = time_left // 3600 
            remaining_seconds = time_left % 3600
            minutes_left = remaining_seconds // 60 
            seconds_left = remaining_seconds % 60 #Gives seconds left

            #Prints minutes and seconds left as two digits over previous digits (CLEAR_AND_RETURN)
            print(f"{CLEAR_AND_RETURN}Time Remaining:{hours_left:02d}:{minutes_left:02d}:{seconds_left:02d}")
            print("--Hold 'm' to return to menu--") 

            #Alarm sounds when time_elapsed is zero (while loop has escaped )
    print(f"Alarm for: {alert_name}!") 
    playsound("alarm.mp3")

        # Get new time values if they want to reset the timer
    restart= input("Do you want to reset the timer ? Press 'y' to restart, or 'n' to exit: ")
    while restart.lower() not in ['y','n']: #Keep looping until user enters 'y' or 'n'
        print ("Not a vlid input. Please enter 'y' to restart or 'n' to exit.")
        restart = input("Do you want to reset the timer ? Press 'y' to restart, or 'n' to exit: ")
    
    if restart.lower() =='y':
        set_timer()
    elif restart.lower() == 'n':
        print("Goodbye!")
        user_choice()

      

user_choice()


