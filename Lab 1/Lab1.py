import sys
import math

operation = input()
offset_input = int(input())
rotors=[]
for i in range(3):
    rotors.append(input())
message_input = input()
offset_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet = list(offset_alphabet) 
message = list(message_input)

if operation == 'ENCODE':
    letter_position = 0
    for letter in message:
        for offset_letter in offset_alphabet:
            if letter == offset_letter:
                offset = offset_input + letter_position + offset_alphabet.index(offset_letter)
                while offset >= len(offset_alphabet):
                    offset = offset - len(offset_alphabet)
                else: 
                    message[letter_position] = offset_alphabet[offset]    
                break
        letter_position= letter_position + 1
 
    
    for rotor in rotors:
        rotor_alphabet = list(rotor)
        letter_position = 0
        for letter in message:
            offset_position = 0
            for offset_letter in offset_alphabet:
                if letter == offset_letter:
                    message[letter_position] = rotor_alphabet[offset_position]
                    break
                offset_position= offset_position + 1   
            letter_position= letter_position + 1         


if operation == 'DECODE':
       
    rotors.reverse()
    for rotor in rotors: 
        rotor_alphabet = list(rotor)
        letter_position = 0
        for letter in message:
            rotor_position = 0
            for rotor_letter in rotor_alphabet:
                if letter == rotor_letter:
                    message[letter_position] = offset_alphabet[rotor_position]
                    break
                rotor_position= rotor_position + 1 
            letter_position= letter_position + 1
    

    alphabet.reverse()
    offset_alphabet = alphabet
    letter_position = 0
    for letter in message:
        for offset_letter in offset_alphabet:
            if letter == offset_letter:
                offset = offset_input + letter_position + offset_alphabet.index(offset_letter)

                while offset >= len(offset_alphabet):
                    offset = offset - len(offset_alphabet)

                else: 

                    message[letter_position] = offset_alphabet[offset] 
      
                break
        letter_position= letter_position + 1


print( message, file=sys.stderr, flush=True)               
 
result = ''.join(message)

print(result)

