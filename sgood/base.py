import csv

import nltk
from nltk import FreqDist

import sgood.config

import logging
log = logging.getLogger('sgood')


def load_inputs(filename):
    log.info("* Loading corpus")
    # Open a csv, read the whole thing
    with open(filename, "r") as f:
        raw = f.read()
    return raw


def tokenize(raw):
    log.info("* Tokenizing")
    tokens = nltk.word_tokenize(raw)
    return tokens


def tag(tokens):
    log.info("* Tagging parts of speech")
    # Save this to strip articles later
    parts_of_speech = nltk.pos_tag(tokens)

    log.info("* Converting POS list into a dict for lookup")
    # TODO -- fix this.  this is going to have a hard time with homonyms
    parts_of_speech = dict(parts_of_speech)

    return parts_of_speech


def strip(tokens, parts_of_speech,
          banned_parts_of_speech=sgood.config.banned_parts_of_speech,
          banned_words=sgood.config.banned_words):
    log.info("* Stripping stuff we don't want")
    # Strip punctuation and banned parts of speech
    tokens = [
        token for token in tokens if (
            # remove punctuation
            token.isalpha() and
            # remove parts of speech that we don't want.
            not parts_of_speech[token] in banned_parts_of_speech and
            not token in banned_words #and
            #len(token) > 4
        )
    ]
    return tokens

def build_freq_dist(tokens):
    log.info("* Building frequency distribution")
    words = FreqDist(tokens)
    return words


def write_csv(words, filename, parts_of_speech, n=10000):
    '''
    Open a CSV, write top n words to it, log.info(top n words)
    '''
    log.info("* Printing top %i words" % n)
    f = open(filename, 'wb')
    writer = csv.writer(f)
    for i, pair in enumerate(words.items()):
        word, count = pair
        row = word, count, parts_of_speech[word]
        writer.writerow(row)
        log.info("%r appeared %i times. Its part of speech is %r" % (
            word, count, parts_of_speech[word],
        ))
        if i > n:
            break
    f.close()
    return (word, count, parts_of_speech)
