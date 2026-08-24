class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        m = len(text1)
        n = len(text2)

        # Create DP table
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):

                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]

                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # Find the actual LCS
        i = m
        j = n
        lcs = []

        while i > 0 and j > 0:

            if text1[i - 1] == text2[j - 1]:
                lcs.append(text1[i - 1])
                i -= 1
                j -= 1

            elif dp[i - 1][j] > dp[i][j - 1]:
                i -= 1

            else:
                j -= 1

        # We found it backwards, so reverse it
        lcs.reverse()

        print("Longest Common Subsequence:", "".join(lcs))
        return dp[m][n]


# Take input from user
text1 = input("Enter the 1st text: ")
text2 = input("Enter the 2nd text: ")

# Create object
solution = Solution()

# Call method
result = solution.longestCommonSubsequence(text1, text2)

print("Length of Longest Common Subsequence:", result)