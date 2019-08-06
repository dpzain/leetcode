class Solution(object):
    #动态规划 时间复杂度N^2
    def longestPalindrome(self, s):
        size = len(s)

        if size <= 1:
            return s
        # 二维 dp 问题
        # 状态：dp[l,r]: s[l:r] 包括 l，r ，表示的字符串是不是回文串
        # 设置为 None 是为了方便调试，看清楚代码执行流程
        dp =[[False for _ in range(size)] for _ in range(size)]

        longest_l = 1
        res = s[0]

        # 因为只有 1 个字符的情况在最开始做了判断
        # 左边界一定要比右边界小，因此右边界从 1 开始
        for r in range(1, size):
            for l in range(r):
                if s[l] == s[r] and (r - l <= 2 or dp[l + 1][r - 1]):
                    dp[l][r] = True
                    cur_len =r-l+1
                    if(cur_len>longest_l):
                        longest_l = cur_len
                        res =s[l:r+1]
            for i in dp:
                print(i)
            print("---------")
        return res





if __name__ == '__main__':
     ca = Solution()
     p=ca.longestPalindrome(['a','b','c','b','a','b','d','e'])
     print('最长回文串：%s' % p)
     # list = ["a","b","c","d"]
     # print(list[0:2])
