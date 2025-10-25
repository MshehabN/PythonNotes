#Count how many vowels (a, e, i, o, u) are in a string.
allVowels = ('a', 'e', 'i', 'o', 'u')

def vowelCount(sentence):
    vowels = 0

    for letter in sentence.lower():
        if letter in allVowels:
            vowels = vowels +1
    return vowels

print(vowelCount("Count how many vowels"))
#i did it right, its just my vowels variable was spelled wrong