class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        t_counter = Counter(t)
        t_chars = len(t_counter)
        cur_counter = defaultdict(int)
        cur_chars = 0

        l, r = 0, 0
        ans = float('inf'), 0, 0

        while r < len(s):
            char = s[r]
            cur_counter[char] += 1

            if char in t_counter and t_counter[char] == cur_counter[char]:
                cur_chars += 1

            while l <= r and t_chars == cur_chars:

                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                char = s[l]

                cur_counter[char] -= 1
                if char in t_counter and cur_counter[char] < t_counter[char]:
                    cur_chars -= 1
                l += 1

            r += 1

        return "" if ans[0] == float('inf') else s[ans[1]: ans[2] + 1]
