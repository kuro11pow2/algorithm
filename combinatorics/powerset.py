from measure import measure
from itertools import chain, combinations

@measure
def powerset1(li):
    return sum([list(combinations(li, n)) for n in range(len(li)+1)], [])

@measure
def powerset2(li):
    res = []
    n = len(li)
    for i in range(1 << n):
        tmp = []
        for j in range(n):
            if i & (1 << j):
                tmp.append(li[j])
        res.append(tuple(tmp))
    return res

if __name__ == "__main__":
    items = [chr(ord('0') + i) for i in range(4)]
    out1 = powerset1(items)
    out2 = powerset2(items)
    same = True
    for i, (a, b) in enumerate(zip(*map(sorted, [out1, out2]))):
        if a != b:
            same = False
        print(f'{i}: {a}\n   {b}')
    print(f'{same=}')