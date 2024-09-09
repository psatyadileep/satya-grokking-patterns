
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        response = []
        subset = []



        def helper(ind):



            if ind>=len(nums):
                response.append(subset[::])
                return


            subset.append(nums[ind])
            helper(ind+1)

            subset.pop()
            while ind+1 <len(nums) and nums[ind] == nums[ind+1]:
                ind+=1
            helper(ind+1)

        helper(0)


        return response
