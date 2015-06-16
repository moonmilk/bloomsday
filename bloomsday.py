#!/usr/bin/python
# coding: utf-8

# ranjit bhatnagar * moonmilk.com
# for bloomsday 2015


import re
import random
import time

# dialog is lines that start with emdash 
# except chapter numbers like -- I -- which also end with -
dialogre = re.compile('^Ñ(.*[^\Ñ])\s*$')

lines = open("ulysses-from-html.txt").read().splitlines()
dialog = [m.group(1) for m in map(dialogre.match, lines) if m]

while True:
	with open('utterance.txt', 'w') as f:
		f.write(random.choice(dialog))
	time.sleep(2)
	
