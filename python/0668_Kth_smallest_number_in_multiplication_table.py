668. Kth Smallest Number in Multiplication Table

Nearly everyone has used the Multiplication Table. The multiplication table of size m x n is an integer matrix mat where mat[i][j] == i * j (1-indexed).

Given three integers m, n, and k, return the kth smallest element in the m x n multiplication table.

Example 1:
Input: m = 3, n = 3, k = 5
Output: 3
Explanation: The 5th smallest number is 3.

Example 2:
Input: m = 2, n = 3, k = 6
Output: 6
Explanation: The 6th smallest number is 6.
 
Constraints:
1 <= m, n <= 3 * 104
1 <= k <= m * n

Source: https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/
Solution:
- Leetcode: https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/editorial/
- AlgoMonster: https://algo.monster/liteproblems/668

Pattern:
- Math
- Binary Search

Final Solution
```
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        # Initialize the search range between 1 and m*n
        left, right = 1, m * n
      
        # Binary search to find the k-th smallest number
        while left <= right:
            mid = (left + right) // 2  # Use floor division for Python3
            count = 0

            # Count the number of values less than or equal to mid in the 2D multiplication table
            '''
            Source: https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/editorial/
            This leaves us with the task of counting how many values are less than or equal to x.
            For each of m rows, the ith row looks like [i, 2*i, 3*i, ..., n*i].
            The largest possible k*i ≤ x that could appear is k = x // i.
            However, if x is really big, then perhaps k > n, so in total there are min(k, n) = min(x // i, n) values in that row that are less than or equal to x.
            '''
            for i in range(1, m + 1):
                count += min(mid // i, n)

            # If the count is greater than or equal to k, search the left half
            '''
            Source: ChatGPT
            Multiplication tables have repeated values because of symmetric properties (e.g., 2×3=3×2).
            When count == k, directly returning mid is incorrect because might not be the smallest number that satisfies the 
            k-th position. For example, if there are multiple numbers with the same value at mid, you need to check if 
            mid truly represents the k-th smallest number by refining the search range further.
            '''
            if count >= k:
                right = mid - 1
            # If the count is less than k, search the right half
            else:
                left = mid + 1

         # The left pointer will be at the k-th smallest number after exiting the loop
        return left
```
Time complexity: O(m * log(m*n))
Space complexity: O(1)
