def count_vowels(word):       # linha 1
    vowels = 'aeiou'          # linha 2
    count = 0                 # linha 3
    for letter in word:       # linha 4
        if letter in vowels:  # linha 5
            count += 1        # linha 6
    return count              # linha 7


count_vowels(input('Word:'))    # linha 10


#I - Na linha #7 a expressão count > 0 sempre resulta em True.
#II - Na linha #2 a expressão count == 0 sempre resulta em NameError.
#III - Na linha #7 a expressão vowels == 'aeiou' sempre resulta em True.

#Quais dessas afirmativas estão corretas?

#R:2,3