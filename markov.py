from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    file_name = open(file_path)
    contents = file_name.read()
    file_name.close()

    return contents


def make_chains(text_string):
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

    for index in range(len(words) - 1):
        
        # We want the index for the value of the next word to stay within range.
        if index + 2 > len(words) - 1:
            break
        
        word_pair = (words[index], words[index + 1])
        
        if word_pair not in chains:
            next_word = [words[index + 2]]
            chains[word_pair] = next_word

        else:
            chains[word_pair].append(words[index + 2])

    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""
    

    link = choice(chains.keys())
    text = link[0] + " " + link[1]

    random_word = choice(chains.get(link))
    text = text + " " + random_word
    new_key = (link[1], random_word)
    last_key = ("Sam", "I")
    
    for new_key in chains:
        next_random_word = choice(chains.get(new_key))
        text = text + " " + next_random_word
        new_key = (new_key[1], next_random_word)
    
        if new_key == last_key:
            break

    #print "text is now ", text
    #print "link is ", link
    #print "new key is ", new_key

    return text
   
#Make a new key out of the second word in the first key and the random word you pulled out from the list of words that followed it.
#Look up that new key in the dictionary, and pull a new random word out of the new list.
#Keep doing that until your program raises a KeyError.


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
