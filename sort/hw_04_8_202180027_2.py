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

def partition(arr, beg, end): # end: exclusive
    ri = random.randrange(beg, end)
    arr[beg], arr[ri] = arr[ri], arr[beg]

    pv = arr[beg] #맨 왼쪽이 피벗

    p, q = beg, end
    while True:#역전안했으면:
        while True: #p 증가:
            p += 1
            # if p >= end: break Q만 비교하면 됨
            if p >= q: break
            if arr[p] < pv: break
        while True: #q 감소:
            q -= 1
            if p > q: break
            if arr[q] >= pv: break
        if p >= q: break
        arr[p], arr[q] = arr[q], arr[p] #@p <=> @q
    arr[q], arr[beg] = arr[beg], arr[q]
    return q
def quickSort(arr, beg, end): #end: exclusive
    size = end - beg
    if size <= 1: return
    pi = partition(arr, beg, end)
    quickSort(arr, beg, pi)
    quickSort(arr, pi + 1, end)
    pass

quickSort(words, 0, l_arr)

print(words)