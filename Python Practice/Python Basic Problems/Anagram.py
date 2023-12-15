# If letters of the word is same after rearranging is called anagram
# Length of word should be same
# act/cat shore/horse
string1 = input("Enter the 1st string ")
string2 = input("Enter the 2nd string ")

if len(string1) != len(string2):
    print("String is not Anagram")
else: 
    
    string1 = sorted(string1)
    string2 = sorted(string2)
if string1 == string2:
    print("They are anagram")
else:
    print("string are not anagram")