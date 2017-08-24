import os

# points to location of the file
filename = 'test.txt'

# code inspired by Python Crash Course book
# the following tries to open the file we've pointed to
try:
    with open(filename) as text:
        # reads the contents
        contents = text.read()
        # counts the number of periods to get count of declarative sentences.  could add two more variables for interogative and exclamatory and combine to get all sentences
        result = contents.count('.')

# creates and exception in case that the file is not located        
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
else:
    # splits the contents that have been read into words
    words = contents.split()
    # below sets up the output
    print("Paragraph Analysis")
    print("------------------")
    
    # variable num_words counts the words that have been split out
    num_words = len(words)
    print("Approximate word count: " + str(num_words))   
    
    #the following actually returns a list of letter counts for each word
    letter_count_per_word = [len(w) for w in words]
    
    # output the approximate sentence count
    print("Approximate sentence count: " + str(result))
    
    # output the approximate letter count per word
    print("Average letter count: " + str(sum(letter_count_per_word) / float(len(letter_count_per_word))))
    
    # output the approximate words per sentence
    print("Approximate words per sentence: " + (str(num_words/result)))
 

    
