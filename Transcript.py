from collections import defaultdict


class Transcript:
    title=""
    path = ""
    word_count = 0
    corpus = u""
    sentences = list
    word_frequencies = defaultdict(int)
    word_lengths = defaultdict(int)

    def __init__(self, transcript_path):
        self.path = transcript_path
        self.word_frequencies = defaultdict(int)
        self.word_lengths = defaultdict(int)

