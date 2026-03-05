""" this file will read a large document and use built-in collections to create a word usage statistics """

import string
from operator import itemgetter

# FNAME = 'tomsawyer.txt'
FNAME = 'pridenprejudice.txt'

def read_dictionary():
    with open('words.txt', 'r') as words:
        all_words = words.read()
    all_words = all_words.lower() # make everything lower-case
    word_list = sorted(all_words.split())
    print('read',len(word_list),'dictionary words')
    return word_list

def remove_punctuation_translate(text):
    # Create a translation table that maps every punctuation character to None (effectively removing it)
    custom_punctuation = string.punctuation + '“' + '”' # add left and right quotes
    translator = str.maketrans('', '', custom_punctuation)    
    # Apply the translation table to the text
    return text.translate(translator)

def read_book():
    with open(FNAME, 'r', encoding="utf-8") as book:
        whole_book = book.read()
    whole_book = whole_book.lower() # make everything lowercase    
    whole_book = remove_punctuation_translate(whole_book) # remove punctuation
    tom_sawyer_words = whole_book.split() # splits book into list of words
    print(FNAME, len(tom_sawyer_words),'words.')
    return tom_sawyer_words

def binary_search(word_list, target_word):
    """
    Performs an iterative binary search on a sorted list of words.
    Returns the index of the target_word if found, otherwise -1.
    """
    # Binary search requires a sorted list
    # If the list isn't sorted, this implementation won't work correctly.
    # For a fresh list, sort it first: word_list.sort() 
    left = 0
    right = len(word_list) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_word = word_list[mid]

        if mid_word == target_word:
            return mid  # Target found, return index
        elif mid_word < target_word:
            left = mid + 1  # Target is in the right half
        else:
            right = mid - 1 # Target is in the left half

    return -1 # Target not found

dictionary_words = read_dictionary() # read in all the words in the dictionary
book_words = read_book() # read in all the words in the book

# if word in book and dictionary add it to common words list else add to uncommmon_words
uncommon_words = []
common_words = []
for word in book_words:
    if binary_search(dictionary_words, word) >= 0:
        common_words.append(word)
    else:
        uncommon_words.append(word)

print(f"\n{FNAME} has {len(common_words)} common words and {len(uncommon_words)} words not in the dictionary.")

# Create a set of common unique words
common_unique_words = set()
for word in common_words:
    common_unique_words.add(word)
print(f'{FNAME} has {len(common_unique_words)} unique common words.')

# Create a set of uncommon unique words
uncommon_unique_words = set()
# TODO: create a set of uncommon (not in dictionary) words

# initialize common word frequency dictionary
common_word_frequency = dict()
for word in common_words:
    if word in common_word_frequency:
        common_word_frequency[word] += 1
    else:
        common_word_frequency[word] = 1

# intiialize uncommon word frequency dictionary
uncommon_word_frequency = dict()
# TODO: Complete uncommon word frequency dictionary

# Sort common words by frequency in ascending order
sorted_items = sorted(common_word_frequency.items(), key=itemgetter(1))
common_sorted_dict = dict(sorted_items)

# Sort uncommon words by frequency in ascending order
sorted_items = sorted(uncommon_word_frequency.items(), key=itemgetter(1))
uncommon_sorted_dict = dict(sorted_items)

# grab the 50 most used common words
common_keys_50 = list(common_sorted_dict.keys())[-50:-1]
print('\nCommon Words:')
columns = 0
for word in common_keys_50:    
    print(f'{word:15s} {common_sorted_dict.get(word):5d}     ',end="")
    columns += 1
    if columns % 3 == 0:
        print()

# grab the 50 most used uncommon words
uncommon_keys_50 = list(uncommon_sorted_dict.keys())[-50:-1]
print('\n\nUncommon Words:')
# TODO: Complete list of 50 most used uncommon words