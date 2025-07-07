class Solution:
    def fizzBuzz(self, n):
        answer = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                answer.append("FizzBuzz")
            elif i % 3 == 0:
                answer.append("Fizz")
            elif i % 5 == 0:
                answer.append("Buzz")
            else:
                answer.append(str(i))
        return answer


ret = Solution().fizzBuzz(16)
print(ret)

# LeetCode Problem: Two Sum


class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i


sol = Solution()
nums = [2, 5, 3, 6]
target = 8
ret = sol.twoSum(nums, target)
print(ret)
