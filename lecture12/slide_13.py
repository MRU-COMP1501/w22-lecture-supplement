# Write a function that takes any string as input, 
# then counts how many vowels (a, e, i, o, u) are in it. 
# Then, print out the vowel count as a percentage of the total number of letters.
# Hint: we need to loop through all the letters to check them individually

def vowel_percentage(word):
    vowel_count = 0
    for letter in word:
        if letter in 'aeiou':
            vowel_count += 1 # could do vowel_count = vowel_count + 1

    print(f'Vowel percentage: {vowel_count / len(word):.1%}')

def main():
    word = input('Enter a word: ')
    vowel_percentage(word)

main()