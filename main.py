# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from importlib.resources import contents
from itertools import count





    with open('story.txt') as f:
        read_file_contents = f.read()  #to return a string
        print(read_file_contents) #read all the lines in a text 
        count_words = read_file_contents.count("a")
        print(count_words) #counting the number of 'a'
        count_words = read_file_contents.count("glass")
        print(count_words) #counting the number of 'glass'

 #creating a dictionary       
dictionary = {'a': '29' , 'glass': '4'}
for key, value in dictionary.items():
    print(f"{key}: {value}") #printing the key and value


 