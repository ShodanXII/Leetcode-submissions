class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []

        for i in range(len(nums)):
            first = []
            wanted = target - nums[i]
            k = i + 1
            while k <= (len(nums ) -1):
                if nums[k] == wanted:
                    answer.append(i)
                    answer.append(k)
                    return answer
                k+= 1
        return answer
            