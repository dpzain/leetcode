# 正则表达式匹配问题
# 给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。
#
# '.' 匹配任意单个字符
# '*' 匹配零个或多个前面的那一个元素
#
# 所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。
#
# 说明:
#     s 可能为空，且只包含从 a-z 的小写字母。
#     p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *
# 来源：LeetCode
# 链接：https://leetcode-cn.com/problems/regular-expression-matching


class Solution:
    # 回溯 暴力递归
    def isMatch(self, text, pattern) -> bool:
        if not pattern: return not text
        first_match = text and pattern[0] in {text[0], '.'}

        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.isMatch(text, pattern[2:])) or \
                   first_match and self.isMatch(text[1:], pattern)
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])


if __name__ == '__main__':
    print(Solution().isMatch('aaa', 'a.*'))
