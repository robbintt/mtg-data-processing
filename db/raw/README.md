
# If you receive error near line 1 "" syntax error, you can likely ignore it.
# `Error: near line 1: near "": syntax error`

Instructions:

1. Use Gatherer Extractor and export as .sql. Put the file in this directory.
2. Run the converter script on the sql dump. This will provide a sqlite file.
3. (Optional) Run the get_dbinfo.sqlite script according to instructions in the shell files.
4. Put the sqlite file where you want it for use.


Issues:
Sqlite supports about 500 records in a single insert. If you have more, you will have to manually break it up into more inserts with fewer records per insert.

After Magic: Origins, the set data was not updated in Gatherer Extractor. I manually updated it in the gatherer extractor set data in menu->options->Booster packaging.
