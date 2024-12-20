#Adding variables
string = input("Enter a prompt your would like to be in reversed ")
string2 = ""
#writing code
for i in string:
    string2 = i + string2
print("Your original text is ",string)
print("The reversed text is ",string2)