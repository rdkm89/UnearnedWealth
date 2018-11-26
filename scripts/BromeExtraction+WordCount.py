# A very quick way to extract individual characters lines from Brome plays
# Last modified: 2018-11-13

# Import required packages, modules
from bs4 import BeautifulSoup
import pandas as pd
from os import listdir
import os

# Define functions
def list_textfiles(directory):
        "Return a list of filenames ending in '.txt' in DIRECTORY."
        textfiles = []
        for filename in listdir(directory):
            if filename.endswith(".txt"):
                textfiles.append(filename)
        return textfiles

def countwords(fp):
    """ Count word length of text file """
   fh = open(fp)
   words = len(fh.read().split(" "))
   fh.close()
   return words

# Set path to corpus; list filenames; join with directory
CORPUS_PATH = "/Users/au564346/Desktop/split/"
filenames = list_textfiles(CORPUS_PATH)
filenames_with_path = [os.path.join(CORPUS_PATH, fn) for fn in filenames]

# Extraction loop - this is really messy and slow! Can be massively optimised!!
for filename in filenames_with_path:

    # read text; create BeautifulSoup instance
    raw = open(filename, encoding = 'utf8').read()
    soup = BeautifulSoup(raw, 'lxml')

    # create list of characters based on lines
    idList = []
    for a in soup.findAll('sp'):
        if 'who' in a.attrs.keys():
            idList.append(a.attrs['who'])

    # Only unique characters
    unique = set(idList)

    for speaker in unique:

            """
            I hate this all of this For-loop. It's so slow and ugly. Can't quite figure out the
            logic to get rid of it right now, though, so it'll need to do. However, for anything
            more than the 16 Brome plays, this really isn't good.
            """

        lines = []
        for test in soup.findAll(who=speaker):

            for line in test(['l', 'p']):
                text = line.text
                lines.append(text)

                words = []
                for word in lines:
                    word = word.replace('\n', ' ').replace('\r', '')
                    words.append(word)

                    with open("/Users/au564346/Desktop/split/"+speaker+".txt", 'w+', encoding='utf8')as f:
                        for inner_list in words:
                            f.write("".join(inner_list)+"")

# Point to split files
SPLIT_PATH = "/Users/au564346/Desktop/split/"
split_files = list_textfiles(SPLIT_PATH)
split_files_with_path = [os.path.join(SPLIT_PATH, fn) for fn in split_files]

# Calculate lengths using countwords()
lengths = [countwords(file) for file in split_files]

# Check integrity!
len(lengths) == len(filenames)

# Create dataframe
data = pd.DataFrame(
    {'character': filenames,
     'word_count': lengths
    })

# Save
data.to_csv("/Users/au564346/Desktop/word_counts.csv", sep="\t")

"""
####
BETTER LOOPING!
####
"""

filename = "/Users/au564346/Documents/datasets/english/Drama/EarlyPrint/SHC/A16923.xml"

# read text; create BeautifulSoup instance using XML parser
raw = open(filename, encoding = 'utf8').read()
soup = BeautifulSoup(raw, 'lxml')

# create list of characters based on lines
idList = []
for a in soup.findAll('sp'):
    if 'who' in a.attrs.keys():
        idList.append(a.attrs['who'])

# Only unique characters
unique = set(idList)

speaker = 'A16923-blaze'

for speaker in unique:

text = [line.text for text in text(['l', 'p']) for text in soup.findAll(who=speaker)]
words = [word.replace('\n', ' ').replace('\r', '') for word in lines]
