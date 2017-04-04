from __future__ import absolute_import, division, print_function

import codecs
import operator
import os
import TranscriptService as TS
import nltk

for root, dirs, files in TS.transcript_dirs_list("transcripts"):

    # Setup tokenizer
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

    # You are -->> Here
    path = root.split(os.sep)

    # For Every Dir in Transcripts
    for directory in dirs:

        # All txt files in this Dir e.g. gwbush
        transcript_paths = path[0] + "/" + directory + "/*.txt"

        # Get list of sorted Transcript files
        transcripts = TS.get_transcripts_list(transcript_paths)

        # Let's look at each transcript file
        for transcript in transcripts:

            # Open file for reading
            with codecs.open(transcript.path, 'r', 'utf-8') as transcript_file:
                transcript.corpus += transcript_file.read()

            # Grab sentences by corpus...
            transcript.sentences = tokenizer.tokenize(transcript.corpus)

            # Inspect Sentences
            # @todo this is too nebulous it does a lot behind the scenes
            TS.inspect_sentences(transcript)

        ################################################################################################################
        # It prints the things
        ################################################################################################################
        # Dump it for the peoples
        # How many transcripts do we have?
        transcript_count = len(transcripts)

        # Word frequencies across all transcripts
        total_word_frequencies = TS.word_frequencies(transcripts)

        # Word count across all transcripts (just adding the frequencies list)
        total_word_count = sum(total_word_frequencies.values())

        print(sorted(total_word_frequencies.items(), key=operator.itemgetter(1), reverse=True))
        print(sorted(transcript.word_lengths.items(), key=operator.itemgetter(1), reverse=True))
        print("")
        print("{0}\n\tUnique words: {1}\n\tTotal words: {2} in {3} transcripts.\n\tAverage words per transcript: {4}"
            .format(
                directory,
                len(total_word_frequencies),
                total_word_count,
                transcript_count,
                total_word_count / transcript_count
            )
        )
        print("")
