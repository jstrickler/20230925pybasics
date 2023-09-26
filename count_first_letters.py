file_path = 'DATA/words.txt'

letter_counts = {}

with open(file_path) as words_in:
    for word in words_in:
        letter = word[0]
        if letter in letter_counts:
            letter_counts[letter] += 1
            #  letter_counts[letter] = letter_counts[letter] + 1
        else:
            letter_counts[letter] = 1
        #  letter_counts[letter] = letter_counts.get(letter, 0) + 1

for letter, count in letter_counts.items():
    print(letter, count)
