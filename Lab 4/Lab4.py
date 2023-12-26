import hashlib

def calculate_md5(input_str):
    md5 = hashlib.md5()
    md5.update(input_str.encode('utf-8'))
    return md5.hexdigest()

def decode(hash):
    for candidate in range(10**5):
        input_str = f"{candidate:05d}"
        hashed_input = calculate_md5(input_str)

        if hashed_input == hash:
            return input_str
    return None

def crack(hash):
    result = decode(hash)
    return result
