from pathlib import Path

path = Path('IO/guest.txt')

names = []
while True:
    name = input("What is your name? ")
    if (name == 'q'):
        break
    else:
        names.append(name)
contents = ''
for name in names:
    contents += f'{name}\n'
path.write_text(contents, encoding='utf-8')
