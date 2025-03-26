def get_number(prompt):
    while True:
        user_input = input(prompt)
        if user_input == 'q':
            return None
        try:
            return int(user_input)
        except ValueError:
            print('Invalid input')

while True:
    first_number = get_number('Enter a number: ')
    if first_number is None:
        break

    second_number = get_number('Enter another number: ')
    if second_number is None:
        break

    print(f'The sum of {first_number} and {second_number} is {first_number + second_number}')