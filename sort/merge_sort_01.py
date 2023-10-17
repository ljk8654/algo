import random

words = [

    '2020180027', 'hut', 'apostle', 'equipment', 'fop', 'refined', 'parapet', 'mog', 'amputate', 'covetous', 'somebody',

    'all', 'lobbyist', 'remark', 'subscriber', 'quorum', 'steppe', 'clean', 'cu', 'commend', 'prosy',

    'supererogation', 'indignation', 'wolverine', 'emporium', 'intersect', 'constitution', 'miscast', 'rabbi', 'enmity',
    'loft',

    'temporize', 'speedboat', 'agenda', 'delusion', 'class04', 'idolize', 'romance', 'overestimate', 'revive', 'smell',

    'modem', 'splat', 'snaky', 'drawn', 'smoke', 'darky', 'lotus', 'mufti', 'pithy', 'jewel', 'nexus',

    'fluff', 'piton', 'finis', 'drake', 'caulk', 'pussy', 'bless', 'weeds', 'realm', 'swoon', 'thorn',

    'plant', 'aorta', 'cupid', 'wafer', 'jewry', 'sinus', 'proud', 'grape', 'cable', 'carer', 'pearl',

    'piece', 'party', 'sleet', 'palmy', 'oiled', 'synod', 'trove', 'voice', 'chest', 'story', 'range',

    'scout', 'sewer', 'lowly', 'usher', 'seine', 'gulch', 'fever', 'frith', 'pylon', 'wager', 'banns',

    'merit', 'cheap', 'booby', 'truss', 'codex', 'sepia', 'totem', 'poult', 'dregs', 'giddy', 'umber',

    'mooch', 'smarm', 'loath', 'spoil', 'drink', 'wrick', 'awake', 'mural', 'glide', 'pinch', 'thine',

    'tawny', 'swede', 'shier', 'satan', 'triad', 'splay', 'tacit',

]
l_arr = len(words)
print(words, l_arr)

def merge(start, mid , end):  # mid is in left, end is inclusive
    merged = []
    l, r = start, mid + 1 #l은 A반 시작, r은 B반 시작
    while l <= mid and r <= end: #A반에 선수있다 and B반에 선수있다.
      if words[l] <= words[r]: #????: 싸움붙여서 A반선수가 지거나 비기면 등호가 없으면 stable하지 못함.
        merged.append(words[l]) #A반 줄서있어
        l += 1
      else:
        merged.append(words[r]) #B반 줄서있어
        r += 1
    if l <= mid:
        merged += words[l:mid+1]
        words[start:end + 1] = merged #남아있는 A반 선수들을 모두 merged 로
    else:
        #merged += array[r:end+1]
        words[start:r] = merged #남아있는 B 반 선수들을 모두 merged 로
   # while l <= mid: #A반에 선수가 있으면:
    #  merged.append(array[l])
     # l+=1
    #while r <= end: #B반에 선수가 있으면:
     # merged.append(array[r])
      #r+=1
    #array[start:end+1] = merged

def mergeSort(start, end):  # end: inclusive
   # size = end - start + 1
   # if size <= 1: return
    if start >= end: return
    mid = (start + end) // 2   # 중간 # 10~14, m = 12, 10~13, m = 11, 11~14 m=12
    mergeSort(start, mid)  # 왼쪽 절반
    mergeSort(mid + 1, end)        # 오른쪽 절반
    merge(start, mid, end) #( start1, end1, start2, end2)


mergeSort(0, l_arr - 1)
print(words)