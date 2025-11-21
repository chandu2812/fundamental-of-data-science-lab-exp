import string
from collections import Counter

def calculate_frequency(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read()
            
        # 1. Normalization: Convert to lowercase to ensure 'Word' == 'word'
        text = text.lower()
        
        # 2. Cleaning: Remove punctuation
        # Creating a translation table is faster than regex for simple stripping
        translator = str.maketrans('', '', string.punctuation)
        text = text.translate(translator)
        
        # 3. Tokenization and Counting
        words = text.split()
        frequency = Counter(words)
        
        return frequency

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None

# Execution
result = calculate_frequency("sample_text.txt")

if result:
    # Print the 5 most common words for quick validation
    for word, count in result.most_common(5):
        print(f"{word}: {count}")