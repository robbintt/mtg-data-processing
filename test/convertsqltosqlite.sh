#!/bin/bash


# Perl command to convert windows to unix newlines
# FROM: https://kb.iu.edu/d/acux
# perl -p -e 's/\r$//' < winfile.txt > unixfile.txt
# UNTESTED TAR 042015


sed --in-place=.win "s//\n/g" $1
