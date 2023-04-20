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
