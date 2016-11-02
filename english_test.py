#!/usr/bin/python3
import random

candidateWords = ('POTATO', 'SMALL', 'NAME', 'YES', 'DAY')
questions = ('How many letters does the word contain? ', 'How many vowels does the word contain? ',
             'How many consonants does the word contain? ', 'What is letter 3 of the word? ',
             'How many letters does the word contain? ')
print("Welcome to English Tester Pro!\n")
wordList = random.sample(candidateWords, 5)  # randomize tuples
score = 0


def countVowelsOrConsonants(string, vowels=True):
    """Method for getting Vowels or Consonants
    Args:
            string: string from which user wants to count number vowels or consonant.
            vowels: Optional parameter, by default its true if user pass false then method will count consonant.
    Returns:
            count of vowels or consonant
    """
    return sum(
        (1 for x in string if x.lower() in 'aeiou') if vowels else (1 for x in string if x.lower() not in 'aeiou'))


def findResult(x, word):
    """Method used for performing some operations on word like length of word, count vowel, count consonant etc.
    Args:
            x: index of dictionary .
            word: On which the operation will be perform.
    Returns:
            length of word, count vowel, count consonant, word on 3rd position, length of word
    """
    return {
        0: len(word),
        1: countVowelsOrConsonants(word),
        2: countVowelsOrConsonants(word, False),
        3: word[2:3],
        4: len(word),
    }[x]


for i, q in enumerate(questions):
    word = wordList[i]
    print("Word %d/5: %s" % (i + 1, word))
    while True:
        try:
            user_answer = input(q).upper()
            if i == 3:
                try:
                    int(user_answer)
                    print("Invalid input...")
                except ValueError:
                    break
            else:
                user_answer = int(user_answer)
                break
        except ValueError:
            print("Invalid Input...")
    res = findResult(i, word)
    if user_answer == res:
        print("Correct!")
        score += 1
    else:
        print("Incorrect! Correct answer was %s" % res)

print("Game Over. Your score is %d/5" % score)
