#A Caesar Cipher program which shifts each character by the specified range
#provided by the user.



#Steps of program

#Ask user for a line of text to encrpyt
    #check to see if text is all letter and or numbers
    #if invalid have them try again
#Ask the user for a shifting value from 1-25
    #check to see if the number is a valid integer between 1-25
#Print out the encoded text



isValid = False
while isValid != True:
    try:
        strng = input("Enter in a code: ")
        if strng == "":
            print("Not a valid entry please enter a valid string with letters and or numbers")
            continue
        else:
            isValid = True
    except(ValueError):
        print("Please enter a valid string with letters and or numbers")
isValid2 = False
while isValid2 != True:
    try:
        ran = int(input("Enter a range from 1-25: "))
        if ran > 25 or ran < 1:
            print("Not a valid number between 1-25 try again")
            continue
        else:
            isValid2 = True
    except(ValueError):
        print("Please enter a valid number from 1-25: ")
        
#set up counting variables based on 65-90 A-Z and 97-122 a-z ASCII
toNinety = 0
toOneTwentyTwo = 0

#Variables that store sum of (chr(ord(let) + ran) when sum is < 122
aChar = 0
bChar = 0

newString = ""


while len(newString) != len(strng):
    for let in strng:
        if let.isalpha():
            if let.islower():
                if(ord(let) + ran) > 122:
                    toOneTwentyTwo = 122 - ord(let)
                    newRan = ran
                    newRan -= toOneTwentyTwo
                    aNewChar = ord("a")
                    newRan -= 1
                    while newRan > 0:
                        newRan -= 1
                        aNewChar += 1
                    
                    newString += chr(aNewChar)
                else:
                    aChar = chr(ord(let) + ran)
                    newString += aChar
            elif let.isupper():
                if(ord(let) + ran) > 90:
                    toNinety = 90 - ord(let)
                    newRan = ran
                    newRan -= toNinety
                    bNewChar = ord("A")
                    newRan -= 1
                    while newRan > 0:
                        newRan -= 1
                        bNewChar +=1 
                    newString += chr(bNewChar)
                else:
                    bChar = chr(ord(let) + ran)
                    newString += bChar
        elif let.isdigit():
            newString += let
        else:
            newString += " "
            
print(newString)
