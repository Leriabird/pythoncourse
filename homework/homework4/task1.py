#! /usr/bin/env python3

with open ('yazkora.txt', 'r+') as yazkora:
    answer = open('answer.txt', 'w')
    suffix = ('yo', 'yo.')
    dot = '.'
    for line in yazkora:
        line_list = line.split().strip()
        for word in line_list:
        #x = [elt for elt in line_list if elt.endswith(suffix)]
            if word.endswith(suffix):
                answer.write(word + ' ')
            elif word.endswith(dot):
                answer.write('\n')
    answer.close()

with open ('yazkora.txt', 'r') as yazkora:
    with open("answer.txt", "w") as answer:
    for line in yazkora:
            print(" ".join([word.enswith(suffix) and word 
                            or word.endswith(dot) and new_line for in line.strip().split()]),
                  end="", file=answer)