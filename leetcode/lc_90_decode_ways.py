class Solution:
    def num_decodings(self, s: str) -> int:
        dp = [0]*(len(s)) + [1]  # dp[len(s)] = 1 => "" empty string has 1 way of decoding "none"
        for i in range(len(s) - 1, -1, -1):
            if int(s[i]) == 0:
                continue  # 0 at the beginning could not be encoded to anything
            
            for j in range(i, i+2):             
                if j+1 > len(s) or int(s[i:j+1]) > 26:
                    break
                # valid digit to be encoded/decoded
                print("dp j+1", dp[j+1])
                dp[i] += dp[j+1]
        return dp[0]
            

def main():
    s = Solution()
    number = "11101"
    print(f"The number of ways to decode the string '{number}' is {s.num_decodings(number)}.")
    

if __name__ == "__main__":
    main()
