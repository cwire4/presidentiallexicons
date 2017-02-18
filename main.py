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


for root, dirs, files in os.walk("transcripts"):
    path = root.split(os.sep)
    for directory in dirs:
        transcript_count = 0
        total_word_count = 0
        individualpath = path[0] + "/" + directory + "/*.txt"

        transcripts = sorted(glob.glob(individualpath))
        # print(transcripts)
        corpus_raw = u""
        for transcript in transcripts:
            transcript_count += 1
            # print("Reading '{0}'...".format(transcript))
            with codecs.open(transcript, 'r', 'utf-8') as transcript_file:
                corpus_raw += transcript_file.read()
                # print("Corpus is now {0} characters long".format(len(corpus_raw)))
                # print()
            tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
            raw_sentences = tokenizer.tokenize(corpus_raw)
            words = defaultdict(int)
            word_length = defaultdict(int)
            for sentence in raw_sentences:
                if len(sentence) > 0:
                    word_tokenization = sentence_to_wordlist(sentence)
                    for word in word_tokenization:
                        words[word] += 1
                        total_word_count += len(word_tokenization)
                        word_length[len(word)] += 1

        print(sorted(words.items(), key=operator.itemgetter(1), reverse=True))
        print(sorted(word_length.items(), key=operator.itemgetter(1), reverse=True))
        print("")
        print("{0} unique words: {1}, total words: {2} in {3} transcripts.  Average words per transcript: {4}".format(
            directory, len(words.items()),
            total_word_count, transcript_count, total_word_count / len(words.items())))
