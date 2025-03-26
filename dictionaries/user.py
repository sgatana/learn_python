# user = {
#     'username': 'admin',
#     'role': 'admin',
#     'password': 'admin123',
#     'email': 'admin.mail.com'
# }

# for key, value in user.items():
#     print(f'\nKey: {key}')
#     print(f'Value: {value}')


# username = user.get('username', 'No username found.')
# username = user.get('name', 'No name found.')
# print(username)

responses = {}

polling_active = True

while polling_active:
    name = input("What is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")
