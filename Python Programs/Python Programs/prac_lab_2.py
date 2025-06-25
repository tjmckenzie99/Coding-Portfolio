# Todd McKenzie, CS 115 Section 002, tmckenzie0034@uky.edu

from random import choice

def scramble(word):
    '''
    Purpose: mix a word to illustrate the power of the human brain
    Pre-condition: ordered word spelled correctly ( string ) as only parameter
    Post-condition: a scrambled word (string) is returned
       The first and last letter remain the same, the middle is mixed
    '''

    if len(word) <= 3:
        scrambled_str = word   # Not necessary to scramble short words

    else:
        # create a source list to choose from the middle of word
        source_lst = list(word[1:-1])

        # create a destination list that starts with the first letter of word
        dest_lst = [ word[0] ]

        # while loop to choose randomly from source, appending to destination
        while len(source_lst) > 0:
            letter = choice(source_lst)
            source_lst.remove(letter)
            dest_lst.append(letter)

        # append the last letter of the word to the destination
        dest_lst.append(word[-1])

        # convert the destination list back to a string
        scrambled_str = ''.join(dest_lst)

    return scrambled_str


def main():

    # print header and instructions
    print('--------------------------------------------------------')
    print('Enter story one line at a time, ending with a blank line')
    print('--------------------------------------------------------')

    # initialize a scrambled story list
    scrambled_story = []

    # use sentinel loop to process each line of input from the user
    
    sentence = input('->')
    
    while sentence != '':

        # split the input line into a list of words
        words = sentence.split()

        # use a for loop to create a list of scrambled words
        scrambled_words = []
        
        for word in words:
            
            # if the last character of the original word is not a letter
            
            if not word[-1].isalpha():
                
                # preserve the non-letter for later
                
                non_letter = word[-1]
                
                # remove the non-letter from the original word
                
                word = word[:-1]
            
            else:
                non_letter = ''

            # use provided function to scramble the original word
            scrambled_word = scramble(word)

            # concatenate scrambled word with last non-letter
            scrambled_word += non_letter

            # append the concatenation to the scrambled list
            scrambled_words.append(scrambled_word)

        # add the list of safely scrambled words to the scrambled story
        
        scrambled_story.append(' '.join(scrambled_words))

        sentence = input('->')

    # print output header
    print('------------------------------------------------------------')
    print('Now, can your human mind read the following scrambled story?')
    print('------------------------------------------------------------')

    # use a for loop to traverse and print the scrambled story
    for sentence in scrambled_story:
        print(sentence)

    
main()