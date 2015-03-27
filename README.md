Sgood
=====
This repository contains a library scripts used for Grokking “What is Good?” in a body of text.

*Fun with NLTK, pygal, and word_cloud*

[NLTK](http://nltk.org "NLTK")
---
Analyze the full-text, tag parts of speech, provide word frequency
distirbutions

[pygal](http://pygal.org "pygal")
---
Create a barchart showing the Parts of Speech in the form of an .svg

[word_cloud](https://github.com/amueller/word_cloud "word_cloud")
---
Generate a wordcloud (independent from NLTK) in the form of a .png


Installing
---

Though these are disparate tools, you can install each to run the component
scripts manually. Start with:


`pip install Cython`

This above line goes into an `install_requires` section in a proper setup.py (coming soon).

After that, you then run:

`pip install -r requirements.txt`

which should contain all the component libraries you'll need


Authors
---

 - Ralph Bean <rbean@redhat.com>
 - Nate Case <qalthos@gmail.com>
 - Remy DeCausemaker <decause@redhat.com>

LICENSE
---

This project is licensed GPLv3. See `LICENSE` for details.
