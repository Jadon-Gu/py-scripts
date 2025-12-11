from collections import Counter
import string

sentence = input('Enter a sentence: ').lower()
filtered = filter(str.isalpha,sentence)
counts = Counter(filtered)

for k in string.ascii_lowercase:
    if counts[k]:
        print(f'{k}: {counts[k]}')