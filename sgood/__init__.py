from sgood.base import *

def sgood(input_filename, output_filename):
    """ Main function.  Use this. """
    raw = load_inputs(input_filename)
    tokens = tokenize(raw)
    parts_of_speech = tag(tokens)
    tokens = strip(tokens, parts_of_speech)
    words = build_freq_dist(tokens)
    write_csv(words, output_filename, parts_of_speech)
