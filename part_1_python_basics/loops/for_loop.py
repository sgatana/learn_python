# fruits = ['Apple', 'Peach', 'Mango'];
# for fruit in fruits:
#     print(fruit)

student_scores = [1, 5, 15, 27]
# print(max(student_scores));
max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score

print(max_score)

sum = 0
for number in range(1, 101):
    sum += number

print(sum)
