"""
Zigzag: a triple <a, b, c>, a < b > c or a > b < c

"""

def zigzag(triples: [int]) -> [int]:
    ans = []
    for i in range(len(triples) - 2):
        if (triples[i] - triples[i + 1]) * (triples[i + 1] - triples[i + 2]) < 0:
            ans.append(1)
        else:
            ans.append(0)

    return ans


triples = [1, 2, 1, 3, 4]
print(zigzag(triples))