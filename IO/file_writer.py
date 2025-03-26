from pathlib import Path

path = Path('IO/write_message.txt')

contents = 'I love coding.\n'
contents += 'I love programming.\n'
contents += 'I love creating new games.\n'
contents += 'I love solving problems.\n'
contents += 'I love working with data.\n'

path.write_text(contents)
