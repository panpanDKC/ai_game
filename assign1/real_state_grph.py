from real_game import *
import copy
import random as rand

class Node:
    def __init__(self, s, _score):
        self.string = s
        self.score = _score
        self.children = []
        self.heu = 0

def gen(s, _score):

    curr = Node(s, _score)

    if len(curr.string) <= 1:
        return curr
    
    sls,s1 = get_left(s,False)
    curr.children.append(gen(s1,curr.score + sls))

    sla,s2 = get_left(s,True)
    curr.children.append(gen(s2,curr.score + sla))

    srs,s3 = get_right(s,False)
    curr.children.append(gen(s3,curr.score + srs))

    sra,s4 = get_right(s,True)
    curr.children.append(gen(s4,curr.score + sra))
    return curr

def print_graph(nod,i):
    print("-"*i,end="")
    print("| str", nod.string,end="")
    print(" | sco",nod.score,end="")
    print(" | heu",nod.heu)
    for c in nod.children:
        print_graph(c,i+1)

def minimax(nod,maxi):
    if len(nod.string) == 1:
        if nod.score > 0:
            nod.heu = 1
        elif nod.score < 0:
            nod.heu = -1
        else:
            nod.heu = 0
        return nod.heu
    
    scores = []
    for c in nod.children:
        scores.append(minimax(c,not maxi))

    if maxi:
        nod.heu = max(scores)
    else:
        nod.heu = min(scores)
    
    return nod.heu

def get_start_str(top):
    a = 10 ** (top-1)
    b = 10 ** top
    r = rand.randint(a,b-1)
    return str(r)

#nod = gen('3857', 0)
#minimax(nod,True)
#print_graph(nod,0)

