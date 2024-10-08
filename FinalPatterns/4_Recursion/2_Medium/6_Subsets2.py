from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        response = []
        nums.sort()

        def helper(ind, curr):

            response.append(curr.copy())

            for i in range(ind, len(nums)):

                if i!=ind and nums[i]==nums[i-1]:
                    continue

                curr.append(nums[i])
                helper(i+1,curr)
                curr.pop()



        helper(0,[])

        return response


# ([1,2,3]))
print(Solution().subsetsWithDup(([1,1,2])))
# print(Solution().





class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        response = []
        subset = []
        nums.sort()


        def helper(ind) :

            if ind>=len(nums):
                response.append(subset[::])

                print(subset)
                return


            subset.append(nums[ind])
            helper(ind+1)

            subset.pop()
            while ind+1 <len(nums) and nums[ind] == nums[ind+1]:
                ind+=1
            helper(ind+1)



        helper(0)


        return response

print(Solution().subsetsWithDup(([1,2,2,3])))