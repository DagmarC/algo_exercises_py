
class Solution:
    def minimum_beautiful_substr(self, s: str) -> int:
        # powers_of_five = {"1", "101", "11001", "1111101", "1001110001", "110000110101", "11110100001001"}
        powers_of_five = {bin(5**i)[2:] for i in range(7)}  # [2:] removes the '0b' prefix
        
        def isPower(substr: str) -> bool:
            return substr in powers_of_five
        
        def rec_find_power(start, mid, end):
            if mid == end:
                res = 1 if isPower(s[start:mid]) else float('inf')
                return res
            
            if s[start] == "0":
                return float('inf')
            
            isLeft = isPower(s[start:mid])
            left = 1 + rec_find_power(mid, mid+1, end) if isLeft else float('inf')
            right = rec_find_power(start, mid+1, end)
            
            return min(left, right)
        
        result = rec_find_power(0, 1, len(s))
        return result if result != float('inf') else -1
       
    def minimum_beautiful_substr_dp(self, s: str) -> int:
        # Number in dp table represents the minimum beautiful substrings found
        # Subproblems: dp[0] - substring s[0-len(s)], dp[1] - substring s[1-len(s)], dp[2] - substring s[2-len(s)], ..., dp[len(s)] = 0 (empty substring "" there is 0 beautiful substrings)
        dp = [float('inf')] * len(s) + [0]
        powers_of_five = {bin((5**i))[2:] for i in range(7)}

        # loop over the string in reversed order and if s[i:j+1] is power of five, decide whether it is min or not
        for i in range(len(s)-1, -1, -1):
            if s[i] == "0":
                continue  # it cant begin with 0
            
            for j in range(i, len(s)):
                subproblem = s[i:j+1]
                #  Decide whether the subproblem is better only if it is a power of five
                if subproblem in powers_of_five:
                    dp[i] = min(dp[i], dp[j+1]+1)  # dp[i] holds the minimum value discovered so far. If a new minimum is found via the smaller subproblem dp[j+1] + 1(current), then dp[i] is updated.
                         
        return dp[0] if dp[0] != float('inf') else -1


def main():
    s = Solution()
    # assert -1 == s.minimum_beautiful_substr("0")
    print(s.minimum_beautiful_substr_dp("111"))  # 3
    print(s.minimum_beautiful_substr_dp("1011"))  # 2
    # assert 2 == s.minimum_beautiful_substr("1011")
    # assert 4 == s.minimum_beautiful_substr("100111000110111")
    print(s.minimum_beautiful_substr_dp("101101111110111"))  # 5


if __name__ == "__main__":
    main()
