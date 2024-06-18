from sys import stdin as ss

''' 31120KB 68ms'''
doc = ss.readline().rstrip()
word = ss.readline().rstrip()

sp_doc = doc.split(word)
print(len(sp_doc) -1)