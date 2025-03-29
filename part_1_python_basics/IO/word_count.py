from pathlib import Path


def count_words(filePath):
    """Count the approximate number of words in a file."""
    try:
        content = filePath.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass
        # print(f"Sorry, the file {filePath} does not exist.")
    else:
        words = content.split()
        num_words = len(words)
        file_name = filePath.name
        print(
            f"The file {file_name} has about {num_words} words.")
        return num_words


filenames = ['guest.txt',  'programming.txt', 'pi_digits.txt']

for filename in filenames:
    path = Path(f"IO/{filename}")
    count_words(path)
