from collections import Counter

def count_word_frequency(file_path):
    # Read the content of the file
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Normalize the text to lower case and split into words
    words = text.lower().split()

    # Count the frequency of each word using Counter
    word_count = Counter(words)

    return word_count

def print_most_common_words(word_count, n=5):
    # Get the n most common words
    most_common = word_count.most_common(n)
    
    print(f'The {n} most common words are:')
    for word, count in most_common:
        print(f'{word}: {count}')

if __name__ == "__main__":
    # Specify the path to the text file
    file_path = 'textfile.txt'  # Ensure this file is in the same directory or provide the full path
    word_count = count_word_frequency(file_path)
    print_most_common_words(word_count)