capital = 1000
import random

print('Print a random string containing 0 or 1:')
print('')


    # Starting values
input_length = 0
string = ''
minimal_length = 100


    # User input
while len(string) < minimal_length:
    user_input = input()
    user_input_list = [x for x in user_input if x == '1' or x == '0']
    user_input = ''.join(user_input_list)
    string += user_input
    input_length += len(user_input)
    if len(string) < 100:
        print(f'Current data length is {input_length}, {minimal_length - input_length} symbols left')
        print('Print a random string containing 0 or 1:')
    print('')


    # Final string
print('Final data string:')
print(string)
print('')
print("""You have $1000. Every time the system successfully predicts your '
next press, you lose $1.
Otherwise, you earn $1. Print "enough" to leave the game. Let's go!""")

    # Triads; slice string into substrings and count all occurrences including overlapping ones
triads = ('000', '001', '010', '011', '100', '101', '110', '111')
list_slices = []
for y in range(4):
    for x in range(len(string)//4):
        list_slices.append(string[0+x*4+y:4+x*4+y])

triad_dict = {triad: [list_slices.count(triad + '0'), list_slices.count(triad + '1')] for triad in triads}


    # Making prediction
def predict(sequence):
    output = random.choice(triads)
    c = 0
    while len(output) != len(sequence):
        first_triad = sequence[c:3 + c]
        next_char = triad_dict.get(first_triad)
        if next_char[0] > next_char[1]:
            output += '0'
        else:
            output += '1'
        c += 1
    return output


    # Second input
while True:
    print('Print a random string containing 0 or 1:\n')
    while True:
        test_string = (input())
        if '0' in test_string and '1' in test_string:
            break
        elif test_string == 'enough':
            print('Game over!')
            break
        elif '0' not in test_string or '1' not in test_string:
            continue
    if test_string == 'enough':
        break
    elif '0' in test_string and '1' in test_string:
        print('prediction:')
        prediction = predict(test_string)
        print(prediction)
        print('')

        # Calculating accuracy:
        counter = 3
        correct = 0
        for digit in test_string[3:]:
            if digit == prediction[counter]:
                correct += 1
                capital -= 1
            else:
                capital += 1
            counter += 1
        print(f'Computer guessed right {correct} out of {len(test_string[3:])} symbols ({(correct / len(test_string[3:]) * 100):.2f} %)')
        print(f"Your capital is now ${capital}")
