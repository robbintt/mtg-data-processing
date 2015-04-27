"""
Gather all the ability text for a provided sqlite db and generate a
word frequency dict for it.
"""
import sqlite3
import re
import utils.wordfreq

def clean_text(dirtytext):
    """ Apply various cleaning to the text.

    """
    allowed_chars = r'[^-a-zA-Z0-9]'
    repl_char = ' '

    cleantext = re.sub(allowed_chars, repl_char, dirtytext)

    # lowercase only
    cleantext = cleantext.lower()

    return cleantext
    

# posix only for now
mydb = "../db/standard.sqlite"

statement = 'select Nability from Ncards'

conn = sqlite3.connect(mydb)
cur = conn.cursor()

#cur.execute('select * from Ncards')
#cur.execute('select Nability from Ncards', selection)
cur.execute(statement)

ability_list = cur.fetchall()

# ditch the tuple wrapping in each item of the list.
# utils.wordfreq.convert_to_frequency_dict requires a list of strings.
ability_strings = list()
for tuple_wrapped_string in ability_list:
    ability_strings.append(clean_text(tuple_wrapped_string[0].encode('utf-8')))

ability_freq_dict = utils.wordfreq.convert_to_frequency_dict(ability_strings)

sorted_ability_words = sorted([(v,k) for k,v in ability_freq_dict.iteritems()])


for c,i in reversed(sorted_ability_words):
    print c, i
