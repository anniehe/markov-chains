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
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}

    words = text_string.split()

    # SOLUTION FOR A BI-GRAM

    # We want to stay within range for index + 2, as used below.
    # for index in range(len(words) - 2):
        
    #     word_pair = (words[index], words[index + 1])
        
    #     if word_pair not in chains:
    #         chains[word_pair] = [words[index + 2]]

    #     else:
    #         chains[word_pair].append(words[index + 2])

    for index in range(len(words) - n):
        word_gram = []

        for i in range(n):
            word_gram.append(words[index + i])
        word_gram = tuple(word_gram)

        if word_gram not in chains:
            chains[word_gram] = [words[index + n]]

        else:
            chains[word_gram].append(words[index + n])

    #print chains

    return chains


def make_text(chains, n):
    """Takes dictionary of markov chains; returns random text."""

    text = ""
    
    while True:
        link = choice(chains.keys())
        if link[0].istitle():
            break

    # SOLUTION FOR A BI-GRAM
    # text = link[0] + " " + link[1]

    # while link in chains:
    #     random_word = choice(chains.get(link))
    #     text = text + " " + random_word
    #     link = (link[1], random_word)

    for i in range(n):
        text = " ".join(link[i])

    while link in chains:
        random_word = choice(chains.get(link))
        text = text + " " + random_word
        link = (link[n - 1], random_word)

    return text


input_path = sys.argv[1]


# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text, int(sys.argv[2]))

# Produce random text
random_text = make_text(chains, int(sys.argv[2]))

print random_text
