# Todd McKenzie, CS 115 Section 002, tmckenzie0034@uky.edu
# Purpose: To calculate the number of lines and words in a string.
# Pre-conditions: User inputs lines of text.
# Post-conditions: User is presented with the total lines, words, and average 
# word length.

def main():

    # initialize variables
    
    word_count = 0
    
    line_count = -1
    
    total_word_length = 0
    
    user_input = None
    
    # loop until sentinel is entered
    
    while user_input != "":
        
        user_input = input("Enter a line of text (press Enter to stop): ")
        
        # count the number of lines
        
        line_count += 1
    
        # split the input into words
        
        words = user_input.split()
    
        # update the word count and total word length
        
        for word in words:
            word_count += 1
            total_word_length += len(word)
    
    # calculate average word length
    
    if word_count == 0:
        
        avg_word_length = 0
        
    else:
        
        avg_word_length = total_word_length / word_count
    
    # print the results
    
    print('')
    
    print("There were", line_count,"line(s) containing", word_count,"word(s)")
    
    print("There was an average of {:.2f} characters per word".format(avg_word_length))

main()

# Test Cases:
# 1 line, 1 word, AVG word length 11.00
# 1 line, 20 words, AVG word length 4.05
# 3 lines, 3 words, AVG word length 5.00
# 1 line, 16 words, AVG word length 3.56
# 0 lines, 0 words, and AVG word length 0.00