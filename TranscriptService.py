from Transcript import Transcript
from collections import defaultdict

import glob
import os

paths = ""


def sentence_to_wordlist(raw):
    clean = raw.lower()
    cleaned_words = clean.split()
    return cleaned_words


def sorted_paths(paths):
    return sorted(glob.glob(paths))


def transcript_dirs_list(transcript_dir):
    return os.walk(transcript_dir)


def get_transcripts_list(paths):
    # Get list of sorted Transcript files
    transcripts = []
    for path in sorted_paths(paths):
        transcripts.append(Transcript(path))
    return transcripts


def valid_sentence(sentence):
    return len(sentence) > 0


def inspect_sentences(transcript):
    # Let's look at each sentence
    for sentence in transcript.sentences:

        # Sentences gotta sentence
        if valid_sentence(sentence):
            inspect_words(sentence, transcript)


def inspect_words(wordlist, transcript):
    # Split up the words
    words = sentence_to_wordlist(wordlist)

    # Gettin Loopy With Loops(tm), Let's evaluate each word.
    # @todo is there a method to do this rather than looping?
    for word in words:
        # @todo need to strip words of punctuation - counts are off
        # Increment individual word count
        transcript.word_frequencies[word] += 1

        # Get sentence length, add that to total count
        transcript.word_count += len(words)

        # Yo dawg I heard you like lengths. I'm gonna length your length.
        transcript.word_lengths[len(word)] += 1


def word_frequencies(transcript_list):
    word_freqs = defaultdict(int)
    for transcript in transcript_list:
        for word, count in transcript.word_frequencies.items():
            word_freqs[word] += count
    return word_freqs

