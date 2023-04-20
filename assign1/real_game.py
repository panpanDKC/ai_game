def get_left(s,m):
    a = int(s[0])
    b = int(s[1])

    if m:
        _sum = (a + b)%10
        return (get_res(_sum), str(_sum) + s[2::])
    _sub = (a - b%10 
    if _sub < 0:
        _sub = _sub*(-1)
    return (get_res(_sub), str(_sub) + s[2::])

def get_right(s,m):
    _len = len(s)
    a = int(s[_len-2])
    b = int(s[_len-1])
    
    if m:
        _sum = (a + b)%10
        return (get_res(_sum), s[0:(_len-2)] + str(_sum))
    _sub = (a - b)%10
    if _sub < 0:
        _sub = _sub*(-1)
    return (get_res(_sub), s[0:(_len-2)] + str(_sub))

def get_res(n):
    res = 0

    if n % 2 == 1:
        res += 1
    else:
        res -= 1

    if n >= 5:
        res += 2
    else:
        res -= 2

    return res

def check_take_off(s,n,side):
    _len = len(s)
    if not side:
        if n == int(s[_len - 1]):
            return True
    else:
        if n == int(s[0]):
            return True
    return False


