def count_words(entire_text):
    return len(entire_text.split())

def count_characters(entire_text):
    lower_text = entire_text.lower()
    char_count_dictionary = {}
    for i in range(0, len(lower_text)):
        if lower_text[i] in char_count_dictionary:
            char_count_dictionary[lower_text[i]] += 1
        else:
            char_count_dictionary[lower_text[i]] = 1
    return char_count_dictionary

def sort_on(items):
    return items["num"]

def sort_character_dictionary(character_dictionary):
    list_of_dictionaries = []
    for key in character_dictionary:
        inner_dictionary = {}
        inner_dictionary["char"] = key
        inner_dictionary["num"] = character_dictionary[key]
        list_of_dictionaries.append(inner_dictionary)
        list_of_dictionaries.sort(reverse=True, key=sort_on)
    return list_of_dictionaries