def sort_on(dict):
    return dict["num"]

def get_num_words(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    text = str.lower(text)
    character_dict = {}
    for letter in text:
        if letter not in character_dict:
            character_dict[letter] = 1
        else:
            character_dict[letter] += 1
    return character_dict


def get_sorted_list(character_dict):
    sorted_list = []
    for item in character_dict:
        sorted_list.append({"char" : item , "num" : character_dict[item]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
    
    
    return sorted_list