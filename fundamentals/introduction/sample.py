def sample_function_name(input_list):
    output_list = []
    # for i in range(0, len(input_list)):
    #     if input_list[i] >= 0:
    #         output_list.append(input_list[i])

    for number in input_list:
        if number >= 0:
            output_list.append(number)
    return output_list

# print('this is not in the function')
# print(sample_function_name([1, -3, 9, -2, 7]))

from random import randint

def roll_dice(number=1, sides=20):
    result = 0

    for i in range(0, number):
        result += randint(1, sides)

    return result

# print(roll_dice(3, 6))
# print(roll_dice())

def generate_new_character():

    character = {}

    character['STR'] = roll_dice(3, 6)
    character['DEX'] = roll_dice(3, 6)
    character['CON'] = roll_dice(3, 6)
    character['WIS'] = roll_dice(3, 6)
    character['INT'] = roll_dice(3, 6)
    character['CHA'] = roll_dice(3, 6)

    return character

new_character = generate_new_character()
print(new_character)