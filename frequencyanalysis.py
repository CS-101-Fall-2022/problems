# Author: Hammad Sajid
# Date: Fall 2022 semester
# Course: CS 101 Programming Fundamentals
# Purpose: demonstrating a method to crack multiple substitution ciphers by the help of Frequency Analysis.
# Reference: https://en.wikipedia.org/wiki/Frequency_analysis#:~:text=In%20cryptanalysis%2C%20frequency%20analysis%20(also,aid%20to%20breaking%20classical%20ciphers.
# Functions:
#           frequencyanalysis: given any string, the function shall return the frequency of each letter
#                              in the form of tuples in a list.
# Concepts: the implementation below uses
#   - functions
#   - computation
#   - string data type
#   - some string methods (count(), lower(), isalpha())
#   - iteration 
#   - conditional statements
#   - list functions (append(), remove())
# Variarions:
#   - output can be returned in the form of nested lists or dictionary.
#   - Instead of using isaplha(), conditions can be used to only allow the 
#     frequency of alphabets to be counted instead of numbers/special characters.   
#   - Instead of using remove(), make another list to keep a check on the alphabets so
#     that the alphabets won't be repeatedly counted. 
#   - Instead of utilising count(), iterative approach can be used to count the frequency
#     of a single character
#   - Instead of making an alphabets list, 'char' can be used iteratively.
#   - sort() may be used to return list with frequency of elements in an ordered form.

string = str(input("Please enter the string to count the frequency of the letters: "))
string = string.lower()   #converts string to lower case to prevent missing out capital letters.
alphabetslst = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']  #check list to avoid repeatation of frequency of each letter.
emplst = []    #final list that will have the frequency of all the letters.


def frequencyanalysis(emplst, string):
    for i in string:
        if i.isalpha() == False:    #condition to only allow the frequency of alphabets to be calculated.
            continue
        else:
            if i in alphabetslst:
                freq = string.count(i)     #the frequency of the single alphabet would be counted in this single line.
                freqtuple = (i, freq)      #tuple will be formed with freqtuple[0] having the character and freqtuple[1] having it's frequency.
                emplst.append(freqtuple)   #appends the above tuple in the final frequency list.
                alphabetslst.remove(i)     #removes the alphabet from the check alphabetslst to avoid repeatation.
    return emplst
    
print(frequencyanalysis(emplst,string))         
