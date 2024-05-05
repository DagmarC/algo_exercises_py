class Solution:
    def minimum_beautiful_substr(self, s: str) -> int:
        powers_of_five = {1: "1", 3: "101", 5: "11001", 7: "1111101",
                          10: "1001110001", 12: "110000110101",
                          14: "11110100001001"}
        
        if s[len(s)-1] != "1" or s[0] != "1":
            return -1
        
        dp = [float('inf')] * (len(s) + 1)
        print(dp)
        def is_power_five(sub: str) -> int:
            if len(sub) in powers_of_five and powers_of_five[len(sub)] == sub:
                return 1
            else:
                return float('inf')
      
        def beautiful_substring(s: str, start: int, end: int):
            print("sub={} s={}, start={}, end={}".format(s[start:end], s, start, end))
            
            if start > end or start >= len(s):
                return float('inf')
            
            if s[start] == "0":
                print("0 inf")
                return float('inf')
            
            if end == len(s):
                print("leaf node is power sub = {} start{}:{}end".format(s[start:end], start, end))
                return is_power_five(s[start:end])  # leaf node
            
            left = beautiful_substring(s, start, end+1)
            print("LEFT END\n", left)
            right = beautiful_substring(s, end, end+1)
            
            a = min(left, right)
            dp[start] = min(a, dp[end] + is_power_five(s[start:end]))
            print("dp={} left = {}, right = {} sub={}, start={}, end={}\n".format(dp, left, right, s[start:end], start, end))
                            
            return dp[end]
        
        print("-------", s)
        return beautiful_substring(s, 0, 1)


def main():
    s = Solution()
    # assert -1 == s.minimum_beautiful_substr("0")
    print(s.minimum_beautiful_substr("111"))
    print(s.minimum_beautiful_substr("1011"))
    # assert 2 == s.minimum_beautiful_substr("1011")
    # assert 4 == s.minimum_beautiful_substr("100111000110111")
    # assert 6 == s.minimum_beautiful_substr("101101111101")


if __name__ == "__main__":
    main()
