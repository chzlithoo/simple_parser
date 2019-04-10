# -*- coding: utf-8 -*-
from konlpy.tag import Kkma
import os
import codecs


kkma = Kkma()


def preprocess_noun(text):
	res = []
	pos_tagged = kkma.nouns(text)
	for word in pos_tagged:
		if len(word) > 1:
			res.append(word)
	return ' '.join(res)


def get_refined_text(path):
	res = []
	with codecs.open(path, 'r', encoding='utf-8', errors='ignore') as raw:
		for line in raw:
			processed = preprocess_noun(line)
			if len(processed) > 1:
				res.append(processed)
	return res


data_path = '/Users/jungwonchoi/Downloads/sysy/'

out_res = []
for pp in os.listdir(data_path):
	ppath = data_path+pp
	try:
		refined_res = get_refined_text(ppath)
		txt = " ".join(refined_res)
		out_res.append(txt)
	except:
		continue


with open('/Users/jungwonchoi/Downloads/out.txt', 'w') as out:
	for t in out_res:
		out.write(t+"\n")