def spin_words(sentence):
        listWords = []
        words = sentence.split()
        for word in words:
            strLength = len(word)
            if strLength >= 5:
                listWords.append(word[::-1])
            else:
                listWords.append(word)
        sentence2 = " ".join(listWords)
        return sentence2

print(spin_words("helloo my name is shehab"))



#the .join() function joins a LIST of strings together into a sentence
#how to use the .join() function
#SEPARATOR.join(LIST_OF_STRINGS)