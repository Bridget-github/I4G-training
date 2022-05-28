# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


from operator import truediv
from turtle import position
from xml.etree.ElementPath import find
from xmlrpc.client import FastUnmarshaller


# def find_anagram(word, anagram):


    
    # [assignment] Add your code here

    # return True



def find_anagram(ward,draw):

#sorting strings to check whether both are matches

    if(sorted(string1)== sorted(string2)):   
        print("True")
    else:
        print("False")

string1 = "ward"    #variable
string2 = "draw"
print("string value1 : ", string1 )
print("string value2 : ", string2 )
find_anagram(string1, string2)   #returns true if they are anagrams


def find_anagram(water,draw):

#sorting strings to check whether both are matches

    if(sorted(string1)== sorted(string2)):   
        print("True")
    else:
        print("False")

string1 = "water"    #variable
string2 = "draw"
print("string value1 : ", string1 ) #prints the string and assigned value
print("string value2 : ", string2 )
find_anagram(string1, string2)   #returns false if they are not anagrams