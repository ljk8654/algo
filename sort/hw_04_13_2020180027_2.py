edges = [ 
  (0, 4, 463), (0, 11, 347), (0, 12, 410), (0, 20, 294), (0, 21, 360), 
  (1, 5, 61), (1, 10, 343), (1, 17, 395), (2, 6, 162), (2, 10, 431), 
  (2, 16, 135), (2, 17, 415), (2, 18, 281), (2, 23, 435), (3, 4, 59), 
  (3, 15, 230), (3, 21, 118), (4, 11, 393), (4, 15, 273), (5, 9, 341), 
  (5, 10, 333), (5, 23, 427), (6, 10, 268), (6, 12, 432), (6, 14, 465), 
  (6, 16, 298), (6, 18, 278), (6, 19, 199), (7, 9, 120), (7, 13, 257), 
  (7, 24, 410), (8, 11, 275), (8, 12, 111), (8, 15, 407), (8, 19, 420), 
  (8, 20, 481), (9, 10, 341), (9, 23, 253), (9, 24, 357), (11, 15, 141), 
  (12, 16, 194), (12, 19, 410), (12, 20, 370), (12, 22, 324), (13, 14, 375), 
  (13, 17, 323), (13, 22, 318), (13, 23, 83), (14, 19, 350), (14, 24, 211), 
  (15, 21, 177), (16, 18, 348), (16, 20, 421), (18, 24, 377), (19, 22, 211), 
  (19, 23, 376), (22, 23, 400), (23, 24, 335), 
]
num_vertex = 25

mst = []

import collections
g = collections.defaultdict(dict)
# g = [dict() for _ in range(num_vertex)] # 빈 딕셔너리 생성
# g = {v : dict() for v in range(num_vertex)}

for s,e,w in edges:
  g[s][e] = w
  g[e][s] = w #중복 저장으로 비용 알 수 있음 g의 type: list

import heapdict

D = heapdict.heapdict()
origins = dict()
completed = set()

start_index = 15
completed.add(start_index)

#for adj, weight in g[start_index].items(): #시작점 주변에 있는 점들
#  D[adj] = weight
  # D[adj] = g[start_index][adj]
#  origins[adj] = start_index
D[start_index] = 0

#main loop
while D:
  fix_to, fix_w = D.popitem()
  completed.add(fix_to)
  if fix_to != start_index:
    fix_fr = origins[fix_to]
    mst.append((fix_fr, fix_to, fix_w))
  for adj, adj_w in g[fix_to].items():
    #1. in mst? : ignore
    if adj in completed: continue
    #2. not adj in D: add
    #3. D[adj] <= adj_w (fix_to~adj) : ignore
    #4. D[adj] > adj_w (fix_to~adj) : update
    if not adj in D or D[adj] > adj_w:
      D[adj] = adj_w
      origins[adj] = fix_to
print(mst)