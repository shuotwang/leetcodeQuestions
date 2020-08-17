def decodeString(self, s: str) -> str:
    stack = []

    for c in s:
        if stack and c == ']':
            string = []
            while stack and stack[-1] != '[':
                string.append(stack.pop())
            string.reverse()

            # now stack[-1] == '['
            if stack[-1] == '[':
                stack.pop()
                num = []
                while stack and stack[-1].isdigit():
                    num.append(stack.pop())
                num = ''.join(num[::-1])
                num = int(num) if num else 0

                for each in (num * string):
                    stack.append(each)
        else:
            stack.append(c)

    ans = []
    while stack:
        ans.append(stack.pop())
    return ''.join(ans)[::-1]
