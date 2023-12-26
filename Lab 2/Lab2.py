def decode_message(encoded_message):
    shift = calculate_shift(encoded_message)
    decoded_message = ""

    for character in encoded_message:
        if character.isalpha():
            base_character = 'A' if character.isupper() else 'a'
            decoded_char = chr(((ord(character) - ord(base_character) - shift + 26) % 26) + ord(base_character))
            decoded_message += decoded_char
        else:
            decoded_message += character

    return decoded_message

def calculate_shift(encoded_message):
    letter_frequencies = [8.167, 1.492, 2.782, 4.253, 12.702, 2.228, 2.015, 6.094, 6.966, 0.153, 0.772, 4.025, 2.406, 6.749, 7.507, 1.929, 0.095, 5.987, 6.327, 9.056, 2.758, 0.978, 2.360, 0.150, 1.974, 0.074]
    best_shift = 0
    best_score = float("-inf")

    for shift in range(26):
        score = 0
        for character in encoded_message:
            if character.isalpha():
                base_character = 'A' if character.isupper() else 'a'
                index = (ord(character) - ord(base_character) - shift + 26) % 26
                score += letter_frequencies[index]

        if score > best_score:
            best_score = score
            best_shift = shift

    return best_shift

if __name__ == "__main__":
    message = input()
    decoded_message = decode_message(message)
    print(decoded_message)
