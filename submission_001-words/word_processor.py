import string

def split(delimiters, text):
    """
    Splits a string using all the delimiters supplied as input string
    :param delimiters:
    :param text: string containing delimiters to use to split the string, e.g. `,;? `
    :return: a list of words from splitting text using the delimiters
    """

    import re
    regex_pattern = '|'.join(map(re.escape, delimiters))
    return re.split(regex_pattern, text, 0)


def convert_to_word_list(text):

    '''
    This function converts a given sting "text" to a list and it removes all punctuation.
    '''

    word_to_list = (lambda text: text.lower().translate(str.maketrans("","",string.punctuation)).split())
    
    return word_to_list(text)


def words_longer_than(length, text):

    '''
    This function takes two parameters it asks for length.
    It returns a list of words greater than the given length.
    '''

    filtered_words = list(filter(lambda text: len(text) > length, text.lower().translate
(str.maketrans("","",string.punctuation)).split()))
    
    return filtered_words


def words_lengths_map(text):

    '''
    This function returns a dictionary where the key is the length of a word in a given string.
    The value is the ammount of times that word length occurs in the string.
    '''

    list_of_lengths = list(map(lambda text: len(text), text.lower().translate
(str.maketrans("","",string.punctuation)).split()))
    set_of_lengths = set(list_of_lengths)
    dict_length_occurence = {key:list_of_lengths.count(key) for key in set_of_lengths}
    
    return dict_length_occurence


def letters_count_map(text):

    '''
    This function returns the ammount of each letter in a given string.
    '''
    
    letters = string.ascii_lowercase
    word_to_list = text.lower()
    dict_number_of_letters = {key:word_to_list.count(key) for key in letters}
    
    return dict_number_of_letters


def most_used_character(text):

    '''
    This function returns the letters that occurs the most in a string.
    '''
    
    if text == "":
        return None
    else:
        letters = string.ascii_lowercase
        word_to_list = text.lower()
        dict_number_of_letters = {key:word_to_list.count(key) for key in letters}
        popular_letters = max(dict_number_of_letters, key = dict_number_of_letters.get)
    
        return popular_letters


if __name__ == '__main__':

    text = "These are indeed interesting, an obvious understatement, times. What say you?"
    
    word_to_list = convert_to_word_list(text)
    #print(word_to_list)
    
    filtered_words = words_longer_than(10, text)
    #print(filtered_words)

    dict_length_occurence = words_lengths_map(text)
    #print(dict_length_occurence)
    
    dict_number_of_letters = letters_count_map(text)
    #print(dict_number_of_letters)

    popular_letters = most_used_character(text)
    #print(popular_letters)