#!/bin/bash

# USAGE: As 1st argument to this script, specify your .sql dump from Gatherer Extractor.
# VERIFICATION: run get_dbinfo.sqlite after loading your new .sqlite db into sqlite3:
#               # sqlite3 <the_new_db>.sqlite
#               > .read get_dbinfo.sqlite

# Perl command to convert windows to unix newlines
# FROM: https://kb.iu.edu/d/acux
# perl -p -e 's/\r$//' < winfile.txt > unixfile.txt
# UNTESTED TAR 042015

# Convert to unix format newlines
sed --in-place=.win "s//\n/g" $1

# Prime file with output DB.
sqlite_filename="${1}ite"
sed --in-place "1s/\(.\)/\1.attach $sqlite_filename as mydb;\n/" $1

sqlite3 $sqlite_filename < $1

