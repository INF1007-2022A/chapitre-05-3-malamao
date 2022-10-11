#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

def get_num_letters(text):
	nb = 0
	for chr in text:
		if chr.isalnum():
			nb+=1
	return nb


def get_word_length_histogram(text):
	mots = text.split()
	dic = {}
	histogramme = []
	for n in range (len(mots)):
		nb_lettres = get_num_letters(mots[n])
		if nb_lettres not in dic:
			dic[nb_lettres] = 1
		else:
			dic[nb_lettres] += 1
	#trouver la clé la plus grande
	limite = 0
	for cle in dic:
		if cle > limite:
			limite = cle
	for n in range(limite+1):
		if n in dic:
			histogramme.append(dic[n])
		else:
			histogramme.append(0)
	return histogramme

def format_histogram(histogram):
	etoile = "*"
	histo = ""
	alignement = len(str(len(histogram) - 1))
	for i in range(1, len(histogram)):
		nb_etoiles = histogram[i]
		histo += f'{i: >{alignement}}' + f'{nb_etoiles*etoile}' +"\n"
	return histo

def format_horizontal_histogram(histogram):
	BLOCK_CHAR = "|"
	LINE_CHAR = "¯"
	histo = ""
	for i in range(max(histogram), 0, -1):
		for n in range(1, len(histogram)):
			if (i <= histogram[n]):
				histo += BLOCK_CHAR
			else:
				histo += " "
		histo += "\n"
	histo += LINE_CHAR * len(histogram)
	return histo


if __name__ == "__main__":
	spam = "Stop right there criminal scum! shouted the guard confidently."
	eggs = get_word_length_histogram(spam)
	print(eggs, "\n")
	print(format_histogram(eggs), "\n")
	print(format_horizontal_histogram(eggs))
