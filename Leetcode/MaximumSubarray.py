class Solution:
    def maxSubArray(self, nums) -> int:

        result_list = []
        if len(nums) == 1:
            return nums[0]

        else:

            for i in range(0,len(nums)):
                x = [nums[i]]
                print(x)
                result_list.append(sum(x))
                for z in range(i+1,len(nums)):

                    x = nums[i:z+1]
                    print(x)

                    result_list.append(sum(x))
                print(result_list)
        return max(result_list)

obj1 = Solution()
nums =[-1,-1,-1,-2,-1]
print(obj1.maxSubArray(nums))
# print(result)