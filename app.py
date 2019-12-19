import json
from difflib import get_close_matches

data = json.load(open("data/data.json"))


def translate(dictionary_key):
    negative_response = "The word '{}' does not exist in the dictionary. " \
                        "Please check your word and then try again, thank you.".format(dictionary_key)
    dictionary_key_lowercase = dictionary_key.lower()

    if dictionary_key_lowercase in data:
        return data[dictionary_key_lowercase]
    elif len(get_close_matches(dictionary_key, data.keys())) > 0:
        yes_or_no = input("Did you mean '{}'? Type 'Y' for yes or 'N' for no: "
                          .format(get_close_matches(dictionary_key, data.keys())[0]))
        if yes_or_no.upper() == 'Y':
            return data[get_close_matches(dictionary_key, data.keys())[0]]
        elif yes_or_no.upper() == 'N':
            return negative_response
        else:
            return "Not sure what you meant, please type either 'Y' for yes or 'N' for no"
    else:
        return negative_response


word = input("Enter word: ")
search_result = translate(word)

if type(search_result) == list:
    for item in search_result:
        print(item)
else:
    print(search_result)
