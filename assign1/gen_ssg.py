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
