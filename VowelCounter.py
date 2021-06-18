vowelList = "aeıioöuü"
vowelMeter = 0
countWord = input("Please enter for word to count: ")

for word in countWord:
    if word in vowelList:
        vowelMeter += 1

if vowelMeter == 1:
    print(f"There are {vowelMeter} vowel in the word {countWord}.")
else:
    print(f"There are {vowelMeter} vowels in the word {countWord}.")
