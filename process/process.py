import binascii
import math
import random
import sys
import json

def process_data(number,message):
    respond = {}

    #even/odd check
    num = int(number)
    if (num % 2) == 0:
        #even
        square_number = math.sqrt(num)
        respond['nPuzzle'] = square_number

    else:
        #odd
        cube_number = pow(num, 3)
        respond['nPuzzle'] = cube_number


    #Text Puzzle
    bmessage = bin(int(binascii.hexlify(message.encode()),16))[2:]
    vocals_count = sum(v in {"a", "A", "e", "E", "i", "I", "o", "O", "u", "U"} for v in message)

    respond['bmessage'] = bmessage
    respond['vocals'] = vocals_count

    respond['treasure'] = treasure_hunt(num)

    return json.dumps(respond)

def treasure_hunt(number):

    attemp = 0
    previous_numbers = set()

    while attemp < 5:

        guess_number = random.randint(1, 100)

        if guess_number in previous_numbers:
            continue
        previous_numbers.add(guess_number)

        if guess_number == number:
            #print('The number is: {}'.format(guess_number))
            return True
        else:
            #print('Attemp with {}'.format(guess_number))
            if attemp == 4:
                return False
        attemp += 1





if __name__ == '__main__':

    print(process_data(sys.argv[1], sys.argv[2]))

