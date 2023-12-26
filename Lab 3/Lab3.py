import sys
import math

def hex_to_bytes(hex_string):
    bytes_array = bytearray.fromhex(hex_string)
    return bytes_array

def calculate_xor(bytes1, bytes2):
    result = bytearray(len(bytes1))
    for i in range(len(bytes1)):
        result[i] = bytes1[i] ^ bytes2[i]
    return result

if __name__ == "__main__":
    message1 = input()
    message2 = input()
    message3 = input()

    message1 = hex_to_bytes(message1)
    message2 = hex_to_bytes(message2)
    message3 = hex_to_bytes(message3)

    alice_bob_key_xor = calculate_xor(message1, message3)
    bob_key = calculate_xor(message2, message3)
    decrypted_message = calculate_xor(bob_key, message1)

    text_message = decrypted_message.decode('utf-8')
    print(text_message)
