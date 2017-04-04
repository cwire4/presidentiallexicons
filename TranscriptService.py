import Transcript


def sentence_to_wordlist(raw):
    clean = raw.lower()
    cleaned_words = clean.split()
    return cleaned_words


def sorted_paths(individual_path):
    return sorted(glob.glob(transcript_paths))


def transcript_dirs_list():
    return os.walk("transcripts")


def get_transcripts_list(paths):
    # Get list of sorted Transcript files
    transcripts = []
    for path in sorted_paths(paths):
        transcripts.append(Transcript(path))
    return transcripts


def valid_sentence(sentence):
    return len(sentence) > 0

