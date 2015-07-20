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
sample_db = "../db/frf.sqlite"

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

# Clean out non-ints.
bad_entries = list()
for i in range(len(creature_size)):
    try:
        int(creature_size[i][0])
        int(creature_size[i][1])
        int(creature_size[i][2])
    except:
        bad_entries.append(i)
print("Unfiltered creature size: {}".format(len(creature_size)))

# Del from top to bottom to preserve the index.
# This could have been done above but was too clever for good code.
print bad_entries
for i in reversed(bad_entries):
    del creature_size[i]
print("Static-sized creature size: {}".format(len(creature_size)))


from matplotlib import pyplot as plt
from matplotlib import cm
import numpy as np

# Rudimentary sort and organization of relevant data.
cmc, powers, toughnesses = zip(*sorted(creature_size))

legend = ["cmc", "power", "toughness"]
xlabel = "cmc"
ylabel = "power"

#plt.legend(legend)
#plt.xlabel(xlabel)
#plt.ylabel(ylabel)

# clear plot
plt.clf()

bins = (max(powers), max(toughnesses))
heatmap, xedges, yedges = np.histogram2d(powers, toughnesses, bins=bins)
extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]

plt.axis([min(powers), max(powers), min(toughnesses), max(toughnesses)])

plt.imshow(heatmap, extent=extent, origin="lower", cmap=cm.get_cmap('spectral'))

cb = plt.colorbar()
cb.set_label('mean value')

plt.show()
