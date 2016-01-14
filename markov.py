from random import choice
import sys


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    file_name = open(file_path)
    contents = file_name.read()
    file_name.close()

    return contents


def make_chains(text_string, n):
    """Takes input text as string; returns _dictionary_ of markov chains with n-gram keys.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}

    words = text_string.split()

    for index in range(len(words) - n):
        word_gram = []

        for i in range(n):
            word_gram.append(words[index + i])
        word_gram = tuple(word_gram)

        if word_gram not in chains:
            chains[word_gram] = [words[index + n]]

        else:
            chains[word_gram].append(words[index + n])

    return chains


def make_text(chains, n):
    """Takes dictionary of markov chains with n-gram keys; returns random text."""
    
    while True:
        # We're choosing a random tuple key from our dictionary, chains.
        # If the first word in the random tuple key is capitalized, go forward.
        link = choice(chains.keys())
        if link[0].istitle():
            break

    # Converting our tuple key to a list so we can join the words in our resulting text.
    link_list = list(link)

    # While our tuple key is found in our chains dictionary,
    # Choose a random word from the list of values found at that key.
    # Add that random word to our list of words.
    # We convert the tuple key slice from index 1 to the end into a list,
    # And add the random word to create a new key link, which is converted back to a tuple.
    # Finally, we combine all words in our list to make a long string (Markov text!)
    while link in chains:
        random_word = choice(chains[link])
        link_list.append(random_word)

        link_temp = list(link[1:])
        link_temp.append(random_word)
        link = tuple(link_temp)
        
        text = " ".join(link_list)

    return text


input_path = sys.argv[1]


# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text, int(sys.argv[2]))

# Produce random text
random_text = make_text(chains, int(sys.argv[2]))

print random_text
