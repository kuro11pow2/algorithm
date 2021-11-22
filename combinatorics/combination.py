import sys, os.path as op
sys.path.append((pDir:=lambda x, n, i=0: pDir(op.abspath(op.dirname(x)), n, i+1) if i < n else x)(__file__, 3))
from measure import measure

from itertools import combinations

@measure
def myCombinations(li, n):
    nLi = len(li)
    arr = []
    ret = []
    def recurse(idx):
        if len(arr) == n:
            ret.append(tuple(map(lambda x: li[x], arr)))
            return
        for i in range(idx, nLi):
            arr.append(i)
            recurse(i + 1)
            arr.pop()
    recurse(0)
    return ret

if __name__ == "__main__":
    items = [chr(ord('0') + i) for i in range(5)]
    com = combinations(items, 3)
    myCom = myCombinations(items, 3)
    same = True
    for a, b in zip(com, myCom):
        if a != b:
            same = False
        print(a, b)
    print(f'{same=}')