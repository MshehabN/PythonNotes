#reverse all words in a string and keep the order

def reversedWords(sentence):
    wordList = []
    reversedSentence = sentence.split() #turns the sentence into a list
    for word in reversedSentence:
        revWord = word[::-1]
        wordList.append(revWord)   #mistake here, its list.append(item) but i did item.append(list)
    sentence2 = " ".join(wordList) #forgot to join the sentence together
    return sentence2

print(reversedWords("reverse all words in a string and keep the order"))
