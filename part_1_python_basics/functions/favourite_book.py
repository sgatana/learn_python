def favourite_book(title):
    """Prints a message about a favourite book."""

    print(f"One of my favourite books is {title.title()}.")
    return title.title()


favourite_book('Python Crash Course')


def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet(pet_name='harry', animal_type='hamster')


def make_shirt(size='Large', message='I love Python'):
    print(f"the shirt of size '{size}' has a message '{message}'")


make_shirt('Medium', 'I love Python Programming')
make_shirt()


def build_profile(firstName, lastName, **userInfo):
    """Build a disctionary about the user"""
    userInfo['firstName'] = firstName
    userInfo['lastName'] = lastName
    return userInfo

user_profile = build_profile('albert', 'einstein', location='Kenya', field='Physics')
print(user_profile)