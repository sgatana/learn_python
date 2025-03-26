users = ['admin', 'alice', 'bob', 'cindy', 'david']
for user in users:
    if user == 'admin':
        print('Hello admin, would you like to see a status report?')
    else:
        print('Hello ' + user.title() + ', thank you for logging in again.')

# 5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is not empty.
# If the list is empty, print the message We need to find some users!
#
# 5-10. Checking Usernames: Do the following to create a program that simulates how websites ensure that everyone has a unique username.
# Make a list of five or more usernames called current_users.
# Make another list of five usernames called new_users. Make sure one or two of the new usernames are also in the current_users list.
# Loop through the new_users list to see if each new username has already been used. If it has, print a message that the person will need to enter a new username. If a username has not been used, print a message saying that the username is available.
# Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted.
#
# 5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
# Store the numbers 1 through 9 in a list.
# Loop through the list.    Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number. Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", and each result should be on a separate line.
#
# 5-12. Styling if statements: Review the programs you wrote in this chapter and make sure you styled your conditional tests appropriately.
# Make sure each conditional test includes a comparison operator, such as ==, >=, <=, >, or <. Also make sure each test evaluates to True or False.
# You should include at least one test with each of these operators.
#
# 5-13. Your Ideas: At this point, you're a more capable programmer than you were when you started this book. Now that you have a better sense of how real-world situations are modeled in programs, you might be thinking of some problems you could solve with your new programming skills. Record any new ideas you have about problems you might want to solve as your programming skills continue to improve. Consider games you might want to write, data sets you might want to explore, and web applications you'd like to create.
#

current_users = ['admin', 'alice', 'bob', 'cindy', 'david']
new_users = ['alice', 'bob', 'cindy', 'DAVID', 'eric']
print(current_users)

for user in new_users:
    if user.lower() in current_users:
        print('Sorry ' + user + ' is already taken, please enter a new username.')
    else:
        print('Congratulations ' + user + ' is available.')
