class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        count = 0
        for i in range(len(nums)):
            i_val = nums[i]
            count += 1
            for j in range(count, len(nums)):
                j_val = nums[j]
                if i_val + j_val == target:
                    output.append(i)
                    output.append(j)
                    return output

        