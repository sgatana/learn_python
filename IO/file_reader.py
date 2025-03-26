from pathlib import Path

path = Path("IO/pi_digits.txt")

contents = path.read_text(encoding='utf-8')
# print(f'{contents.rstrip()}\n')

lines = contents.splitlines()
for indx, line in enumerate(lines):
    print(f'{indx + 1}. {line}')


pi_string = ''

for line in lines:
    pi_string += line.strip()

print(pi_string)
print('string length:', len(pi_string))
