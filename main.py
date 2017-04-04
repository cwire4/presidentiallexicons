from __future__ import absolute_import, division, print_function

import codecs
import glob
import operator
import os
from collections import defaultdict

import nltk


def sentence_to_wordlist(raw):
    clean = raw.lower()
    cleaned_words = clean.split()
    return cleaned_words

# @todo So much nesting this code should be executed in a forest. Let's update this.
for root, dirs, files in os.walk("transcripts"):
    # You are -->> Here
    path = root.split(os.sep)

    # For Every Dir in Transcripts
    for directory in dirs:
        # Initialize
        total_word_count = 0

        # All txt files in this Dir e.g. gwbush
        individualPath = path[0] + "/" + directory + "/*.txt"

        # Get list of sorted Transcript files
        transcripts = sorted(glob.glob(individualPath))
        transcript_count = len(transcripts)

        # All the cool kids use Unicode
        corpus_raw = u""

        # Let's look at each transcript file
        for transcript in transcripts:

            # Keep track of number of transcripts
            # @todo Just get transcripts count from size of transcripts array
            # transcript_count += 1

            # Open file for reading
            with codecs.open(transcript, 'r', 'utf-8') as transcript_file:
                corpus_raw += transcript_file.read()

            # Setup tokenization
            tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

            # Grab sentences by their ...
            raw_sentences = tokenizer.tokenize(corpus_raw)

            # Initialize
            words = defaultdict(int)
            word_length = defaultdict(int)

            # Let's look at each sentence
            for sentence in raw_sentences:

                # Sentences gotta sentence
                if len(sentence) > 0:

                    # Split up the words
                    word_tokenization = sentence_to_wordlist(sentence)

                    # Gettin Loopy With Loops(tm), Let's evaluate each word.
                    # @todo is there a method to do this rather than looping?
                    for word in word_tokenization:
                        # Increment individual word count
                        words[word] += 1

                        # Get sentence length, add that to total count
                        total_word_count += len(word_tokenization)

                        # Yo dawg I heard you like lengths. I'm gonna length your length.
                        word_length[len(word)] += 1

        # Dump it for the peoples
        # @todo Let's extract methods here so we can build this app up
        print(sorted(words.items(), key=operator.itemgetter(1), reverse=True))
        print(sorted(word_length.items(), key=operator.itemgetter(1), reverse=True))
        print("")
        print("{0} unique words: {1}, total words: {2} in {3} transcripts.  Average words per transcript: {4}".format(
            directory, len(words.items()),
            total_word_count, transcript_count, total_word_count / len(words.items())))
