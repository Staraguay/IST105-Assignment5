import binascii
import math
from struct import pack_into


def process_data(number,message):
    #even/odd check
    num = int(number)
    if (num % 2) == 0:
        #even
        square_number = math.sqrt(num)
        print(square_number)
    else:
        #odd
        cube_number = pow(num, 3)
        print(cube_number)

    #Text Puzzle
    bmessage = bin(int(binascii.hexlify(message.encode()),16))[2:]
    vocals_count = sum(v in {"a", "A", "e", "E", "i", "I", "o", "O", "u", "U"} for v in message)
    print(bmessage)
    print(vocals_count)


if __name__ == '__main__':
    n = input()
    m = input()
    process_data(n,m)