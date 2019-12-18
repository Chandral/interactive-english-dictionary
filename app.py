import json

data = json.load(open("data/data.json"))


def translate(dictionary_key):
    dictionary_key_lowercase = dictionary_key.lower()
    if dictionary_key_lowercase in data:
        return data[dictionary_key_lowercase]
    else:
        return "The word does not exist, please check your word."


word = input("Enter a word: ")
print(translate(word))
