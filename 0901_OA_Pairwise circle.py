"""
    Input pairs: [[3, 5], [1, 4], [2, 4], [1, 5], [2, 3]]
    Output: [3, 5, 1, 4, 2]
"""
import _collections


def pairwiseCircle(pairs: [[int]]) -> [int]:
    if not pairs:
        return None

    def addPair(ans, pair):
        if ans[0] == pair[0]:
            ans.appendleft(pair[1])
        elif ans[0] == pair[1]:
            ans.appendleft(pair[0])
        elif ans[1] == pair[0]:
            ans.append(pair[1])
        else:
            ans.append(pair[0])

    stack = [pairs[0]]
    seen = set()
    ans = _collections.deque()
    i = 1

    while stack:
        if not ans:
            pair = stack.pop()
            for each in pair:
                seen.add(each)
                ans.append(each)

        else:
            pair = stack.pop()
            if pair[0] not in seen and pair[1] not in seen:
                stack.append(pair)

            else:
                for each in pair:
                    seen.add(each)
                addPair(ans, pair)

        if i < len(pairs):
            stack.append(pairs[i])
            i += 1

    return list(ans)[:-1]


pairs = [[3, 5], [1, 4], [2, 4], [1, 5], [2, 3]]
print(pairwiseCircle(pairs))