#!/usr/bin/env python
import urllib, re

uri = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s'
nothing_rep = "and the next nothing is (\d+)"
nothing = "12345"
temp = ""
print "Inicio "

while True:
        try:
                spam = urllib.urlopen(uri % nothing).read()
                nothing = re.search(nothing_rep, spam).group(1)
                print nothing
                temp = nothing
        except:
                print "Divida o ultimo por 2 e recomece."
                print "Recomecando..."
                break

nothing = str(int(temp)/2)
print "TEMP ",temp
print "NOTHING ",nothing 

while True:
        try:
                spam = urllib.urlopen(uri % nothing).read()
                nothing = re.search(nothing_rep, spam).group(1)
                print spam
                print nothing
        except:
                print "Pronto! Ufa..."
                print spam
                break
