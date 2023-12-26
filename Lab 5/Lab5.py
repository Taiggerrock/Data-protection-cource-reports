# Good Luck!
def encode(string):
    bits = ""

    for char in string:
        ascii_value = ord(char)
        binary_value = format(ascii_value, '08b')

        tripled_bits = "".join([bit * 3 for bit in binary_value])
        bits += tripled_bits

    return bits


def decode(bits):
    string = ""

    for i in range(0, len(bits), 24):
        triple = bits[i:i+24]

        corrected_bits = ""
        for j in range(0, len(triple), 3):
            bit_group = triple[j:j+3]
            corrected_bit = max(set(bit_group), key=bit_group.count)
            corrected_bits += corrected_bit

        for k in range(0, len(corrected_bits), 8):
            binary_byte = corrected_bits[k:k+8]
            ascii_value = int(binary_byte, 2)
            decoded_char = chr(ascii_value)
            string += decoded_char

    return string


if __name__ == "__main__":
    text = input()
    encoded_text = encode(text)
    decoded_text = decode(encoded_text)

    print("Text:", text)
    print("Encoded text:", encoded_text)
    print("Decoded text:", decoded_text)
