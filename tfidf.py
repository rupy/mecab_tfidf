#!/usr/bin/python
# -*- coding: utf-8 -*-

from mymecab import MyMecab
from collections import defaultdict
from math import log
from prettyprint import pp, pp_str

class WordCount:

  def __init__(self):
    self.m = MyMecab()
    self.tf = {}
    self.all_tf = defaultdict(int)
    self.df = defaultdict(int)
    self.tfidf = defaultdict(dict)

  def calc_tfidf(self, documents):
    doc_num = len(documents)
    # 文書名と文書内容を取り出す
    for doc_name, doc in documents.items():
      d = defaultdict(int)
      # 文書の形態素解析により単語の原型を取り出す
      words = self.m.getFeature(doc, MyMecab.MECAB_FEATURE_BASE)
      # 得られた単語に対して数を数える
      for word in words:
        d[word] += 1 # 単語頻度（tf）のため
        self.all_tf[word] += 1 # 文書頻度（df）のため
      self.tf[doc_name] = d

    # すべての単語でループする
    for word in self.all_tf.keys():
      # 全ドキュメントでループする
      for doc_name in documents.keys():
        # 単語が数えられていたら
        if word in self.tf[doc_name] and self.tf[doc_name][word] > 0:
            # 単語頻度dfの計算
            self.df[word] += 1

      for doc_name in documents.keys():
        # tf-idfの計算
        if word in self.tf[doc_name]:
          # print doc_name
          # print word
          # print self.tf[doc_name][word]
          # print float(self.df[word])
          # print log(doc_num / float(self.df[word]))
          self.tfidf[doc_name][word] = self.tf[doc_name][word] * log(doc_num / float(self.df[word]))
        # else:
        #   self.tfidf[doc_name][word] = 0

# wc = WordCount()

# documents = {
#   "text0": "I am a japanese student.",
#   "text1": "こんにちは。私は太郎ですよ。私はげんきです",
#   "text2": "こんにちは。いい天気ですね。私は気分が良いです。",
#   "text3": "こんにちは。元気ですか？"
# }

# wc.calc_tfidf(documents)
# pp(wc.tf)
# pp(wc.df)
# pp(wc.tfidf)

