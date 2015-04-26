"""
Perform word frequency analysis for the ability text on each card in a given set.

This utility accepts a list of strings and returns a dictionary of words.

In order to send in a list of strings, use the convert_to_frequency_dict() method.

This utility does accept an alternate separator but does not clean the text.

You may consider cleaning the text of: punctuation, capitalization before passing
it to the convert_to_frequency_dict() method.
"""



def create_frequency_dict(sourcetext, sep=' '):
    """ Accepts a string and returns a frequency dictionary

    NOTE: This does not preprocess the string. Any preprocessing, such as
    reducing to lower case, must be done prior to using this function.

    Default separator is a space.
    """
    source_fdict = dict()
    sourcelist = sourcetext.split(sep)
    
    for word in sourcelist:
        source_fdict[word] = source_fdict.get(word, 0) + 1

    return source_fdict


def merge_frequency_dicts(*args):
    """ accepts any number of word frequency dictionaries and merges them.
    
    """
    aggregate_dictionary = dict()

    for fdict in args:
        for k,v in fdict.iteritems():
            aggregate_dictionary[k] += aggregate_dictionary.get(k, 0) + v

    return aggregate_dictionary


def convert_to_frequency_dict(listofstrings, sep=' '):
    """ Pass in a list of strings and get back a word frequency dict

    This is a utility function to manage a compound datastructure alongside
    the simpler methods in this library
    """
    partial_fdicts = list()

    for sourcetext in listofstrings:
        partial_fdicts.append(create_frequency_dict(sourcetext, sep))

    return merge_frequency_dicts(partial_fdicts)




