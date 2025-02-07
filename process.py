import binascii
import math
import random
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

    treasure_hunt(number)

def treasure_hunt(number):

    attemp = 0
    previous_numbers = set()

    while True:
        guess_number = random.randint(1, 100)

        if guess_number in previous_numbers:
            continue
        previous_numbers.add(guess_number)

        if guess_number == number:
            print('The number is: {}'.format(guess_number))
            break
        else:
            print('Attemp with {}'.format(guess_number))
            attemp += 1
            if attemp == 5:
                break




    if attemp == 5:
        print('The number could not be guessed')
    else:
        print('Win')




if __name__ == '__main__':
    n = input()
    m = input()
    process_data(n,m)