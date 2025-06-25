# Todd McKenzie, CS 115 Section 002, tmckenzie0034@uky.edu

# Purpose: To pull this dictionary file.
# Pre-conditions: User enters the name of the text file.
# Post-conditions: The corrected words list is returned

def get_dictionary_file():
    
    # Open the "dictionary.txt" file in read mode
    dictionary_file = open("dictionary.txt", "r")

    # Read in the contents of the file as a string
    dictionary_string = dictionary_file.read()

    # Close the file
    dictionary_file.close()

    # Split the string into individual words and return the list of valid words
    goodlist = dictionary_string.split()
    
    return goodlist

# Purpose: To calculate how many misspelled words are in the a statement
# Pre-conditions: User enters the file name.
# Post-conditions: User is presented with the misspelled word count.

def main():
    
    # Retrieve the list of valid words
    goodlist = get_dictionary_file()

    # Prompt the user to enter a filename to check
    filename = input("Enter a filename to check: ")

    # Open the file specified by the user in read mode
    file = open(filename, "r")

    # Read in the contents of the file as a string and split it into individual words
    words = file.read().split()

    # Close the file
    file.close()

    # Initialize counters for misspelled words and a list to store them
    misspelled_count = 0
    misspelled_words = []

    # Loop over each word in the file
    
    for word in words:
        
        # Convert the word to lowercase to compare it with the valid words
        
        word = word.lower()

        # Check if the word is misspelled (not in the valid words list and longer than 3 characters)
        
        if len(word) > 3 and word not in goodlist:
            
            # If the word is misspelled, increment the counter and add it to the list of misspelled words
            
            misspelled_count += 1
            misspelled_words.append(word)

    # Print out the list of misspelled words and the total count of misspelled words
    
    print("Misspelled words:")
    
    for word in misspelled_words:
        
        print(word)
        
    print(f"There were {misspelled_count} misspelled words.")

# Call the main function to run the spell-checker

main()

