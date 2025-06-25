# Prolog
# Team 2
# Gabriel Gesteira, Evan Kalb, Todd McKenzie 
#Purpose: Compare two inputted times in the format of hours, minutes, and seconds, and determine which time occurs first or if they are the same.
#Pre-conditions (input): User provides the program hours, minutes, and seconds
#Post-conditions (output): The program will output a message indicating the relationship between the input times, and continue prompting the user for input until they enter -1 for the first hours to stop
def main():
    print("Tough times never last, but tough teams do\n")
    
    # Prompt the user to enter the first hours or -1 to stop
    first_hours = 0
    
    # Loop until the user enters -1 for the first hours
    while first_hours != -1:
        
        # Prompt the user to enter the first minutes, seconds, and the second hours, minutes, and seconds
        first_hours = int(input("Enter first hours or -1 to stop: "))
        if first_hours == -1:
        # If the user enters -1, skip the rest of the loop and continue with the next iteration
            continue 
        
        first_minutes = int(input("Enter first minutes: "))
        first_seconds = int(input("Enter first seconds: "))
        second_hours = int(input("Enter second hours: "))
        second_minutes = int(input("Enter second minutes: "))
        second_seconds = int(input("Enter second seconds: "))
    
        # Calculate the time in seconds for the first and second times
        first_time = (first_hours * 3600) + (first_minutes * 60) + first_seconds
        second_time = (second_hours * 3600) + (second_minutes * 60) + second_seconds
    
        # Compare the first and second times and print the appropriate message
        if first_time > second_time:
            print(f"\nFirst time: {first_hours:02d}:{first_minutes:02d}:{first_seconds:02d}")
            print(f"Second time: {second_hours:02d}:{second_minutes:02d}:{second_seconds:02d}")
            print("First time happens after second time\n")
        elif first_time == second_time:
            print(f"\nFirst time: {first_hours:02d}:{first_minutes:02d}:{first_seconds:02d}")
            print(f"Second time: {second_hours:02d}:{second_minutes:02d}:{second_seconds:02d}")
            print("The times are the same\n")
        else:
            print(f"\nFirst time: {first_hours:02d}:{first_minutes:02d}:{first_seconds:02d}")
            print(f"Second time: {second_hours:02d}:{second_minutes:02d}:{second_seconds:02d}")
            print("Second time happens after first time\n")
    
main()

'''
Test Cases

Behavior of time_compare
1: 0
2: 1
3: 1
4: 1
5: 2
6: 2
7: 2

Behavior of time_print 
1: 12:45:13
2: 04:44:15
3: 14:09:22
4: 17:13:05
5: 02:03:04

Behavior of main
1: First time = 11:34:02, Second time = 11:34:02, times are the same

'''