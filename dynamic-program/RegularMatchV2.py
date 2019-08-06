class Solution:
    # 动态规划
    def isMatch(self, text, pattern) -> bool:
        memo = dict()

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if j == len(pattern):
                return i == len(text)
            first = i < len(text) and pattern[j] in {text[i], '.'}

            if j <= len(pattern) - 2 and pattern[j + 1] == '*':
                ans = dp(i, j + 2) or \
                      first and dp(i + 1, j)
            else:
                ans = first and dp(i + 1, j + 1)

            memo[(i, j)] = ans

        return dp(0, 0)


if __name__ == '__main__':
    print(Solution().isMatch('aaa', 'a.*'))
