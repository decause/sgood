#!/usr/bin/env python


import sgood

import logging
logging.basicConfig(level=logging.DEBUG)

sgood.sgood('data/presinaug-addresses.txt', 'foo.csv')
