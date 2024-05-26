from typing import List


class Solution:
    def longest_conseq_seq(self, nums: List[int]) -> int:
        numsSet = {n: False for n in nums}  # False means not visited
  
        seqCount = 0
        maxSeqCount = 0
        for n in numsSet:
            if numsSet[n]:
                continue  # key was already visited, jump to the next key
            
            numsSet[n] = True  # set current number n as visited
            seqCount = 1  # reset seq. count, 1 because n is counted as the first element in the sequecne
            
            # 1st go down until no more consequtive keys (n) are found
            i = 1
            while n-i in numsSet:
                numsSet[n-i] = True  # set as visited
                seqCount += 1
                i += 1
                
            i = 1
            while n+i in numsSet:
                numsSet[n+i] = True  # set as visited
                seqCount += 1
                i += 1

            maxSeqCount = max(maxSeqCount, seqCount)
        return maxSeqCount


def main():
    solution = Solution()
    nums = [100, 4, 200, 1, 3, 2]
    print(solution.longest_conseq_seq(nums))  # Output: 4


if __name__ == "__main__":
    main()
