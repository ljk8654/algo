d = [5,9,3,7,2,6,3,9,3]
mc = len(d) - 1

INF =float('INF')
C = [[0 for _ in d] for _ in d]
P = [[0 for _ in d] for _ in d]

for sps in range(2, mc + 1): #Sub Problem Size
    for s in range(1, mc - sps + 2):
        e = s + sps - 1 # e is inclusive
        mult = INF
        for k in range(s, e):
            t = C[s][k] + C[k+1][e] + d[s-1] * d[k] * d[e]
            if mult > t:
                mult = t
                P[s][e] = k
        C[s][e] = mult

def getMulStr(s,e):
    if s== e: return f'A{s}'
    p = P[s][e]
    return f'({getMulStr(s,p)} X {getMulStr(p+1,e)})'

print(f'곱셈수 = {C[1][mc]} 수식={getMulStr(1,mc)}')