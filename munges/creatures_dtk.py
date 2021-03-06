"""
Gather all the ability text for a provided sqlite db and generate a
word frequency dict for it.
"""
import sqlite3
import re
import utils.wordfreq
import copy

# This uses a symlink, may break in non posix.
# use os.path.join here if you wish.
sample_db = "../db/dtk.sqlite"

def clean_text(dirtytext):
    """ Apply various cleaning to the text.

    This function was used when cleaning bizarre characters out of the ability text.
    There may be information lost if you use this function. KNOW YOUR DATABASE.
    """
    allowed_chars = r"[^a-zA-Z0-9'/{}+-]"
    repl_char = ' '

    cleantext = re.sub(allowed_chars, repl_char, dirtytext)

    # lowercase only
    cleantext = cleantext.lower()

    return cleantext
    
"""
# ditch the tuple wrapping in each item of the list.
# utils.wordfreq.convert_to_frequency_dict requires a list of strings.
ability_strings = list()
for tuple_wrapped_string in ability_list:
    ability_strings.append(clean_text(tuple_wrapped_string[0].encode('utf-8')))
"""
"""
ability_freq_dict = utils.wordfreq.convert_to_frequency_dict(ability_strings)

sorted_ability_words = sorted([(v,k) for k,v in ability_freq_dict.iteritems()])


for c,i in reversed(sorted_ability_words):
    print c, i
"""

def try_int(v):
    """ Convert to an int and return input on ValueError.
    """
    try:
        v = int(v)
    except ValueError:
        pass
    return v

statement = "select Nname,Nconverted_manacost,Npower,Ntoughness from Ncards where Npower<>'' or Ntoughness<>''"

conn = sqlite3.connect(sample_db)
cur = conn.cursor()

cur.execute(statement)
fetched_cards = cur.fetchall()

names, cmc, powers, toughnesses = zip(*fetched_cards)
names = list(names)
# Map to int if possible with try_int
cmc = map(try_int, cmc)
powers = map(try_int, powers)
toughnesses = map(try_int, toughnesses)


# Test if all card names are unique.
names_test = copy.deepcopy(names)
while len(names_test) > 0:
    name = names_test.pop()
    if name in names_test:
        print("Names has a nonunique: {}".format(name))
print("All card names are unique, {} cards.".format(len(names)))

creature_size = zip(cmc, powers, toughnesses)
print sorted(creature_size)

import numpy as np
from matplotlib import pyplot as plt

print cmc

plt.bar(range(len(cmc)), sorted(cmc))
plt.show()
