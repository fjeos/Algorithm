from math import gcd
def solution(w,h):
    w, h = max(w, h), min(w, h)
    repeat = gcd(w, h)
    
    n_w = w // repeat
    n_h = h // repeat
    
    out = (n_w * n_h) - ((n_w - 1) * (n_h - 1))
        
    return (w * h) - (out * repeat)