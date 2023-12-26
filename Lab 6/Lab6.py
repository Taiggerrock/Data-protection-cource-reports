import numpy as np

def scanner(qrcode):
    qr_matrix = np.zeros((21, 21), dtype=int)

    for index_i, row_data in enumerate(qrcode):
        for index_j, value in enumerate(row_data):
            qr_matrix[index_i, index_j] = 1 - value if (index_i + index_j) % 2 == 0 else value

    qr_matrix = qr_matrix[9:]
    odd_flag, decoded_data = 0, []

    for index in [19, 17, 15, 13]:
        column_data = qr_matrix[:, index:index+2]
        direction = 1 if odd_flag == 1 else -1
        decoded_data.extend(column_data[::direction, ::-1].flatten())
        odd_flag = 1 - odd_flag

    decoded_data = ''.join(map(str, decoded_data[4:]))
    num_letters = int(decoded_data[:8], 2)
    decoded_data = decoded_data[8:]

    result = ''
    for index in range(0, num_letters * 8, 8):
        result += chr(int(decoded_data[index:index+8], 2))

    return result
