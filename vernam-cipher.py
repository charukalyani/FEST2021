"""
Vernam Cipher
A method of encrypting alphabetic text. It is a Transposition techniques for converting a plain text into a cipher text. 
In this mechanism we assign a number to each character of the Plain-Text, like a = 0, b = 1, c = 2, .. z = 25.
"""


def vernam(key, message):
    message = str(message)
    m = message.upper().replace(" ", "")  
    encrypt = ""
    for i in range(len(m)):
        letter = ord(m[i])-65     
        letter = (letter + key) % 25  
        letter += 65
        encrypt = encrypt + chr(letter) 

    return encrypt


print("*****VERNAM CIPHER*****")
Key = int(input("Key: "))
message = input("Message: ")
encrpt = vernam(Key, message)
print("Encrypted Message: ",encrpt)