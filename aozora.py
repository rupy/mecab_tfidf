#!/usr/bin/python
# -*- coding: utf-8 -*-

import MeCab
import sys
import string
import os
import codecs
from tfidf import WordCount
from prettyprint import pp, pp_str


wc = WordCount()
documents = {}
for folder in os.listdir("aozora/"):
    if folder != "夏目漱石":
        continue
    for file in os.listdir("aozora/" + folder):
        path = "aozora/" + folder + "/" + file
        print path
        # print os.path.exists(path)

        documents[file] = "\n".join([line.encode('utf-8') for line in codecs.open(path, 'r', 'shift_jis')])

# exit()
wc.calc_tfidf(documents)
#pp(wc.tf)
# pp(wc.df)
for k, v in sorted(wc.tfidf['こころ.txt'].items(), key=lambda x:x[1]):
    print k, v

