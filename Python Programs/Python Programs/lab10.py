# Prolog
# Name: Evan Kalb, Gabriel Gesteira, Todd McKenzie 
# Section: 002
# Email: eka263@uky.edu
# Purpose: The purpose of this function is to take an English sentence as input, translate it to Pig Latin using specified rules, and return the translated Pig Latin sentence as output.
# Pre-conditions: Any english word or sentnce (input)
# Post-conditions: Each word in the output is translated to Pig Latin using the specified rules:
 # If the word starts with a vowel, the suffix "way" is added to the end of the word.
 # If the word starts with a consonant, all the consonants up to the first vowel are moved to the end of the word, followed by the suffix "ay".
 # If the word contains no vowels, the suffix "ay" is added to the end of the word.

# Version 1: Pig Latin Translator
def main():
    def find_vowel(word):
        """
        This function returns the location of the leftmost vowel in the given word.
        If no vowel is found, it returns -1.
        """
        vowels = 'aeiou'
        word = word.lower()
        i = 0
        while i < len(word):
            if word[i] in vowels:
                return i
            i += 1
        return -1
   
    def pig_latin_v2(sentence):
        """
        This function translates the given English sentence to Pig Latin
        using the strict Pig Latin rules (Version 2).
        """
        # Split the sentence into words
        words = sentence.split()
   
        # Initialize the new sentence
        new_sentence = ""
   
        # Loop through each word in the sentence
        for word in words:
            # Check if the word starts with a vowel
            if word[0].lower() in 'aeiou':
                new_word = word + "way"
            else:
                # Find the index of the leftmost vowel
                vowel_index = find_vowel(word)
                if vowel_index == -1:
                    # No vowels found, add 'ay' to the end of the word
                    new_word = word + "ay"
                else:
                    # Move the consonants up to the vowel to the end of the word, add 'ay'
                    new_word = word[vowel_index:] + word[:vowel_index] + "ay"
            # Add the translated word to the new sentence
            new_sentence += new_word + " "
   
        return new_sentence.strip()
   
    # Get input from user
    print("Translate an English sentence to a Pig Latin sentence!")
    english_sentence = input("Enter English sentence: ")
   
    # Translate the sentence to Pig Latin (Version 2)
    pig_latin_sentence_v2 = pig_latin_v2(english_sentence)
   
    # Translate the sentence to Pig Latin (Version 1) for comparison
    pig_latin_sentence_v1 = ""
    vowels = "aeiou"
   
    # Split the sentence into words
    words = english_sentence.split()
   
    # Loop through each word in the sentence
    for word in words:
        # Check if the word starts with a vowel
        if word[0].lower() in vowels:
            new_word = word + "way"
        else:
            new_word = word[1:] + word[0] + "ay"
        # Add the translated word to the new sentence
        pig_latin_sentence_v1 += new_word + " "
   
    # Print the original and translated sentences
    print("English: " + english_sentence)
    print("PL Ver1: " + pig_latin_sentence_v1.strip())
    print("PL Ver2: " + pig_latin_sentence_v2)
main()