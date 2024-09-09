class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        response = []

        def helper(ind,curr):
            response.append(curr[:])
            for i in range(ind,len(nums)):

                # check Duplicates

                if i!=ind and nums[i] == nums[i-1]:
                    continue

                curr.append(nums[i])
                helper(i+1,curr)
                curr.pop()

        helper(0,[])
        return response[2,,]

print(Solution().subsets([1,2,3]))
