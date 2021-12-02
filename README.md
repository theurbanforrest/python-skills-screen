# python-skills-screen
Basic showcase of Python skills 10

## Questions

### Question 1
Given an array of integers, return how many of them contain an even number of digits.

Example 1:
Input: nums = [12,345,2,6,7896]
Output: 2

Explanation:
12 contains 2 digits (even number of digits).
345 contains 3 digits (odd number of digits).
2 contains 1 digit (odd number of digits).
6 contains 1 digit (odd number of digits).
7896 contains 4 digits (even number of digits).
Therefore only 12 and 7896 contain an even number of digits.
Example 2:
Input: nums = [555,901,482,1771]
Output: 1
Explanation:
Only 1771 contains an even number of digits.
Constraints:
1 <= nums.length <= 500
1 <= nums[i] <= 10^5


## Question 2
Given an array A of strings made only from lowercase letters, return a list of all characters that show up
in all strings within the list (including duplicates). For example, if a character occurs 3 times in all strings
but not 4 times, you need to include that character three times in the final answer.
You may return the answer in any order.
Example 1:
Input: ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:
Input: ["cool","lock","cook"]
Output: ["c","o"]
Note:
1 <= A.length <= 100
1 <= A[i].length <= 100
A[i][j] is a lowercase letter


## Question 3
Given a set of distinct integers, nums, return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.
Example:
Input: nums = [1,2,3]
Output:
[
[3],
[1],
[2],
[1,2,3],
[1,3],
[2,3],
[1,2],
[]
]