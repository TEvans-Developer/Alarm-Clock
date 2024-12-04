#Downloadable Alarm Sound Effects 
#https://www.fesliyanstudios.com/royalty-free-sound-effects-download/alarm-203

from playsound import playsound
import time 

#ANSI escape sequences to manipulate the terminal
#CLEAR Clears entire terminal screen
#CLEAR_AND_RETURN Clears terminal and returns cursor to home position
CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

#Defines the alarm function to take in time in seconds and elapse until 0

def alarm(seconds):
    time_elapsed = 0

    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60 
        seconds_left = time_left % 60 #Gives seconds left

        #Prints minutes and seconds left as two digits over previous digits (CLEAR_AND_RETURN)
        print(f"{CLEAR_AND_RETURN}Time Remaining: {minutes_left:02d}:{seconds_left:02d}") 

    #Alarm sounds when time_elapsed is zero (while loop has escaped )
    playsound("alarm.mp3")

#Takes in user input as an integer in minutes and seconds 
#Total_seconds determines how many seconds are in the minutes inputed + seoncds input
minutes = int(input("How many minutes to wait: "))
seconds = int(input("How many seconds to wait: "))
total_seconds = minutes * 60 + seconds 

#Total_seconds is the arguments for the seconds parameter in the alarm function
alarm(total_seconds)
