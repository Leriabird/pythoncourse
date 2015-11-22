#! /usr/bin/env python3

with open ('yazkora.txt', 'r+') as ds:
   f = open('answer.txt', 'w')
   for line in ds:
       temp = line.split()
       for elt in temp:
           if elt[-2:] == 'yo':
               f.write(elt + ' ')
           if elt[-3:] == 'yo.':
               f.write(elt[:-1], '\n')
           if elt[-1:] == '.' and elt[-3:] != 'yo.':
               f.write('\n')

with open('yazkora.txt', 'r') as f:
   language = f.read()
 
language = language.split('.')
answer = open('answer.txt', 'w')
for sentence in language:
   sentence = sentence.replace('\n', ' ')
   words = sentence.split(' ')
   for word in words:
       if word[-2:] == 'yo':
           tmp = word + ' '
           answer.write(tmp)
   answer.write('\n')
answer.close()
