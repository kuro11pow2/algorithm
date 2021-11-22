import sys, os.path as op
sys.path.append((pDir:=lambda x, n, i=0: pDir(op.abspath(op.dirname(x)), n, i+1) if i < n else x)(__file__, 3))
from measure import measure

from itertools import permutations

@measure
def myPermutations(li, n):
    visited = [False for _ in li]
    arr = []
    ret = []
    def recurse():
        if len(arr) == n:
            ret.append(tuple(map(lambda x: li[x], arr)))
            return
        for i in range(len(li)):
            if visited[i]:
               continue
            visited[i] = True
            arr.append(i)
            recurse()
            arr.pop()
            visited[i] = False
    recurse()
    return ret

if __name__ == "__main__":
    items = [chr(ord('0') + i) for i in range(5)]
    per = permutations(items, 3)
    myPer = myPermutations(items, 3)
    same = True
    for a, b in zip(per, myPer):
        if a != b:
            same = False
        print(a, b)
    print(f'{same=}')